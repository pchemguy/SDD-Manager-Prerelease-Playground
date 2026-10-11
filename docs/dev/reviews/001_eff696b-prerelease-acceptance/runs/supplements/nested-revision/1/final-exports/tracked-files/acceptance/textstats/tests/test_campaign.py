"""Required/optional coverage and compatibility sensitivity, not live acceptance."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from . import test_catalog as assets
catalog = assets.catalog


class VariantCatalog(unittest.TestCase):
    setUp = assets.CatalogIntegrity.setUp
    def test_unknown_requirement_and_optional_prerequisite_are_rejected(self):
        for change in ('unknown', 'optional-gate'):
            value=copy.deepcopy(self.value)
            value['cases'][0]['variants']=[{'id':'core','requirement':'optional' if change=='optional-gate' else 'sometimes','evidence_class':'consumer','facilities':[]}]
            with self.subTest(change=change),self.assertRaises(ValueError):catalog.validate_catalog(self.root,value)

    def test_duplicate_variants_are_rejected(self):
        value=copy.deepcopy(self.value)
        value['cases'][0]['variants']=[{'id':'core','requirement':'required','evidence_class':'consumer','facilities':[]}]*2
        with self.assertRaises(ValueError):catalog.validate_catalog(self.root,value)


class CoveragePolicy(unittest.TestCase):
    def module(self):
        path=Path(__file__).parents[1]/'scripts/campaign.py'
        spec=importlib.util.spec_from_file_location('coverage_policy',path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

    def cases(self):
        return {'A-024':{'id':'A-024','variants':[
            {'id':'core','requirement':'required','evidence_class':'controlled','facilities':[]},
            {'id':'native','requirement':'optional','evidence_class':'native','facilities':['protected_handoff']}]}}

    def test_optional_missing_does_not_block_required_pass(self):
        result=self.module().coverage(self.cases(),{'A-024.core':{'status':'Passed','agent_behavior_assessed':True,'evidence_class':'controlled'}})
        self.assertTrue(result['required_ready']);self.assertEqual(result['required'],{'Passed':1})
        self.assertEqual(result['optional'],{'Not run':1});self.assertEqual(result['unexecuted'][0]['id'],'A-024.native')

    def test_optional_failed_visible_and_required_failed_blocks(self):
        results={'A-024.core':{'status':'Failed','agent_behavior_assessed':True},'A-024.native':{'status':'Failed','agent_behavior_assessed':True}}
        result=self.module().coverage(self.cases(),results);self.assertFalse(result['required_ready']);self.assertEqual(result['optional'],{'Failed':1})

    def test_deterministic_pass_is_not_independent_acceptance(self):
        result=self.module().coverage(self.cases(),{'A-024.core':{'status':'Passed','agent_behavior_assessed':False}})
        self.assertFalse(result['required_ready']);self.assertEqual(result['required'],{'Blocked':1})

    def test_old_assessment_remains_legacy_not_split_into_variant_passes(self):
        result=self.module().coverage(self.cases(),{'A-024':{'status':'Blocked'}})
        self.assertEqual(result['legacy'],{'A-024':{'status':'Blocked'}});self.assertEqual(result['required'],{'Blocked':1});self.assertEqual(result['optional'],{'Not run':1})

    def test_selection_rejects_unknown_variant_and_excludes_unselected_optional(self):
        module=self.module()
        with self.assertRaises(ValueError):module.coverage(self.cases(),{},selection={'A-024':['invented']})
        result=module.coverage(self.cases(),{},selection={'A-024':['core']});self.assertEqual(result['optional'],{})
