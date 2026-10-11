"""Actual controlled ledger effects and fault boundaries, never GitHub acceptance."""
import importlib.util
from pathlib import Path
import tempfile
import unittest


class FaultAdapter(unittest.TestCase):
    def module(self):
        p=Path(__file__).parents[1]/'scripts/fault_adapter.py';s=importlib.util.spec_from_file_location('fault_adapter',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

    def test_response_loss_applies_once_and_exact_readback_is_available(self):
        with tempfile.TemporaryDirectory() as root:
            m=self.module();result=m.operation(root,'task-one','write',{'state':'closed'},'after-send-loss')
            self.assertEqual(result['status'],'Uncertain');self.assertNotIn('object',result)
            read=m.operation(root,'task-one','read');self.assertEqual(read['object']['state'],'closed')
            self.assertEqual(m.operation(root,'task-one','write',{'state':'closed'})['status'],'Duplicate refused')

    def test_presend_fault_has_no_effect_and_can_be_boundedly_restored(self):
        with tempfile.TemporaryDirectory() as root:
            m=self.module();self.assertEqual(m.operation(root,'task-one','write',{'state':'closed'},'before-send-unavailable')['status'],'Unavailable')
            self.assertIsNone(m.operation(root,'task-one','read')['object']);self.assertEqual(m.operation(root,'task-one','write',{'state':'closed'})['status'],'Applied')

    def test_denial_rate_and_unavailable_access_are_distinct(self):
        with tempfile.TemporaryDirectory() as root:
            m=self.module();self.assertEqual(m.operation(root,'task-one','read',mode='denial')['http_status'],403)
            rate=m.operation(root,'task-one','read',mode='rate-limit');self.assertEqual(rate['http_status'],429);self.assertEqual(rate['retry_after'],1)
            self.assertIsNone(m.operation(root,'task-one','read',mode='unavailable-access')['http_status'])
            self.assertIsNone(m.operation(root,'task-one','read')['object'])

    def test_identity_escape_and_sensitive_payload_are_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            m=self.module()
            with self.assertRaises(ValueError):m.operation(root,'../outside','read')
            with self.assertRaises(Exception):m.operation(root,'task-one','write',{'token':'ghp_'+'SYNTHETIC_NOT_A_CREDENTIAL'})
