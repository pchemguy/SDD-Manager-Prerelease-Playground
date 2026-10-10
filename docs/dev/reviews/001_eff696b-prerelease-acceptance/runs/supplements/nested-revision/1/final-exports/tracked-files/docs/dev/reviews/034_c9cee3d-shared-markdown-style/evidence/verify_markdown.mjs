/** Campaign 034 verification: scoped style candidates, parser scenarios and Git preservation.
 * Run from repository root with the primary runtime Node and NODE_MODULES environment.
 * Uses preinstalled marked for local evidence, not a shipped plugin dependency.
 */
import fs from 'node:fs';
import {spacingIssues} from './verify_spacing.mjs';
import {markerIssues} from './verify_markers.mjs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {pathToFileURL} from 'node:url';
const {marked}=await import(pathToFileURL(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,'marked/lib/marked.esm.js')));
const baseline='c9cee3dc61ab3362b30d449d25852e8f35ee70b5';
const campaign='docs/dev/reviews/034_c9cee3d-shared-markdown-style';
const tracked=execFileSync('git',['ls-files','*.md'],{encoding:'utf8'}).trim().split('\n');
const roots=new Set(['AGENTS.md','README.md','SDD-MANAGER.md','AI_DISCLOSURE.md','Greenfield Project Prompt Template.md','docs/dev/CAPABILITY-MAP.md','docs/dev/reviews/README.md']);
const files=tracked.filter(f=>f.startsWith('skills/')||f.startsWith('assets/')||f.startsWith(campaign+'/')||roots.has(f));
function issues(src){
 const lines=src.split('\n'), out=[];let fence=null,front=false;
 for(let i=0;i<lines.length;i++){
  const line=lines[i];
  if(i===0&&line==='---'){front=true;continue;}
  if(front){if(line==='---')front=false;continue;}
  const m=line.match(/^\s*(`{3,}|~{3,})(.*)$/);
  if(m){
   if(!fence)fence={char:m[1][0],length:m[1].length,markdown:/^(markdown|md)\s*$/.test(m[2])};
   else if(m[1][0]===fence.char&&m[1].length>=fence.length&&!m[2].trim())fence=null;
   continue;
  }
  if(fence&&!fence.markdown)continue;
  if(/^\s*#{1,6}\s/.test(line)&& (i+1>=lines.length||lines[i+1].trim()))out.push([i+1,'heading blank line']);
  if (/^ {0,3}(?:=+|-+)\s*$/.test(line)&&i>0&&lines[i-1].trim()&&!/^(?:\s*[-+*]\s|\s*#{1,6}\s)/.test(lines[i-1])&&(i+1>=lines.length||lines[i+1].trim()))out.push([i+1,'Setext heading blank line']);
  const list=line.match(/^(\s*)(?:[-+*]|\d+[.)])\s/);
  if(list&&(list[1].includes('\t')||list[1].length%4))out.push([i+1,'list indentation']);
 }
 return out;
}
for(const f of files){const src=fs.readFileSync(f,'utf8');assert.deepEqual(issues(src),[],f);assert.deepEqual(spacingIssues(src),[],f);assert.deepEqual(markerIssues(src),[],f);}
const scenarios=[];
function check(id,fn){fn();scenarios.push({id,result:'passed',method:'local parser/source assertion'});}
check('SC-001',()=>{for(const body of ['prose','## Child\n\n','- item','| A |\n| --- |','```text\nx\n```']){assert.equal(issues('# Heading\n'+body).length,1);assert.deepEqual(issues('# Heading\n\n'+body),[]);assert.equal(marked.lexer('# Heading\n\n'+body)[0].type,'heading');}});
check('SC-002',()=>{assert.equal(issues('Title\n=====\nBody\n').length,1);assert.deepEqual(issues('Title\n=====\n\nBody\n'),[]);const t=marked.lexer('Title\n=====\n\nBody\n');assert.equal(t[0].type,'heading');assert.equal(t[0].depth,1);assert.equal(marked.lexer('---\n\nBody\n')[0].type,'hr');});
check('SC-003',()=>{let src='- Parent\n    - Child\n        - Grandchild\n';assert.deepEqual(issues(src),[]);let t=marked.lexer(src)[0];assert.equal(t.items[0].tokens[1].type,'list');assert.equal(t.items[0].tokens[1].items[0].tokens[1].type,'list');assert.equal(issues('- Parent\n  - Child\n').length,1);});
check('SC-004',()=>{for(const src of ['1. Parent\n    - Child\n','- Parent\n    1. Child\n','1000. Parent\n        - Child\n']){assert.deepEqual(issues(src),[]);assert.equal(marked.lexer(src)[0].items[0].tokens[1].type,'list');}});
check('SC-005',()=>{const src=fs.readFileSync('skills/sdd-tasks/references/task-derivation.md','utf8');const code=marked.lexer(src).find(t=>t.type==='code'&&t.lang==='markdown');assert(code);let phase=marked.lexer(code.text).find(t=>t.type==='list');assert(phase.items[0].task);let milestone=phase.items[0].tokens.find(t=>t.type==='list');assert(milestone.items[0].task);assert(milestone.items[0].tokens.find(t=>t.type==='list').items[0].task);const prior=marked.lexer(execFileSync('git',['show',`${baseline}:skills/sdd-tasks/references/task-derivation.md`],{encoding:'utf8'})).find(t=>t.type==='code'&&t.lang==='markdown');assert.equal(code.text.trim(),prior.text.trim());});
check('SC-006',()=>{const src='1. Prepare.\n    - Verify.\n\n    Keep checksum.\n\n    ```text\n    file.zip\n    ```\n2. Publish.\n';const t=marked.lexer(src);assert.equal(t.length,1);assert.equal(t[0].items.length,2);assert(t[0].items[0].tokens.some(t=>t.type==='paragraph'&&t.text.includes('checksum')));assert(t[0].items[0].tokens.some(t=>t.type==='code'&&t.text==='file.zip'));});
check('SC-007',()=>{assert.equal(issues('````markdown\n# Title\nBody\n````\n').length,1);assert.equal(issues('````markdown\n- Parent\n  - Child\n````\n').length,1);const src=fs.readFileSync('skills/sdd-conventions/references/markdown-style.md','utf8');const code=marked.lexer(src).find(t=>t.type==='code'&&t.lang==='markdown');assert(code);assert.deepEqual(issues(code.text+'\n'),[]);assert(marked.lexer(code.text).some(t=>t.type==='list'));});
function literalCodes(src){return marked.lexer(src).filter(t=>t.type==='code'&&!/^(md|markdown)$/.test(t.lang||'')).map(t=>({lang:t.lang,text:t.text}));}
check('SC-008',()=>{assert.deepEqual(issues('```python\n# comment\nif True:\n  print(1)\n```\n'),[]);for(const f of files){let old;try{old=execFileSync('git',['show',`${baseline}:${f}`],{encoding:'utf8',stdio:['ignore','pipe','ignore']});}catch{continue;}assert.deepEqual(literalCodes(fs.readFileSync(f,'utf8')),literalCodes(old),f);}});
check('SC-009',()=>{for(const f of files.filter(f=>f.endsWith('/SKILL.md')&&!f.includes('/sdd-conventions/'))){const src=fs.readFileSync(f,'utf8');assert(src.includes('[Markdown style](../sdd-conventions/references/markdown-style.md)'),f);}});
check('SC-010',()=>{const changed=execFileSync('git',['diff','--name-only',baseline],{encoding:'utf8'}).trim().split('\n');assert(!changed.some(f=>f.startsWith('docs/dev/reviews/')&&!f.startsWith(campaign+'/')&&f!=='docs/dev/reviews/README.md'));assert(!changed.some(f=>f.startsWith('docs/dev/features/')||f.startsWith('docs/dev/reports/')));});
check('SC-011',()=>{for(const marker of ['-','1.']){assert.deepEqual(spacingIssues(`Intro\n\n${marker} Item\n\n## After\n\nBody\n`),[]);assert(spacingIssues(`Intro\n${marker} Item\n## After\n\nBody\n`).some(x=>x.kind==='top-level list before'));assert(spacingIssues(`${marker} Item\n## After\n\nBody\n`).some(x=>x.kind==='top-level list after'));}});
check('SC-012',()=>{const src='- Parent\n    - Child\n        - Grandchild\n- Sibling\n\n';assert.deepEqual(spacingIssues(src),[]);assert.equal(marked.lexer(src)[0].items.length,2);});
check('SC-013',()=>{assert.deepEqual(spacingIssues('Intro\n\n```py\nx=1\n```\n\nAfter\n'),[]);assert(spacingIssues('Intro\n```py\nx=1\n```\nAfter\n').some(x=>x.kind==='fenced block before'));assert(spacingIssues('Intro\n```py\nx=1\n```\nAfter\n').some(x=>x.kind==='fenced block after'));assert.deepEqual(spacingIssues('Intro\n\n    x=1\n\nAfter\n'),[]);assert(marked.lexer('Intro\n\n    x=1\n\nAfter\n').some(t=>t.type==='code'));assert(spacingIssues('```text\nx\n```\n').length);assert.deepEqual(spacingIssues('```text\nx\n```\n\n'),[]);});
check('SC-014',()=>{const src='- Parent\n\n    ```python\n    if True:\n        print(1)\n    ```\n\n- Sibling\n\n';assert.deepEqual(spacingIssues(src),[]);const block=marked.lexer(src)[0].items[0].tokens.find(t=>t.type==='code');assert.equal(block.text,'if True:\n    print(1)');assert(spacingIssues('- Parent\n    ```python\n    x=1\n    ```\n- Sibling\n\n').length);});
check('SC-015',()=>{for(const marker of ['-','*','+','1.','1)','100.']){for(const content of ['item','[ ] task','[x] task']){for(const indent of ['', '    ']){const prefix=indent?'- Parent\n':'';assert.deepEqual(markerIssues(`${prefix}${indent}${marker} ${content}\n`),[]);assert(markerIssues(`${prefix}${indent}${marker}  ${content}\n`).length);assert(markerIssues(`${prefix}${indent}${marker}\t${content}\n`).length);}}}});
check('SC-016',()=>{for(const src of ['---\nx: 1\n---\n','*  *  *\n','    -  literal code\n','```python\n-  literal code\n```\n','````markdown\n```text\n-  literal code\n```\n````\n'])assert.deepEqual(markerIssues(src),[]);assert(markerIssues('````markdown\n-  template item\n````\n').length);assert.deepEqual(markerIssues('````markdown\n- template item\n````\n'),[]);});
let links=0;
for(const f of files){marked.walkTokens(marked.lexer(fs.readFileSync(f,'utf8')),token=>{if(token.type!=='link')return;const target=token.href.split('#')[0];if(!target||/^\w+:/.test(target)||target.includes('<'))return;assert(fs.existsSync(path.resolve(path.dirname(f),target)),`${f}: ${target}`);links++;});}
assert.equal(fs.readFileSync('plugin.json','utf8'),fs.readFileSync('.codex-plugin/plugin.json','utf8'));
assert.equal(JSON.parse(fs.readFileSync('plugin.json','utf8')).version,'0.15.0');
const result={checkedSource:execFileSync('git',['rev-parse','HEAD'],{encoding:'utf8'}).trim(),workingTreeChanges:execFileSync('git',['status','--porcelain'],{encoding:'utf8'}).trim().split('\n').filter(Boolean),markedVersion:JSON.parse(fs.readFileSync(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,'marked/package.json'),'utf8')).version,files:files.length,links,scenarios,limits:['Heading/list candidate scan plus representative parser assertions; not a complete general-purpose Markdown linter.','Source checks do not establish live agent behavior.','Closed records and verbatim transcripts excluded.']};
fs.writeFileSync(process.argv[2]||'/tmp/sdd034-check.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));
