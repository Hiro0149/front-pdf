// ================= デスク（フォルダの書類をサムネイルで並べる画面）
const DEV=/*__DEV__*/false;
const DK={on:false,root:null,cur:null,path:[],items:[],sel:new Set(),pos:{},hist:[],fut:[],clip:[],watcher:null,pollT:null,refreshT:null,openTok:0,thumbs:new Map(),busy:false,size:LS.get('deskSize',170)};
const DKLOG=[];
function dlog(s){const t=new Date().toTimeString().slice(0,8);DKLOG.push('['+t+'] '+s);if(DKLOG.length>800)DKLOG.shift();const el=$('#dkLog');if(el){el.textContent=DKLOG.join('\n');el.scrollTop=1e9;}}
function dmsg(s){$('#dkMsg').textContent=s;}
window.addEventListener('error',e=>dlog('エラー: '+e.message));
window.addEventListener('unhandledrejection',e=>dlog('エラー: '+((e.reason&&e.reason.message)||e.reason)));
const DKIND=n=>/\.pdf$/i.test(n)?'pdf':/\.(frontpdf|pdfkobo)$/i.test(n)?'fp':/\.(jpe?g|png)$/i.test(n)?'img':null;
const DEXT=n=>(n.match(/\.([^.]+)$/)||['',''])[1].toUpperCase();
const DSETTINGS='.frontpdf-desk';
const TRASH='_削除予定';

/* ---------- 保存場所（IndexedDB：フォルダの記憶と別ウインドウへの受け渡し） ---------- */
function dIdb(){return new Promise((ok,ng)=>{const r=indexedDB.open('frontpdf-desk',1);r.onupgradeneeded=()=>r.result.createObjectStore('kv');r.onsuccess=()=>ok(r.result);r.onerror=()=>ng(r.error);});}
async function dSet(k,v){const d=await dIdb();return new Promise((ok,ng)=>{const t=d.transaction('kv','readwrite');t.objectStore('kv').put(v,k);t.oncomplete=ok;t.onerror=()=>ng(t.error);});}
async function dGet(k){const d=await dIdb();return new Promise((ok,ng)=>{const t=d.transaction('kv');const r=t.objectStore('kv').get(k);r.onsuccess=()=>ok(r.result);r.onerror=()=>ng(r.error);});}
async function dDel(k){const d=await dIdb();return new Promise(ok=>{const t=d.transaction('kv','readwrite');t.objectStore('kv').delete(k);t.oncomplete=ok;t.onerror=ok;});}
async function dPerm(h,mode='readwrite'){if((await h.queryPermission({mode}))==='granted')return true;return (await h.requestPermission({mode}))==='granted';}

/* ---------- デスク専用の PDF ワーカー（エディターのものとは別にして、互いに影響しないようにする） ---------- */
let DKW=null;
function dWorker(){if(DKW)return DKW;try{DKW=new pdfjsLib.PDFWorker({port:new Worker(pdfjsLib.GlobalWorkerOptions.workerSrc)});}catch(e){DKW=null;}return DKW;}
function dDoc(bytes){const w=dWorker();return pdfjsLib.getDocument(w?{data:bytes,...PDFOPTS,worker:w}:{data:bytes,...PDFOPTS});}

/* ---------- 画面の切り替え ---------- */
function setView(v){DK.on=v==='desk';document.body.dataset.view=v;
  if(DK.on){$('#dkSkin').value=LS.get('skin',DEV?'gba':'modern');if(DK.cur)dScheduleRefresh('デスクに戻った');}
  else{setTimeout(()=>{try{if(ed.p)showPage(ed.p.uid,true);}catch(e){}},30);}}
$('#dkEdBig').onclick=$('#toEditor').onclick=()=>{const w=dEdWin('editor=1');if(!w)setView('editor');};
$('#toDesk').onclick=()=>{try{if(window.opener&&!window.opener.closed&&window.opener.DK){window.opener.focus();return;}}catch(e){}setView('desk');};
$('#dkSkin').onchange=()=>setSkin($('#dkSkin').value);

/* ---------- フォルダ ---------- */
async function dPickRoot(){
  if(!window.showDirectoryPicker){msg('デスク','このブラウザではフォルダを開けません。Microsoft Edge か Google Chrome をお使いください。');return;}
  try{const h=await window.showDirectoryPicker({mode:'readwrite',id:'fpdesk'});DK.root=h;await dSet('root',h);dlog('トップフォルダ: '+h.name);await dOpenRoot([]);
    if(!LS.get('deskTrashInfo',false)){LS.set('deskTrashInfo',true);msg('「'+TRASH+'」フォルダについて',tr('デスクで削除した書類や、上書きする前の版は、そのフォルダの中に作る「_削除予定」フォルダに移します（必要になったときに自動で作ります）。\nこれは Windows や Mac のごみ箱ではありません。中の書類はデスクの［元に戻す］で戻せます。\n不要になったら、左の一覧で「_削除予定」フォルダを右クリックし、［空にする］で完全に削除できます。'));}}
  catch(e){if(e.name!=='AbortError'){dlog('フォルダ選択失敗: '+e.name+' '+e.message);msg('フォルダを開けません',e.message);}}
}
async function dResume(h){
  try{if(!(await dPerm(h))){dmsg('フォルダへのアクセスが許可されませんでした');return;}
    DK.root=h;dlog('前回のフォルダを開いた: '+h.name);let last=[];try{last=LS.get('deskLast',[]);}catch(e){}
    await dOpenRoot(last[0]===h.name?last.slice(1):[]);}
  catch(e){dlog('前回のフォルダを開けない: '+e.message);dmsg('前回のフォルダを開けませんでした。もう一度選んでください');}
}
async function dOpenRoot(sub,expandLast){
  const tree=$('#dkTree');tree.innerHTML='';const n=await dTreeNode(DK.root,[DK.root.name],0);tree.appendChild(n);
  await n._open();let box=n;
  for(const nm of sub){const kids=box._kids;if(kids.style.display==='none')await box._toggle();const next=[...kids.children].find(w=>w._name===nm);if(!next)break;box=next;}
  if(expandLast&&box._kids.style.display==='none')await box._toggle();
  box._row.click();dStartWatch();
}
async function dTreeNode(dir,path,depth){
  const wrap=document.createElement('div');wrap._name=dir.name;
  const row=document.createElement('div');row.className='tn';row.style.paddingLeft=(6+depth*14)+'px';
  row.innerHTML='<span class="tw">▸</span><span class="fi"></span><span class="tnm"></span>';row.querySelector('.tnm').textContent=dir.name;row.title=path.join(' / ');
  const kids=document.createElement('div');kids.style.display='none';let loaded=false;
  const load=async()=>{if(loaded)return;loaded=true;const subs=[];
    try{for await(const [n,h] of dir.entries())if(h.kind==='directory'&&!n.startsWith('.'))subs.push(h);}catch(e){dlog('ツリー読み込み失敗: '+e.message);}
    subs.sort((a,b)=>a.name.localeCompare(b.name,'ja',{numeric:true}));for(const s of subs)kids.appendChild(await dTreeNode(s,[...path,s.name],depth+1));
    if(!subs.length)row.querySelector('.tw').textContent='';};
  const toggle=async()=>{await load();const open=kids.style.display==='none';kids.style.display=open?'':'none';const tw=row.querySelector('.tw');if(tw.textContent)tw.textContent=open?'▾':'▸';};
  wrap._toggle=toggle;wrap._open=async()=>{if(kids.style.display==='none')await toggle();};wrap._kids=kids;wrap._row=row;wrap._dir=dir;wrap._path=path;
  row.querySelector('.tw').onclick=async ev=>{ev.stopPropagation();await toggle();};
  row.onclick=()=>{document.querySelectorAll('#dkTree .tn.cur').forEach(x=>x.classList.remove('cur'));row.classList.add('cur');dOpenDir(dir,path);};
  row.ondragover=ev=>{if([...ev.dataTransfer.types].includes('Files')){ev.preventDefault();ev.stopPropagation();row.classList.add('drop');}};
  row.ondragleave=()=>row.classList.remove('drop');
  row.ondrop=async ev=>{ev.preventDefault();ev.stopPropagation();row.classList.remove('drop');const fs=[...ev.dataTransfer.files];if(fs.length)await dImport(fs,dir,path);};
  row._drop=async names=>dMoveTo(names,dir,path);
  wrap.append(row,kids);return wrap;
}
async function dOpenDir(dir,path,quiet){
  if(!dir)return;const same=DK.cur&&DK.path.join('/')===path.join('/');DK.cur=dir;DK.path=path;LS.set('deskLast',path);
  if(!same){DK.sel.clear();DK.pos={};DK.posLoaded=false;}
  const tok=++DK.openTok,got=[],t0=performance.now();
  try{for await(const [n,h] of dir.entries()){if(h.kind!=='file')continue;const k=DKIND(n);if(k)got.push({name:n,h,kind:k});}}
  catch(e){dlog('一覧の取得失敗: '+e.message);dmsg('フォルダを読めませんでした: '+e.message);return;}
  if(tok!==DK.openTok)return;
  got.sort((a,b)=>a.name.localeCompare(b.name,'ja',{numeric:true}));DK.items=got;
  if(!DK.posLoaded){await dLoadPos();DK.posLoaded=true;}
  $('#dkTitle').textContent=tr('Front PDF ― デスク')+' ― '+path.join(' / ');
  if(!quiet)dlog('フォルダ「'+path.join(' / ')+'」: '+got.length+' 件（'+Math.round(performance.now()-t0)+' ms）');
  if(!quiet)dmsg(path.join(' / '));dLayout();
}

