/** Parse actual list markers and Markdown templates while excluding literal code/data. */
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const {marked}=await import(pathToFileURL(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,'marked/lib/marked.esm.js')));
export function markerIssues(src){
 const errors=[];
 const body=src.replace(/^---\n[\s\S]*?\n---(?:\n|$)/,'');
 marked.walkTokens(marked.lexer(body),token=>{
  if(token.type==='list')for(const item of token.items){
   const m=item.raw.split('\n')[0].match(/^\s*([-+*]|\d+[.)])([ \t]+)/);
   if(m&&m[2]!==' ')errors.push({kind:'list-marker separator',marker:m[1],separator:m[2]});
  }
  if(token.type==='code'&&/^(md|markdown)$/.test(token.lang||''))errors.push(...markerIssues(token.text));
 });
 return errors;
}
