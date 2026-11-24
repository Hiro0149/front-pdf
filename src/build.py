import json,base64,os,re
nm='node_modules/'; pj='v5/node_modules/pdfjs-dist/' if os.path.isdir('v5/node_modules/pdfjs-dist') else 'node_modules/pdfjs-dist/'
def to_classic(code,glob=None):
    code=code.replace('import.meta.url','""')
    m=list(re.finditer(r'export\s*\{([^}]*)\}\s*;?',code))
    assert len(m)==1; m=m[0]
    rep=''
    if glob:
        ents=[]
        for e in m.group(1).split(','):
            e=e.strip()
            if not e: continue
            if ' as ' in e: a,b=[x.strip() for x in e.split(' as ')]; ents.append(f'{b}:{a}')
            else: ents.append(f'{e}:{e}')
        rep=f'globalThis.{glob}={{{",".join(ents)}}};'
    code=code[:m.start()]+rep+code[m.end():]
    assert not re.search(r'(^|[;}\s])import\s*[{*\w]', code[:0]+'')  # placeholder
    return '(function(){"use strict";\n'+code+'\n})();'
s=open('app.html',encoding='utf-8').read()
cm={}
d=pj+'cmaps/'
for f in os.listdir(d):
    if re.search(r'JIS|RKSJ|Japan1|^H\.|^V\.|^EUC-|^78-|Hankaku|Hiragana|Katakana|Roman|WP-Symbol|^Ext-|^Add-|^NWP|^83pv|^90p',f):
        cm[f[:-6]]=base64.b64encode(open(d+f,'rb').read()).decode()
wasm={f:base64.b64encode(open(pj+'wasm/'+f,'rb').read()).decode() for f in ['openjpeg.wasm','jbig2.wasm']}
main=to_classic(open(pj+'legacy/build/pdf.min.mjs',encoding='utf-8').read(),'pdfjsLib')
work=to_classic(open(pj+'legacy/build/pdf.worker.min.mjs',encoding='utf-8').read())
for t in (main,work): assert '</script' not in t.lower() and '<!--' not in t
s=s.replace('/*__PDFLIB__*/',open(nm+'pdf-lib/dist/pdf-lib.min.js',encoding='utf-8').read())
s=s.replace('/*__PDFJS__*/',main).replace('/*__WORKER__*/',work)
import subprocess,sys;subprocess.check_call([sys.executable,'i18n_src.py'])  # 翻訳辞書 i18n.json を生成
i18n=json.load(open('i18n.json',encoding='utf-8'))
s=s.replace('/*__I18N__*/',json.dumps(i18n,ensure_ascii=False))
# ===== 公開設定（ここだけ書き換える） =====
SITE_URL=os.environ.get('KOBO_SITE','')   # 公式ページの URL 例 'https://USER.github.io/front-pdf/'（空のあいだは利用登録なしで起動）
REPO_URL=os.environ.get('KOBO_REPO','')   # リポジトリの URL 例 'https://github.com/USER/front-pdf'
DONATE_URL=''                             # 応援ページの URL（空なら公式ページに表示しない）
APP_VERSION='1.1.1'
WORKS=[{'name':'ExVAN Planner','ja':'コンテナ積み付け最適化ソフト（業務用）','en':'Container loading optimizer (for business)','url':'https://exvan-planner.github.io/'},{'name':'ものがたり英単語','ja':'ストーリーで覚える英検単語アプリ（無料）','en':'Learn Eiken (English test) vocabulary through stories (free)','url':'https://hiro0149.github.io/story-eitango/'}]
ACTIVATION=True                           # True: SITE_URL があれば初回に利用登録を求める
LIC_SECRET='FSW-PDFKOBO-7f3a9c2e5b1d'      # 登録コード計算用の文字列（アプリと公式ページで共通。変えると全員再登録）
OUT=os.environ.get('KOBO_OUT','out')
ACT=bool(SITE_URL and ACTIVATION)
licjs=open('kobo_lic.js',encoding='utf-8').read().replace('/*__LICSECRET__*/',LIC_SECRET)
qr=open(nm+'qrcode-generator/qrcode.js',encoding='utf-8').read()
for t in (licjs,qr): assert '</script' not in t.lower()
s=s.replace('/*__LIC__*/',licjs).replace('/*__QR__*/',qr).replace('/*__ACT__*/false','true' if ACT else 'false').replace("'/*__SITEURL__*/'",json.dumps(SITE_URL))
LANGS=['ja','en','zhCN','zhTW','pt','fr','ko']
apx=open('manual/_appendix.md',encoding='utf-8').read().strip()
mans={l:open('manual/%s.md'%l,encoding='utf-8').read().strip()+'\n\n'+apx+'\n' for l in LANGS}
head=(
"> For AI assistants: this block is the official manual of the single-file web app \"Front PDF\" (v1.1.0, (c) 2026 Front Softworks, MIT License).\n"
"> Use it to answer questions about how to operate the app, to troubleshoot, and as a map of the code when asked to modify it.\n"
"> Japanese and English versions follow, then technical notes. Manuals in all 7 UI languages are in the script#manuals JSON block.\n\n")
man=head+open('manual/ja.md',encoding='utf-8').read().strip()+'\n\n---\n\n'+open('manual/en.md',encoding='utf-8').read().strip()+'\n\n---\n\n'+apx+'\n'
for t in [man]+list(mans.values()): assert '</script' not in t.lower()
s=s.replace('/*__MANUAL__*/',man)
s=s.replace('/*__MANUALS__*/',json.dumps(mans,ensure_ascii=False).replace('</','<\\/'))
lic=open('LICENSE',encoding='utf-8').read();nt=open('THIRD_PARTY_NOTICES.txt',encoding='utf-8').read()
for t in (lic,nt): assert '</script' not in t.lower() and '<!--' not in t
s=s.replace('/*__LICENSE__*/',lic).replace('/*__NOTICES__*/',nt)
s=s.replace('/*__CMAPS__*/',json.dumps(cm)).replace('/*__WASM__*/',json.dumps(wasm))
DEVB=os.environ.get('KOBO_DEV','')=='1'
s=s.replace('/*__DESK_CSS__*/',open('desk/desk.css',encoding='utf-8').read()).replace('<!--__DESK_HTML__-->',open('desk/desk.html',encoding='utf-8').read())
s=s.replace('/*__DESK_JS__*/',open('desk/desk.js',encoding='utf-8').read())
s=s.replace('/*__DEV__*/false','true' if DEVB else 'false')
os.makedirs(OUT,exist_ok=True)
import shutil
shutil.rmtree(OUT,ignore_errors=True);os.makedirs(OUT,exist_ok=True)
open(OUT+'/Front_PDF.html','w',encoding='utf-8').write(s)
for l in LANGS: open(OUT+'/Front_PDF_manual_%s.md'%l,'w',encoding='utf-8').write(mans[l])
import shutil;shutil.copy('LICENSE',OUT+'/LICENSE');shutil.copy('THIRD_PARTY_NOTICES.txt',OUT+'/THIRD_PARTY_NOTICES.txt')
import hashlib;h=hashlib.sha256(open(OUT+'/Front_PDF.html','rb').read()).hexdigest();open(OUT+'/SHA256SUMS.txt','w').write(h+'  Front_PDF.html\n');print('sha256',h)
print(len(cm),'cmaps', os.path.getsize(OUT+'/Front_PDF.html'))

