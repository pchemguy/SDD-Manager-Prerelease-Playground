/** Local campaign spacing checks using marked; no formatter or plugin dependency. */
import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
import {pathToFileURL} from 'node:url';
const {marked}=await import(pathToFileURL(path.join(process.env.CODEX_PRIMARY_RUNTIME_NODE_MODULES,'marked/lib/marked.esm.js')));
export function spacingIssues(src,base=0){
 const found=[];
 function boundary(start,end,kind){
  const before=src.slice(0,start),after=src.slice(end);
  if(start>0&&!/\n[ \t]*\n$/.test(before))found.push({position:base+start,insert:'\n',kind:kind+' before'});
  if(!/^\n[ \t]*\n/.test(after))found.push({position:base+end,insert:after.startsWith('\n')?'\n':'\n\n',kind:kind+' after'});
 }
 let prefix=0;
 if(src.startsWith('---\n')){const m=src.slice(4).match(/^---\s*\n/m);if(m)prefix=4+m.index+m[0].length;}
 let cursor=prefix;
 for(const t of marked.lexer(src.slice(prefix))){
  const pos=src.indexOf(t.raw,cursor);if(pos<0)continue;cursor=pos+t.raw.length;
  if(t.type==='list'||t.type==='code')boundary(pos,pos+t.raw.replace(/\n+$/,'').length,t.type==='list'?'top-level list':'code block');
 }
 const lines=src.split('\n');let offset=0,fence=null;
 for(const line of lines){
  const m=line.match(/^([ \t]*)(`{3,}|~{3,})(.*)$/);
  if(m){
   if(!fence)fence={char:m[2][0],length:m[2].length,start:offset,contentStart:offset+line.length+1,markdown:/^(markdown|md)\s*$/.test(m[3])};
   else if(m[2][0]===fence.char&&m[2].length>=fence.length&&!m[3].trim()){
    boundary(fence.start,offset+line.length,'fenced block');
    if(fence.markdown)found.push(...spacingIssues(src.slice(fence.contentStart,offset),base+fence.contentStart));
    fence=null;
   }
  }
  offset+=line.length+1;
 }
 const unique=new Map();for(const f of found)unique.set(f.position+':'+f.insert,f);return [...unique.values()];
}