/* ---------- 配置の保存（ブラウザ内 ＋ フォルダ内の設定ファイル .frontpdf-desk） ---------- */
const dPosKey=()=>'deskPos.'+DK.path.join('/');
async function dLoadPos(){
  let p=LS.get(dPosKey(),null);
  try{const fh=await DK.cur.getFileHandle(DSETTINGS);const j=JSON.parse(await (await fh.getFile()).text());if(j&&j.pos){p=j.pos;if(j.size)DK.size=j.size;}}catch(e){}
  DK.pos=p||{};
}
let dPosT=null;
function dSavePos(){LS.set(dPosKey(),DK.pos);clearTimeout(dPosT);const dir=DK.cur,pos=JSON.parse(JSON.stringify(DK.pos));
  dPosT=setTimeout(async()=>{try{DK.selfWrite=Date.now();const fh=await dir.getFileHandle(DSETTINGS,{create:true});const w=await fh.createWritable();
    await w.write(JSON.stringify({app:'Front PDF desk',ver:1,size:DK.size,pos},null,0));await w.close();}catch(e){dlog('配置ファイルの保存失敗: '+e.message);}},900);}

/* ---------- 並べる ---------- */
const dio=new IntersectionObserver(es=>{for(const e of es)if(e.isIntersecting){dio.unobserve(e.target);dThumb(e.target);}},{root:$('#dkArea'),rootMargin:'300px'});
function dDims(){const W=DK.size;return{W,H:Math.round(W*1.38)+20,G:18};}
function dLayout(){
  const desk=$('#dkDesk');desk.innerHTML='';$('#dkSize').value=DK.size;
  const q=$('#dkQ').value.trim().toLowerCase();const {W,H,G}=dDims();
  const cols=Math.max(1,Math.floor(($('#dkArea').clientWidth-G)/(W+G)));
  const taken=Object.values(DK.pos);const free=(x,y)=>!taken.some(p=>Math.abs(p.x-x)<W*.7&&Math.abs(p.y-y)<H*.7);
  let slot=0,maxY=0,shown=0;
  for(const it of DK.items){
    if(q&&!it.name.toLowerCase().includes(q))continue;shown++;
    let p=DK.pos[it.name];
    if(!p){do{p={x:G+(slot%cols)*(W+G),y:G+Math.floor(slot/cols)*(H+G)};slot++;}while(!free(p.x,p.y)&&slot<5000);taken.push(p);}
    const c=document.createElement('div');c.className='dcard k-'+it.kind+(DK.sel.has(it.name)?' sel':'');
    c.style.cssText='left:'+p.x+'px;top:'+p.y+'px;width:'+W+'px;height:'+H+'px';maxY=Math.max(maxY,p.y+H);
    c.innerHTML='<div class="th"><span class="ph">読み込み中…</span></div><div class="nm"></div><span class="ext"></span>';
    c.querySelector('.nm').textContent=it.name;c.querySelector('.nm').title=it.name;c.querySelector('.ext').textContent=DEXT(it.name);
    c._it=it;it.el=c;c.addEventListener('dragstart',e=>e.preventDefault());
    c.onmousedown=ev=>dStartDrag(ev,c);c.ondblclick=()=>dOpenItem(it);
    desk.appendChild(c);dio.observe(c);}
  desk.style.height=(maxY+40)+'px';
  $('#dkHello').style.display=DK.cur&&DK.items.length?'none':'flex';
  if(DK.cur&&!DK.items.length)$('#dkHello').innerHTML='<div>このフォルダには PDF・作業ファイル・画像がありません<br><small>エクスプローラーからドラッグ＆ドロップで取り込めます</small></div>';
  DK.shown=shown;DK.filt=!!q;dCountTxt();dActs();
}
async function dThumb(c){
  const it=c._it,th=c.querySelector('.th');
  try{const f=await it.h.getFile();const ck=it.name+'|'+f.size+'|'+f.lastModified;const hit=DK.thumbs.get(ck);
    const put=u=>{const img=new Image();img.src=u;th.innerHTML='';th.appendChild(img);};
    if(hit){put(hit);return;}
    if(it.kind==='img'){const u=URL.createObjectURL(f);DK.thumbs.set(ck,u);put(u);return;}
    let bytes=new Uint8Array(await f.arrayBuffer()),label='';
    if(it.kind==='fp'){const r=await dWorkFirst(bytes);if(!r){th.innerHTML='<span class="ph">作業ファイル</span>';return;}
      if(r.thumb){it.pages=r.pages;DK.thumbs.set(ck,r.thumb);put(r.thumb);c.querySelector('.nm').title=it.name+'\n'+r.pages+' ページ ／ '+Math.round(f.size/1024)+' KB ／ '+new Date(f.lastModified).toLocaleString();return;}
      bytes=r.bytes;it.fpIdx=r.idx;label=r.pages;}
    const task=dDoc(bytes);const doc=await task.promise;const pg=await doc.getPage((it.fpIdx||0)+1);
    const v0=pg.getViewport({scale:1});const sc=Math.min(2,(DK.size*1.6)/v0.width);const vp=pg.getViewport({scale:sc});
    const cv=document.createElement('canvas');cv.width=vp.width;cv.height=vp.height;await pg.render({canvasContext:cv.getContext('2d'),viewport:vp}).promise;
    it.pages=label||doc.numPages;await task.destroy();
    const u=cv.toDataURL('image/jpeg',.85);DK.thumbs.set(ck,u);put(u);
    c.querySelector('.nm').title=it.name+'\n'+it.pages+' ページ ／ '+Math.round(f.size/1024)+' KB ／ '+new Date(f.lastModified).toLocaleString();
  }catch(e){th.innerHTML='<span class="ph">表示できません</span>';dlog('サムネイル失敗 '+it.name+': '+e.message);}
}
async function dWorkFirst(raw){// 作業ファイルの1ページ目：保存時のサムネ画像があればそれ、無ければ元PDF（書き込みなし）
  try{if(new TextDecoder().decode(raw.subarray(0,8))!==KOBO_MAGIC)return null;let body=raw.subarray(9);
    if(String.fromCharCode(raw[8])==='Z')body=await streamConv(body,new DecompressionStream('gzip'));
    const d=JSON.parse(new TextDecoder().decode(body));const p=d.pages&&d.pages[0];if(!p)return null;const s=d.sources.find(x=>x.id===p.srcId);if(!s)return null;
    return{bytes:b64u8(s.b64),idx:p.idx,pages:d.pages.length,thumb:d.thumb||null};}catch(e){return null;}
}