# ===== 配布用 ZIP =====
import zipfile
with zipfile.ZipFile(OUT+'/Front_PDF.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for f in sorted(os.listdir(OUT)):
        if f!='Front_PDF.zip': z.write(OUT+'/'+f,'Front_PDF/'+f)
# ===== 公式ページ（docs/ → GitHub Pages） =====
SITE_OUT=os.environ.get('KOBO_SITE_OUT','docs')
rj='site_src/releases.json'
rel=json.load(open(rj,encoding='utf-8')) if os.path.exists(rj) else {}
if SITE_URL and not os.environ.get('KOBO_TEST'):  # 公開用ビルドのときだけ公式ハッシュとして記録（同じ版は上書き）
    rel['v'+APP_VERSION]=h; json.dump(rel,open(rj,'w',encoding='utf-8'),indent=1,ensure_ascii=False)
hashes={v2:k2 for k2,v2 in rel.items()}; hashes[h]='v'+APP_VERSION
cfg={'version':APP_VERSION,'size':os.path.getsize(OUT+'/Front_PDF.html'),'sha256':h,'hashes':hashes,'repo':REPO_URL,'site':SITE_URL,'donate':DONATE_URL,'works':WORKS}
site=open('site_src/index.html',encoding='utf-8').read().replace('/*__LIC__*/',licjs).replace('/*__CFG__*/{}',json.dumps(cfg,ensure_ascii=False))
shutil.rmtree(SITE_OUT,ignore_errors=True);os.makedirs(SITE_OUT)
open(SITE_OUT+'/index.html','w',encoding='utf-8').write(site)
SITE_ASSETS=['hero.jpg','act_1.jpg','act_2.jpg','act_3.jpg','screenshot_ja.jpg','screenshot_en.jpg','feat_tsel.jpg','feat_stamp.jpg','feat_dual.jpg','feat_draw.jpg','feat_emoji.jpg','feat_paste.jpg','feat_desk.jpg','demo_editor.mp4','demo_editor.jpg','demo_desk.mp4','demo_desk.jpg']+['skin_%s.jpg'%k for k in ('modern','dark','98','aqua','gba','mofu')]
for f in SITE_ASSETS: shutil.copy('site_work/'+f,SITE_OUT+'/'+f)
shutil.copy('site_src/sitemap.xml',SITE_OUT+'/sitemap.xml')
shutil.copy('site_src/google0b06dbd8d8f1ec95.html',SITE_OUT+'/google0b06dbd8d8f1ec95.html')  # Search Console 所有権確認（消すと登録が外れる）
open(SITE_OUT+'/.nojekyll','w').close()
print('site ->',SITE_OUT, 'activation' if ACT else 'no-activation')