/* ---------- 選択・ドラッグ ---------- */
function dSelItems(){return DK.items.filter(i=>DK.sel.has(i.name));}
function dRefreshSel(){document.querySelectorAll('.dcard').forEach(x=>x.classList.toggle('sel',DK.sel.has(x._it.name)));dCountTxt();dActs();}
function dCountTxt(){$('#dkCount').textContent=(DK.shown||0)+' 件'+(DK.filt?'（絞り込み中）':'')+' ／ 選択 '+DK.sel.size;}
function dActs(){const n=DK.sel.size;$('#dkPrint').disabled=!n;$('#dkOpen').disabled=n!==1;$('#dkWin').disabled=n!==1;$('#dkPrevB').disabled=!n;$('#dkRen').disabled=n!==1;$('#dkTrash').disabled=!n;
  $('#dkUndo').disabled=!DK.hist.length;$('#dkRedo').disabled=!DK.fut.length;}
function dStartDrag(ev,c){
  if(ev.button!==0)return;const it=c._it;
  if(ev.ctrlKey||ev.shiftKey){DK.sel.has(it.name)?DK.sel.delete(it.name):DK.sel.add(it.name);}else if(!DK.sel.has(it.name)){DK.sel.clear();DK.sel.add(it.name);}
  dRefreshSel();
  const sx=ev.clientX,sy=ev.clientY,starts=[...document.querySelectorAll('.dcard.sel')].map(x=>({x,l:x.offsetLeft,t:x.offsetTop}));
  const gh=c.cloneNode(true);gh.classList.add('dghost');gh.style.left=gh.style.top='0';gh.style.width=c.offsetWidth*.6+'px';gh.style.height=c.offsetHeight*.6+'px';
  if(starts.length>1){const b=document.createElement('span');b.className='cnt';b.textContent=starts.length+' 件';gh.appendChild(b);}
  document.body.appendChild(gh);const wr=$('#dkArea').getBoundingClientRect();let moved=false,over=null,target=null;
  for(const s of starts)s.x.classList.add('dragging');
  const mv=e=>{const dx=e.clientX-sx,dy=e.clientY-sy;if(Math.abs(dx)+Math.abs(dy)>3)moved=true;if(!moved)return;
    const out=e.clientX<wr.left;gh.style.display=out?'block':'none';gh.style.left=(e.clientX+8)+'px';gh.style.top=(e.clientY+8)+'px';
    for(const s of starts){s.x.style.opacity=out?'.35':'';s.x.style.left=Math.max(0,s.l+dx)+'px';s.x.style.top=Math.max(0,s.t+dy)+'px';}
    const el=document.elementFromPoint(e.clientX,e.clientY);const tn=el&&el.closest&&el.closest('#dkTree .tn');
    document.querySelectorAll('#dkTree .tn.drop').forEach(x=>x!==tn&&x.classList.remove('drop'));if(tn)tn.classList.add('drop');over=tn;
    let tc=null;if(!tn){for(const x of document.elementsFromPoint(e.clientX,e.clientY)){const cc=x.closest&&x.closest('.dcard');if(cc&&!cc.classList.contains('sel')&&!cc.classList.contains('dghost')){tc=cc;break;}}}
    document.querySelectorAll('.dcard.mtarget').forEach(x=>x!==tc&&x.classList.remove('mtarget'));if(tc)tc.classList.add('mtarget');target=tc;for(const s of starts)s.x.classList.toggle('over',!!tc);};
  const up=async()=>{document.removeEventListener('mousemove',mv);document.removeEventListener('mouseup',up);gh.remove();document.querySelectorAll('#dkTree .tn.drop').forEach(x=>x.classList.remove('drop'));
    for(const s of starts){s.x.style.opacity='';s.x.classList.remove('dragging','over');}
    document.querySelectorAll('.dcard.mtarget').forEach(x=>x.classList.remove('mtarget'));
    if(over&&moved){for(const s of starts){s.x.style.left=s.l+'px';s.x.style.top=s.t+'px';}await over._drop([...DK.sel]);return;}
    if(target&&moved){for(const s of starts){s.x.style.left=s.l+'px';s.x.style.top=s.t+'px';}dMergeAsk([...dSelItems(),target._it]);return;}
    if(moved){for(const s of starts)DK.pos[s.x._it.name]={x:s.x.offsetLeft,y:s.x.offsetTop};dSavePos();}};
  document.addEventListener('mousemove',mv);document.addEventListener('mouseup',up);
}
$('#dkDesk').addEventListener('mousedown',e=>{if(e.target.id==='dkDesk'){DK.sel.clear();dRefreshSel();}});

/* ---------- ファイル操作（すべて Ctrl+Z で戻せるように記録する） ---------- */
async function dExists(dir,name){try{await dir.getFileHandle(name);return true;}catch(e){return false;}}
async function dWrite(dir,name,blob){const fh=await dir.getFileHandle(name,{create:true});const w=await fh.createWritable();await w.write(blob);await w.close();return fh;}
function dSplit(n){const m=n.match(/^(.*?)(\.[^.]+)?$/);return[m[1],m[2]||''];}
async function dFreeName(dir,name,suf){const[b,e]=dSplit(name);let nn=suf?b+suf+e:name,k=2;while(await dExists(dir,nn))nn=b+(suf||'')+' ('+(k++)+')'+e;return nn;}
// エディターのウインドウで行った保存を、デスクの［元に戻す］の履歴に渡す（IndexedDB 経由）
async function dDeskOp(op){if(!new URLSearchParams(location.search).get('open')&&!new URLSearchParams(location.search).get('editor')){dPush(op);return;}
  try{const q=(await dGet('pendingOps'))||[];q.push(op);await dSet('pendingOps',q);}catch(e){dlog('履歴の受け渡し失敗: '+e.message);}}
async function dPullOps(){try{const q=await dGet('pendingOps');if(q&&q.length){await dSet('pendingOps',[]);for(const op of q)dPush(op);dlog('エディターでの保存 '+q.length+' 件を［元に戻す］の履歴に追加');}}catch(e){}}
function dPush(op){DK.hist.push(op);if(DK.hist.length>200)DK.hist.shift();DK.fut=[];dActs();}
async function dRun(op,dir){// dir: 'undo' | 'redo'
  const u=dir==='undo';
  switch(op.t){
    case'rename':await op.h.move(u?op.from:op.to);break;
    case'move':await op.h.move(u?op.fromDir:op.toDir,op.name);break;
    case'trash':if(u)await op.h.move(op.fromDir,op.name);else{const tr=await op.fromDir.getDirectoryHandle(TRASH,{create:true});await op.h.move(tr,op.trName);}break;
    case'create':if(u){op.blob=op.blob||await (await (await op.dir.getFileHandle(op.name)).getFile());await op.dir.removeEntry(op.name);}else await dWrite(op.dir,op.name,op.blob);break;
    case'mkdir':if(u)await op.dir.removeEntry(op.name);else await op.dir.getDirectoryHandle(op.name,{create:true});DK.treeDirty=true;break;
    case'group':{const ops=u?[...op.ops].reverse():op.ops;for(const o of ops)await dRun(o,dir);break;}
    case'overwrite':{const cur=await (await (await op.dir.getFileHandle(op.name)).getFile()).arrayBuffer();const back=await (await (await op.bdir.getFileHandle(op.bname)).getFile()).arrayBuffer();
      await dWrite(op.dir,op.name,new Blob([back]));await dWrite(op.bdir,op.bname,new Blob([cur]));break;}
  }
}
async function dUndoRedo(dir){
  await dPullOps();
  const from=dir==='undo'?DK.hist:DK.fut,to=dir==='undo'?DK.fut:DK.hist;const op=from.pop();if(!op){dmsg(dir==='undo'?'これ以上元に戻せません':'やり直す操作がありません');return;}
  try{await dRun(op,dir);to.push(op);dmsg((dir==='undo'?'元に戻しました：':'やり直しました：')+op.label);dlog((dir==='undo'?'元に戻す: ':'やり直し: ')+op.label);}
  catch(e){dmsg('戻せませんでした（ファイルが移動・変更されている可能性）：'+op.label);dlog('戻す失敗 '+op.label+': '+e.name+' '+e.message);}
  dActs();if(DK.treeDirty)await dRebuildTree();else await dOpenDir(DK.cur,DK.path,true);
}
async function dRename(){
  const it=dSelItems()[0];if(!it)return;const nn=(prompt(tr('新しい名前'),it.name)||'').trim();if(!nn||nn===it.name)return;
  if(/[\\/:*?"<>|]/.test(nn)){msg('名前変更','次の文字は使えません： \\ / : * ? " < > |');return;}
  if(await dExists(DK.cur,nn)){msg('名前変更','同じ名前のファイルがあります。');return;}
  try{await it.h.move(nn);if(DK.pos[it.name]){DK.pos[nn]=DK.pos[it.name];delete DK.pos[it.name];dSavePos();}
    DK.sel.clear();DK.sel.add(nn);dPush({t:'rename',h:it.h,from:it.name,to:nn,label:'名前変更 '+it.name+' → '+nn});dlog('名前変更: '+it.name+' → '+nn);await dOpenDir(DK.cur,DK.path,true);}
  catch(e){msg('名前変更できません',e.message);dlog('名前変更失敗: '+e.name+' '+e.message);}
}
async function dMoveTo(names,dir,path){
  if(!names.length||path.join('/')===DK.path.join('/'))return;let n=0;
  for(const name of names){const it=DK.items.find(i=>i.name===name);if(!it)continue;
    if(await dExists(dir,name)){dlog('移動先に同じ名前があるので移動しません: '+name);dmsg('移動先に同じ名前の「'+name+'」があります');continue;}
    try{await it.h.move(dir,name);n++;delete DK.pos[name];dPush({t:'move',h:it.h,fromDir:DK.cur,toDir:dir,name,label:'移動 '+name+' → '+path.join(' / ')});dlog('移動: '+name+' → '+path.join(' / '));}
    catch(e){dlog('移動失敗: '+e.name+' '+e.message);msg('移動できません',name+'\n'+e.message);}}
  if(n){dSavePos();dmsg(n+' 件を「'+path[path.length-1]+'」へ移動しました（Ctrl+Z で戻せます）');}
  DK.sel.clear();await dOpenDir(DK.cur,DK.path,true);
}
async function dTrash(){
  const its=dSelItems();if(!its.length)return;
  if(DK.path[DK.path.length-1]===TRASH){msg(TRASH,'このフォルダの中身は、左の一覧でこのフォルダを右クリックして［空にする］で削除してください。');return;}
  try{const tr=await DK.cur.getDirectoryHandle(TRASH,{create:true});
    for(const it of its){const tn=await dFreeName(tr,it.name);await it.h.move(tr,tn);delete DK.pos[it.name];dPush({t:'trash',h:it.h,fromDir:DK.cur,name:it.name,trName:tn,label:'_削除予定へ '+it.name});dlog('_削除予定へ: '+it.name);}
    dSavePos();dmsg(its.length+' 件を「_削除予定」へ移しました（Ctrl+Z で戻せます）');DK.sel.clear();await dOpenDir(DK.cur,DK.path,true);}
  catch(e){msg('_削除予定へ移せません',e.message);dlog('_削除予定失敗: '+e.message);}
}
async function dPaste(){
  if(!DK.clip.length||!DK.cur)return;let n=0;DK.sel.clear();
  for(const c of DK.clip){try{const f=await c.h.getFile();const nn=await dFreeName(DK.cur,c.name,DK.path.join('/')===c.from?' - コピー':'');await dWrite(DK.cur,nn,f);n++;DK.sel.add(nn);
      dPush({t:'create',dir:DK.cur,name:nn,label:'複製 '+nn});dlog('貼り付け: '+nn);}catch(e){dlog('貼り付け失敗: '+e.message);msg('貼り付けできません',c.name+'\n'+e.message);}}
  if(n)dmsg(n+' 件を貼り付けました（Ctrl+Z で戻せます）');await dOpenDir(DK.cur,DK.path,true);
}
async function dImport(files,dir,path){
  let n=0;for(const f of files){if(!DKIND(f.name)){dmsg('PDF・作業ファイル・JPG・PNG 以外は取り込めません：'+f.name);continue;}
    try{const nn=await dFreeName(dir,f.name);await dWrite(dir,nn,f);n++;dPush({t:'create',dir,name:nn,label:'取り込み '+nn});dlog('取り込み（コピー）: '+nn+' → '+path.join(' / '));}
    catch(e){dlog('取り込み失敗: '+e.message);msg('取り込めません',f.name+'\n'+e.message);}}
  if(n)dmsg(n+' 件を「'+path[path.length-1]+'」に取り込みました（コピー）');if(DK.cur)await dOpenDir(DK.cur,DK.path,true);
}

/* ---------- 結合（サムネイルを重ねる） ---------- */
let MG=[];
function dMergeAsk(list){
  MG=list;const hasFp=list.some(i=>i.kind==='fp');$('#mgExt').textContent=hasFp?'.frontpdf':'.pdf';$('#mgFpNote').style.display=hasFp?'block':'none';dMergeList();const[b]=dSplit(list[0].name);$('#mgName').value=b.replace(/_作業ファイル$/,'')+'_結合';$('#mgTrash').checked=false;
  $('#mgImgNote').style.display=list.some(i=>i.kind==='img')?'block':'none';openDlg('#dkMergeDlg');setTimeout(()=>$('#mgName').select(),30);}
function dMergeList(){const box=$('#mgList');box.innerHTML='';MG.forEach((it,i)=>{const r=document.createElement('div');r.className='mi';
  r.innerHTML='<b>'+(i+1)+'</b><span class="tag" style="background:'+(it.kind==='img'?'#2f8a4a':it.kind==='fp'?'#2f5fc8':'#c8382c')+'">'+DEXT(it.name)+'</span><span class="n"></span><button title="上へ">↑</button><button title="下へ">↓</button>';
  r.querySelector('.n').textContent=it.name;const[u,dn]=r.querySelectorAll('button');u.disabled=!i;dn.disabled=i===MG.length-1;
  u.onclick=()=>{[MG[i-1],MG[i]]=[MG[i],MG[i-1]];dMergeList();};dn.onclick=()=>{[MG[i+1],MG[i]]=[MG[i],MG[i+1]];dMergeList();};box.appendChild(r);});}
$('#mgGo').onclick=async()=>{
  const hasFp=MG.some(i=>i.kind==='fp'),ext=hasFp?'.frontpdf':'.pdf';
  const base=($('#mgName').value.trim()||'結合').replace(/[\\/:*?"<>|]/g,'_').replace(/\.(pdf|frontpdf)$/i,'');let name=base+ext;const trash=$('#mgTrash').checked;closeDlg($('#mgGo'));
  if(await dExists(DK.cur,name)){if(!confirm(tr('「'+name+'」がすでにあります。別の名前（番号付き）で保存します。')))return;name=await dFreeName(DK.cur,name);}
  try{busy('結合しています...',0.05);
    if(hasFp){const data=await dMergeWork(MG);await dWrite(DK.cur,name,new Blob([data],{type:'application/octet-stream'}));}
    else{const out=await PDFDocument.create();
    for(let i=0;i<MG.length;i++){const it=MG[i];busy('結合しています... '+(i+1)+' / '+MG.length,0.05+0.8*i/MG.length);
      let bytes=new Uint8Array(await (await it.h.getFile()).arrayBuffer());if(it.kind==='img')bytes=await imageToPdf(bytes,/\.png$/i.test(it.name));
      const src=await PDFDocument.load(bytes,{ignoreEncryption:true});const ps=await out.copyPages(src,src.getPageIndices());ps.forEach(p=>out.addPage(p));}
    const data=await out.save();await dWrite(DK.cur,name,new Blob([data],{type:'application/pdf'}));}
    const ops=[{t:'create',dir:DK.cur,name}];
    if(trash){const tr_=await DK.cur.getDirectoryHandle(TRASH,{create:true});for(const it of MG){const tn=await dFreeName(tr_,it.name);await it.h.move(tr_,tn);delete DK.pos[it.name];ops.push({t:'trash',h:it.h,fromDir:DK.cur,name:it.name,trName:tn});}}
    const p0=DK.pos[MG[0].name];if(p0&&!trash)DK.pos[name]={x:p0.x+24,y:p0.y+24};else if(p0)DK.pos[name]=p0;dSavePos();
    dPush({t:'group',ops,label:'結合 '+name});busy(false);DK.sel.clear();DK.sel.add(name);
    dlog('結合: '+MG.map(i=>i.name).join(' + ')+' → '+name+(trash?'（元は _削除予定へ）':''));dmsg('「'+name+'」を作りました（Ctrl+Z で結合前に戻せます）');await dOpenDir(DK.cur,DK.path,true);}
  catch(e){busy(false);msg('結合できません',(e.message||e)+(/encrypt|password/i.test(String(e))?'\n（パスワード付きのPDFは結合できません）':''));dlog('結合失敗: '+e.message);}
};

async function dReadWork(raw){if(new TextDecoder().decode(raw.subarray(0,8))!==KOBO_MAGIC)throw new Error('作業ファイルを読めません');let body=raw.subarray(9);
  if(String.fromCharCode(raw[8])==='Z')body=await streamConv(body,new DecompressionStream('gzip'));return JSON.parse(new TextDecoder().decode(body));}
async function dMergeWork(list){// 作業ファイル（＋PDF・画像）を1つの作業ファイルにまとめる。書き込み・付箋はそのまま
  const out={app:'Front PDF',ver:1,saved:new Date().toISOString(),cur:null,wm:null,sources:[],pages:[],images:{},thumb:null};let next=1;
  for(let k=0;k<list.length;k++){const it=list[k];busy('結合しています... '+(k+1)+' / '+list.length,0.05+0.8*k/list.length);
    const raw=new Uint8Array(await (await it.h.getFile()).arrayBuffer());
    if(it.kind==='fp'){const d=await dReadWork(raw);let mx=0;const js=JSON.stringify(d);for(const m of js.matchAll(/"u(\d+)"/g))mx=Math.max(mx,+m[1]);const off=next;next+=mx+1;
      const map=v=>{if(typeof v!=='string')return v;const m=/^u(\d+)$/.exec(v);return m?'u'+(+m[1]+off):v+'_m'+k;};
      const walk=o=>{if(Array.isArray(o)){o.forEach(walk);return;}if(o&&typeof o==='object')for(const key of Object.keys(o)){if(['id','uid','srcId','imgId'].includes(key))o[key]=map(o[key]);else walk(o[key]);}};
      for(const s of d.sources){out.sources.push({id:map(s.id),name:s.name,b64:s.b64});}
      walk(d.pages);out.pages.push(...d.pages);for(const[id,url]of Object.entries(d.images||{}))out.images[map(id)]=url;
      if(!out.wm||(!out.wm.on&&d.wm&&d.wm.on))out.wm=d.wm||out.wm;if(k===0)out.thumb=d.thumb||null;}
    else{let bytes=raw;if(it.kind==='img')bytes=await imageToPdf(bytes,/\.png$/i.test(it.name));
      const sid='u'+(next++);out.sources.push({id:sid,name:it.name,b64:u8b64(bytes)});
      const task=dDoc(bytes.slice());const doc=await task.promise;
      for(let i=0;i<doc.numPages;i++){const pg=await doc.getPage(i+1);const vp=pg.getViewport({scale:1,rotation:0});out.pages.push({uid:'u'+(next++),srcId:sid,idx:i,baseRot:pg.rotate||0,rot:0,w:vp.width,h:vp.height,objects:[]});}
      await task.destroy();}}
  if(!out.wm)out.wm={on:false,text:'COPY',size:110,angle:35,color:'#ff0000',opacity:14};out.cur=out.pages[0]?.uid||null;
  let body=new TextEncoder().encode(JSON.stringify(out)),flag='J';
  if(window.CompressionStream){try{body=await streamConv(body,new CompressionStream('gzip'));flag='Z';}catch(e){}}
  const head=new TextEncoder().encode(KOBO_MAGIC+flag);const r=new Uint8Array(head.length+body.length);r.set(head);r.set(body,head.length);return r;}

async function dEmptyTrash(dir,path){
  const names=[];try{for await(const [n] of dir.entries())names.push(n);}catch(e){msg('フォルダを開けません',e.message);return;}
  if(!names.length){msg('空にする','「'+TRASH+'」フォルダは空です。');return;}
  if(!confirm(tr('「'+path.join(' / ')+'」の中の '+names.length+' 件を完全に削除します。\nWindows や Mac のごみ箱には入らず、元に戻せません。\n（デスクの［元に戻す］の履歴もリセットされます）')))return;
  let n=0,fail=0;busy('削除しています...',0.05);
  for(let i=0;i<names.length;i++){try{await dir.removeEntry(names[i],{recursive:true});n++;}catch(e){fail++;dlog('削除失敗 '+names[i]+': '+e.message);}busy('削除しています...',0.05+0.9*(i+1)/names.length);}
  busy(false);DK.hist=[];DK.fut=[];dActs();dlog('空にした: '+path.join('/')+' '+n+' 件'+(fail?'（失敗 '+fail+'）':''));
  dmsg(fail?n+' 件を完全に削除しました（'+fail+' 件は削除できませんでした）':n+' 件を完全に削除しました');
  if(DK.cur&&await DK.cur.isSameEntry(dir))await dOpenDir(DK.cur,DK.path,true);}

/* ---------- ページごとにばらす ---------- */
let SP=[];
async function dSplitAsk(list){
  list=list.filter(i=>i.kind==='pdf');if(!list.length){msg('ページごとにばらす','PDF を選んでください（作業ファイル・画像はばらせません）。');return;}
  let total=0;for(const it of list){if(!it.pages){try{const t=dDoc(new Uint8Array(await (await it.h.getFile()).arrayBuffer()));const doc=await t.promise;it.pages=doc.numPages;await t.destroy();}catch(e){it.pages=0;}}total+=+it.pages||0;}
  SP=list;const[b]=dSplit(list[0].name);$('#spFolder').textContent='「'+(list.length>1?tr('ページ別'):b+tr('_ページ別'))+'」';
  $('#spInfo').innerHTML='';$('#spInfo').textContent=(list.length>1?list.length+' 個の PDF':'「'+list[0].name+'」')+'を、1ページずつ別の PDF（合計 '+total+' 個）に分けます。名前は「元の名前_p01.pdf」のようになります。';
  $('#spTrash').checked=false;openDlg('#dkSplitDlg');}
$('#spGo').onclick=async()=>{
  const toFolder=document.querySelector('input[name=spWhere]:checked').value==='folder',trash=$('#spTrash').checked;closeDlg($('#spGo'));
  const ops=[];let out=DK.cur,made=0;
  try{busy('ページごとに分けています...',0.03);
    if(toFolder){const fn0=$('#spFolder').textContent.replace(/^「|」$/g,'');let fn=fn0,k=2;const has=async n=>{try{await DK.cur.getDirectoryHandle(n);return true;}catch(e){return false;}};while(await has(fn))fn=fn0+' ('+(k++)+')';
      out=await DK.cur.getDirectoryHandle(fn,{create:true});ops.push({t:'mkdir',dir:DK.cur,name:fn});DK.treeDirty=true;}
    for(const it of SP){const src=await PDFDocument.load(new Uint8Array(await (await it.h.getFile()).arrayBuffer()),{ignoreEncryption:true});const n=src.getPageCount(),w=Math.max(2,String(n).length);const[b]=dSplit(it.name);
      for(let i=0;i<n;i++){busy('分けています... '+it.name+' '+(i+1)+' / '+n,0.05+0.9*(i/n));const one=await PDFDocument.create();const[p]=await one.copyPages(src,[i]);one.addPage(p);
        const nn=await dFreeName(out,b+'_p'+String(i+1).padStart(w,'0')+'.pdf');await dWrite(out,nn,new Blob([await one.save()],{type:'application/pdf'}));ops.push({t:'create',dir:out,name:nn});made++;}}
    if(trash){const tr_=await DK.cur.getDirectoryHandle(TRASH,{create:true});for(const it of SP){const tn=await dFreeName(tr_,it.name);await it.h.move(tr_,tn);delete DK.pos[it.name];ops.push({t:'trash',h:it.h,fromDir:DK.cur,name:it.name,trName:tn});}dSavePos();}
    dPush({t:'group',ops,label:'ばらす '+SP.map(i=>i.name).join('、')});busy(false);
    dlog('ばらす: '+SP.map(i=>i.name).join(' + ')+' → '+made+' 個'+(toFolder?'（フォルダ '+ops[0].name+'）':''));
    dmsg(made+' 個の PDF に分けました'+(toFolder?'（フォルダ「'+ops[0].name+'」）':'')+'。Ctrl+Z で元に戻せます');
    if(DK.treeDirty)await dRebuildTree();else await dOpenDir(DK.cur,DK.path,true);}
  catch(e){busy(false);msg('ばらせません',(e.message||e)+(/encrypt|password/i.test(String(e))?'\n（パスワード付きのPDFはばらせません）':''));dlog('ばらす失敗: '+e.message);if(ops.length)dPush({t:'group',ops,label:'ばらす（途中まで）'});}
};
async function dRebuildTree(){DK.treeDirty=false;const keep=DK.path.slice(1),m=$('#dkMsg').textContent;await dOpenRoot(keep,true);await new Promise(r=>setTimeout(r,60));$('#dkMsg').textContent=m;}
async function dNewFolder(){
  if(!DK.cur)return;let nm=(prompt(tr('新しいフォルダの名前'),tr('新しいフォルダ'))||'').trim();if(!nm)return;
  if(/[\\/:*?"<>|]/.test(nm)){msg('新しいフォルダ','次の文字は使えません： \\ / : * ? " < > |');return;}
  try{try{await DK.cur.getDirectoryHandle(nm);msg('新しいフォルダ','同じ名前のフォルダがあります。');return;}catch(e){}
    await DK.cur.getDirectoryHandle(nm,{create:true});dPush({t:'mkdir',dir:DK.cur,name:nm,label:'新しいフォルダ '+nm});dlog('新しいフォルダ: '+nm);dmsg('フォルダ「'+nm+'」を作りました');await dRebuildTree();}
  catch(e){msg('フォルダを作れません',e.message);}
}

/* ---------- 印刷 ---------- */
async function dPrint(list){
  list=(list||dSelItems());const ok=list.filter(i=>i.kind!=='fp');
  if(!ok.length){msg('印刷','印刷する PDF・画像を選んでください（作業ファイルはエディターで開いて印刷してください）。');return;}
  try{busy('印刷の準備中...',0.02);const src=[];for(const it of ok){const f=await it.h.getFile();src.push(it.kind==='img'?{blob:f}:{bytes:new Uint8Array(await f.arrayBuffer())});}
    dlog('印刷: '+ok.map(i=>i.name).join('、'));await printDocs(src);}
  catch(e){busy(false);msg('印刷できません',e.message||String(e));}
}
$('#dkPrint').onclick=()=>dPrint();

/* ---------- 右クリックメニュー ---------- */
function dMenu(x,y,items){
  const m=$('#dkMenu');m.innerHTML='';
  for(const it of items){if(it==='-'){const s=document.createElement('div');s.className='ms';m.appendChild(s);continue;}
    const r=document.createElement('div');r.className='mi'+(it.off?' off':'');r.innerHTML='<span></span><span class="k"></span>';r.children[0].textContent=it.t;r.children[1].textContent=it.k||'';
    r.onclick=()=>{dMenuClose();it.f();};m.appendChild(r);}
  m.classList.add('show');const w=m.offsetWidth,h=m.offsetHeight;m.style.left=Math.min(x,innerWidth-w-6)+'px';m.style.top=Math.min(y,innerHeight-h-6)+'px';
}
function dMenuClose(){$('#dkMenu').classList.remove('show');}
document.addEventListener('mousedown',e=>{if(!e.target.closest||!e.target.closest('#dkMenu'))dMenuClose();},true);
window.addEventListener('blur',dMenuClose);
$('#deskWin').addEventListener('contextmenu',e=>{
  if(isTyping(e.target))return;// 入力欄だけは普段のメニュー（貼り付けなど）を使えるようにする
  e.preventDefault();
  const tn=e.target.closest('#dkTree .tn');
  if(tn){const w=tn.parentElement;tn.click();
    const isTr=w._path&&w._path[w._path.length-1]===TRASH;
    dMenu(e.clientX,e.clientY,[{t:'このフォルダを開く',f:()=>{}},{t:'ここに貼り付け',k:'Ctrl+V',f:dPaste,off:!DK.clip.length||isTr},{t:'この中に新しいフォルダ',f:dNewFolder,off:isTr},'-',...(isTr?[{t:'空にする（完全に削除）',f:()=>dEmptyTrash(w._dir,w._path)},'-']:[]),{t:'更新',f:()=>dRebuildTree()}]);return;}
  if(!e.target.closest('#dkArea'))return;
  if(!DK.cur){dMenu(e.clientX,e.clientY,[{t:'フォルダを選ぶ',f:dPickRoot}]);return;}
  const c=e.target.closest('.dcard');
  if(c){if(!DK.sel.has(c._it.name)){DK.sel.clear();DK.sel.add(c._it.name);dRefreshSel();}
    const its=dSelItems(),n=its.length,pdfs=its.filter(i=>i.kind==='pdf').length,one=n===1;
    dMenu(e.clientX,e.clientY,[
      {t:'開く',k:'Enter',f:()=>dOpenItem(its[0]),off:!one},
      {t:'プレビュー',k:'Space',f:()=>dPreview(its[0])},
      {t:n>1?'選んだ '+n+' 件を印刷':'印刷',k:'Ctrl+P',f:()=>dPrint(its)},
      '-',
      {t:'名前の変更',k:'F2',f:dRename,off:!one},
      {t:'コピー',k:'Ctrl+C',f:()=>dCopySel()},
      {t:'貼り付け',k:'Ctrl+V',f:dPaste,off:!DK.clip.length},
      {t:'複製（このフォルダに）',f:async()=>{dCopySel();await dPaste();}},
      '-',
      {t:n>1?'選んだ '+n+' 件を結合':'結合（2件以上を選んでください）',f:()=>dMergeAsk([...its].sort((a,b)=>a.name.localeCompare(b.name,'ja',{numeric:true}))),off:n<2},
      {t:'ページごとにばらす',f:()=>dSplitAsk(its),off:!pdfs},
      '-',
      {t:'_削除予定へ',k:'Delete',f:dTrash}]);}
  else{DK.sel.clear();dRefreshSel();
    dMenu(e.clientX,e.clientY,[
      {t:'貼り付け',k:'Ctrl+V',f:dPaste,off:!DK.clip.length},
      {t:'新しいフォルダ',f:dNewFolder},
      '-',
      {t:'すべて選択',k:'Ctrl+A',f:()=>{DK.items.forEach(i=>DK.sel.add(i.name));dRefreshSel();}},
      {t:'名前順に整列',f:()=>$('#dkAlign').click()},
      ...(DK.path[DK.path.length-1]===TRASH?['-',{t:'空にする（完全に削除）',f:()=>dEmptyTrash(DK.cur,DK.path)}]:[]),
      {t:'更新',f:()=>dOpenDir(DK.cur,DK.path)},
      '-',
      {t:'元に戻す',k:'Ctrl+Z',f:()=>dUndoRedo('undo'),off:!DK.hist.length},
      {t:'やり直し',k:'Ctrl+Y',f:()=>dUndoRedo('redo'),off:!DK.fut.length}]);}
});
function dCopySel(){DK.clip=dSelItems().map(i=>({h:i.h,name:i.name,from:DK.path.join('/')}));dmsg(DK.clip.length+' 件をコピーしました（Ctrl+V で貼り付け）');}

/* ---------- 開く（エディター / 別ウインドウ） ---------- */
function dEdWin(key){const w=Math.min(screen.availWidth,1600),h=Math.min(screen.availHeight,1000);
  return window.open(location.pathname+'?'+key,'fp'+Date.now(),'width='+w+',height='+h+',left='+Math.max(0,(screen.availWidth-w)/2)+',top=0');}
async function dOpenItem(it,newWin=true){
  if(!it)return;
  if(newWin){const id='o'+Date.now();try{await dSet('open.'+id,{h:it.h,dir:DK.cur,path:DK.path,name:it.name});
      const w=dEdWin('open='+id);if(!w)msg('別ウインドウ','ポップアップがブロックされました。');else dlog('別ウインドウで開いた: '+it.name);}
    catch(e){msg('別ウインドウで開けません',e.message);}return;}
  await openFromDesk(it.h,DK.cur,DK.path);
}
function resetDoc(){
  for(const s of Object.values(state.sources)){try{s.doc.destroy();}catch(e){}}
  state.sources={};state.pages=[];state.sel.clear();tcache.clear();for(const c of cards.values())c.remove();cards.clear();clearSearch();
  ed.p=null;ed.sel=null;ed.tsel=null;ed.tchars=null;state.hist=[];state.fut=[];state.last=serialize();
  work.handle=null;work.name='';work.dir=null;work.origin=null;work.path=null;work.saved=serialize();renderGrid();showPage(null);
}
async function openFromDesk(fh,dir,path){
  if(isDirty()&&!confirm(tr('エディターで編集中の内容が保存されていません。閉じて別の文書を開きますか？')))return;
  try{const f=await fh.getFile();resetDoc();setView('editor');
    if(DKIND(f.name)==='fp'){await loadWorkFile(f);work.handle=fh;work.name=fh.name;}
    else{await addFiles([f]);state.hist=[];state.fut=[];state.last=serialize();work.saved=serialize();work.origin={name:f.name,h:fh};}
    work.dir=dir;work.path=path;updatePgNo();
    status('「'+f.name+'」を開きました。保存は元のフォルダ「'+((path||[]).slice(-1)[0]||'')+'」に行います');dlog('エディターで開いた: '+f.name);
  }catch(e){msg('開けません',e.message);dlog('開けない: '+e.message);}
}
/* エディターの保存先：デスクから開いた文書は元のフォルダへ */
async function deskSaveHandle(dir,fname){
  const ex=await dExists(dir,fname);
  if(ex&&!confirm(tr('同じフォルダに「'+fname+'」があります。上書きしますか？')))throw Object.assign(new Error('cancel'),{name:'AbortError'});
  if(!ex)dDeskOp({t:'create',dir,name:fname,label:'作業ファイル保存 '+fname});
  work.name=fname;return dir.getFileHandle(fname,{create:true});
}
async function saveOut(blob,name,opt={}){
  if(!work.dir){download(blob,name);return;}
  const dir=work.dir;
  if(await dExists(dir,name)){
    const isOrig=work.origin&&work.origin.name===name;
    if(!(opt.force&&isOrig)&&!confirm(tr(isOrig?'元のファイル「'+name+'」に上書きします。\n上書き前の版は「_削除予定」フォルダに残し、デスクの［元に戻す］で戻せます。':'同じフォルダに「'+name+'」があります。上書きしますか？\n（上書き前の版は「_削除予定」フォルダに残します）'))){
      name=await dFreeName(dir,name);}
    else{const tr_=await dir.getDirectoryHandle(TRASH,{create:true});const[b,e]=dSplit(name);const D=new Date(),p2=x=>String(x).padStart(2,'0'),st=D.getFullYear()+p2(D.getMonth()+1)+p2(D.getDate())+'_'+p2(D.getHours())+p2(D.getMinutes())+p2(D.getSeconds());
      const bname=await dFreeName(tr_,b+'_上書き前_'+st+e);await dWrite(tr_,bname,await (await (await dir.getFileHandle(name)).getFile()));
      await dWrite(dir,name,blob);dDeskOp({t:'overwrite',dir,name,bdir:tr_,bname,label:'上書き '+name});dlog('上書き保存: '+name+'（前の版 → _削除予定/'+bname+'）');status('「'+name+'」に上書きしました（前の版は _削除予定 に残しました）');return;}
  }
  await dWrite(dir,name,blob);dDeskOp({t:'create',dir,name,label:'保存 '+name});dlog('書き出し: '+name);status('「'+name+'」を元のフォルダに保存しました');
}

/* ---------- プレビュー（開かずに大きく確認） ---------- */
const PV={it:null,doc:null,task:null,pg:1,n:1};
async function dPreview(it){
  if(!it)return;PV.it=it;PV.pg=1;$('#dkPrev').classList.add('show');const body=$('#pvBody');body.innerHTML='';
  try{if(PV.task){try{await PV.task.destroy();}catch(e){}}PV.task=null;PV.doc=null;const f=await it.h.getFile();
    if(it.kind==='img'){const img=new Image();img.src=URL.createObjectURL(f);body.appendChild(img);PV.n=1;dPvInfo();return;}
    let bytes=new Uint8Array(await f.arrayBuffer());if(it.kind==='fp'){const r=await dWorkFirst(bytes);if(!r){body.textContent='作業ファイルを表示できません';return;}bytes=r.bytes;}
    PV.task=dDoc(bytes);PV.doc=await PV.task.promise;PV.n=PV.doc.numPages;await dPvShow();}
  catch(e){body.textContent='表示できません: '+e.message;}
}
async function dPvShow(){if(!PV.doc)return;const pg=await PV.doc.getPage(PV.pg);const a=$('#dkArea');const v0=pg.getViewport({scale:1});
  const sc=Math.min((a.clientWidth-40)/v0.width,(a.clientHeight-70)/v0.height)*(window.devicePixelRatio||1);const vp=pg.getViewport({scale:sc});
  const cv=document.createElement('canvas');cv.width=vp.width;cv.height=vp.height;cv.style.width=vp.width/(window.devicePixelRatio||1)+'px';
  await pg.render({canvasContext:cv.getContext('2d'),viewport:vp}).promise;const b=$('#pvBody');b.innerHTML='';b.appendChild(cv);dPvInfo();}
function dPvInfo(){$('#pvInfo').textContent=PV.it.name+'　'+PV.pg+' / '+PV.n;}
function dPvClose(){$('#dkPrev').classList.remove('show');if(PV.task){PV.task.destroy();PV.task=null;PV.doc=null;}}
function dPvDoc(d){const vis=DK.items.filter(i=>i.el&&i.el.isConnected);const i=vis.indexOf(PV.it)+d;if(i<0||i>=vis.length)return;DK.sel.clear();DK.sel.add(vis[i].name);dRefreshSel();dPreview(vis[i]);}
$('#pvPrev').onclick=()=>{if(PV.pg>1){PV.pg--;dPvShow();}};$('#pvNext').onclick=()=>{if(PV.pg<PV.n){PV.pg++;dPvShow();}};
$('#pvClose').onclick=dPvClose;$('#pvOpen').onclick=()=>{const it=PV.it;dPvClose();dOpenItem(it);};
$('#pvBody').addEventListener('wheel',e=>{if(e.ctrlKey)return;if(e.deltaY>0&&PV.pg<PV.n){PV.pg++;dPvShow();e.preventDefault();}else if(e.deltaY<0&&PV.pg>1){PV.pg--;dPvShow();e.preventDefault();}},{passive:false});

/* ---------- 自動反映（フォルダの変更を見張る） ---------- */
function dScheduleRefresh(why){clearTimeout(DK.refreshT);DK.refreshT=setTimeout(async()=>{if(!DK.cur||!DK.on)return;await dPullOps();const b=DK.items.map(i=>i.name).join('|');await dOpenDir(DK.cur,DK.path,true);if(b!==DK.items.map(i=>i.name).join('|'))dlog('自動で反映しました（'+why+'）');},400);}
async function dStartWatch(){
  if(DK.watcher){DK.watcher.disconnect();DK.watcher=null;}clearInterval(DK.pollT);
  if('FileSystemObserver' in window){try{
      DK.watcher=new FileSystemObserver(recs=>{const here=DK.path.slice(1).join('/');
        if(recs.some(r=>{const rp=r.relativePathComponents||[];if(rp[rp.length-1]===DSETTINGS)return false;const p=rp.slice(0,-1).join('/');const p2=r.relativePathMovedFrom?r.relativePathMovedFrom.slice(0,-1).join('/'):null;return p===here||p2===here||r.type==='unknown'||r.type==='errored';}))dScheduleRefresh('フォルダの変更');});
      await DK.watcher.observe(DK.root,{recursive:true});dlog('フォルダの変更の見張りを開始');return;}catch(e){dlog('見張り機能を使えない: '+e.message);}}
  DK.pollT=setInterval(async()=>{if(!DK.cur||!DK.on||document.hidden)return;const names=[];try{for await(const [n,h] of DK.cur.entries())if(h.kind==='file'&&DKIND(n))names.push(n);}catch(e){return;}
    names.sort((a,b)=>a.localeCompare(b,'ja',{numeric:true}));if(names.join('|')!==DK.items.map(i=>i.name).join('|'))dScheduleRefresh('定期確認');},4000);
  dlog('自動反映：4秒ごとの確認で代用');
}
window.addEventListener('focus',()=>{if(DK.on&&DK.cur)dScheduleRefresh('画面に戻った');});

/* ---------- ボタン・キー・ドロップ ---------- */
$('#dkPick').onclick=dPickRoot;$('#dkReload').onclick=()=>DK.cur&&dOpenDir(DK.cur,DK.path);
$('#dkQ').oninput=dLayout;$('#dkSize').oninput=()=>{DK.size=+$('#dkSize').value;LS.set('deskSize',DK.size);dLayout();};
$('#dkAlign').onclick=()=>{if(!DK.cur)return;DK.pos={};dSavePos();dLayout();dmsg('名前順に並べ直しました');};
$('#dkOpen').onclick=()=>dOpenItem(dSelItems()[0]);$('#dkWin').onclick=()=>dOpenItem(dSelItems()[0],false);
$('#dkPrevB').onclick=()=>dPreview(dSelItems()[0]);$('#dkRen').onclick=dRename;$('#dkTrash').onclick=dTrash;
$('#dkUndo').onclick=()=>dUndoRedo('undo');$('#dkRedo').onclick=()=>dUndoRedo('redo');
$('#dkLogB').onclick=()=>$('#deskWin').classList.toggle('devlog');
$('#dkCopyLog').onclick=()=>{const t=['Front PDF デスク ログ（v'+APP_VER+(DEV?' 開発版':'')+'）',navigator.userAgent,'FileSystemObserver: '+('FileSystemObserver' in window),''].concat(DKLOG).join('\n');
  copyText(t);dmsg('ログをコピーしました。不具合の報告に貼り付けてください');};
let pvCombo=false;
document.addEventListener('keydown',e=>{if(!DK.on)return;if((e.key==='Shift'&&e.ctrlKey)||(e.key==='Control'&&e.shiftKey))pvCombo=true;else if(e.key!=='Shift'&&e.key!=='Control')pvCombo=false;},true);
document.addEventListener('keyup',e=>{if(!DK.on)return;if(pvCombo&&(e.key==='Shift'||e.key==='Control')){pvCombo=false;if(document.querySelector('.modal.show')||isTyping(e.target))return;
  if($('#dkPrev').classList.contains('show'))dPvClose();else if(DK.sel.size)dPreview(dSelItems()[0]);}});
document.addEventListener('keydown',e=>{
  if(!DK.on||document.querySelector('.modal.show')||isTyping(e.target))return;
  if(e.key==='Escape'&&$('#dkMenu').classList.contains('show')){dMenuClose();return;}
  const ctrl=e.ctrlKey||e.metaKey,k=e.key.toLowerCase();
  if($('#dkPrev').classList.contains('show')){
    if(e.key==='Escape'||e.key===' '){e.preventDefault();dPvClose();}else if(e.key==='ArrowRight'){e.preventDefault();$('#pvNext').click();}else if(e.key==='ArrowLeft'){e.preventDefault();$('#pvPrev').click();}
    else if(e.key==='ArrowDown'){e.preventDefault();dPvDoc(1);}else if(e.key==='ArrowUp'){e.preventDefault();dPvDoc(-1);}else if(e.key==='Enter'){e.preventDefault();$('#pvOpen').click();}return;}
  if(ctrl&&k==='z'){e.preventDefault();dUndoRedo(e.shiftKey?'redo':'undo');}
  else if(ctrl&&k==='y'){e.preventDefault();dUndoRedo('redo');}
  else if(ctrl&&k==='c'&&DK.sel.size){e.preventDefault();dCopySel();}
  else if(ctrl&&k==='v'){e.preventDefault();dPaste();}
  else if(ctrl&&k==='a'){e.preventDefault();DK.items.forEach(i=>DK.sel.add(i.name));dRefreshSel();}
  else if(ctrl&&k==='f'){e.preventDefault();$('#dkQ').focus();}
  else if(ctrl&&k==='p'){e.preventDefault();if(DK.sel.size)dPrint();}
  else if(e.key==='F2'){e.preventDefault();dRename();}
  else if(e.key==='Delete'){e.preventDefault();dTrash();}
  else if(e.key==='Enter'&&DK.sel.size===1){e.preventDefault();dOpenItem(dSelItems()[0]);}
  else if(e.key===' '&&DK.sel.size){e.preventDefault();dPreview(dSelItems()[0]);}
});
$('#dkArea').addEventListener('dragover',e=>{if(DK.cur&&[...e.dataTransfer.types].includes('Files')){e.preventDefault();$('#dkDesk').classList.add('drop');}});
$('#dkArea').addEventListener('dragleave',()=>$('#dkDesk').classList.remove('drop'));
$('#dkArea').addEventListener('dragover',e=>{if(!DK.cur&&[...e.dataTransfer.types].includes('Files'))e.preventDefault();});
$('#dkArea').addEventListener('drop',async e=>{e.preventDefault();$('#dkDesk').classList.remove('drop');const fs=[...e.dataTransfer.files];if(!fs.length)return;
  if(!DK.cur){const id='f'+Date.now();await dSet('open.'+id,{files:fs});if(!dEdWin('open='+id))msg('エディター','ポップアップがブロックされました。');return;}
  await dImport(fs,DK.cur,DK.path);});
document.addEventListener('dragover',e=>{if(DK.on)e.preventDefault();},true);
document.addEventListener('drop',e=>{if(DK.on&&!e.defaultPrevented)e.preventDefault();});

/* ---------- 起動 ---------- */
(async function deskBoot(){
  $('#dkSize').value=DK.size;
  const qp=new URLSearchParams(location.search);
  if(qp.get('editor')){setView('editor');$('#toDesk').textContent='デスクを表示';return;}
  if(qp.get('open')){setView('editor');$('#toDesk').textContent='デスクを表示';try{const rec=await dGet('open.'+qp.get('open'));if(!rec)throw new Error('ファイルの情報を受け取れませんでした');
      if(rec.files){await addFiles(rec.files);dDel('open.'+qp.get('open'));return;}
      const go=async()=>{await openFromDesk(rec.h,rec.dir,rec.path);dDel('open.'+qp.get('open'));};
      if((await rec.h.queryPermission({mode:'readwrite'}))==='granted')await go();
      else{$('#dkResume').firstElementChild.innerHTML='<span>フォルダを開きます</span><br><b data-noi18n></b><br><small style="opacity:.75">クリックすると開きます</small>';$('#dkResume b').textContent=rec.name;const ov=$('#dkResume');ov.classList.add('show');
        ov.onclick=async()=>{ov.classList.remove('show');try{await rec.h.requestPermission({mode:'readwrite'});await rec.dir.requestPermission({mode:'readwrite'});}catch(e){}await go();};}
    }catch(e){msg('開けません',e.message);}return;}
  setView('desk');
  if(!window.showDirectoryPicker){$('#dkTree').innerHTML='<div class="empty">このブラウザではデスクを使えません（Microsoft Edge か Google Chrome をお使いください）。［エディター］から PDF の編集はできます。</div>';$('#dkPick').disabled=true;return;}
  try{const h=await dGet('root');if(!h)return;
    if((await h.queryPermission({mode:'readwrite'}))==='granted'){await dResume(h);return;}
    $('#dkResumeName').textContent=h.name;const ov=$('#dkResume');ov.classList.add('show');ov.onclick=async()=>{ov.classList.remove('show');await dResume(h);};
    dlog('前回のフォルダの再許可待ち');}catch(e){dlog('記憶の読み込み失敗: '+e.message);}
})();
