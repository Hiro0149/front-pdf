import asyncio, os, math
from playwright.async_api import async_playwright
H='file://'+os.path.abspath('out/PDF_KOBO.html')+'#nowelcome'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=await b.new_page(locale='ja-JP',viewport={'width':1280,'height':860},device_scale_factor=1.5)
    await pg.goto(H); await pg.click('#bBlank'); await pg.wait_for_timeout(800)
    box=await pg.locator('#edOv').bounding_box(); k=box['width']/595.28; X=lambda x:box['x']+x*k; Y=lambda y:box['y']+y*k
    async def tool(t): await pg.click(f'#toolbox button[data-t={t}]'); await pg.wait_for_timeout(60)
    async def stroke(pts,steps=1):
      await pg.mouse.move(X(pts[0][0]),Y(pts[0][1])); await pg.mouse.down()
      for x,y in pts[1:]: await pg.mouse.move(X(x),Y(y),steps=steps)
      await pg.mouse.up()
    D=lambda js: pg.evaluate(js)
    # 空（エアブラシ）
    await D("Object.assign(ed.defaults.pen,{style:'air',color:'#7fb8e8',lw:38,alpha:70})"); await tool('pen')
    for y in (70,108): await stroke([(40+i*26, y+8*math.sin(i/2)) for i in range(21)],2)
    # 山（ブラシ）
    await D("Object.assign(ed.defaults.brush,{color:'#2f5d46',lw:7})"); await tool('brush')
    await stroke([(40,520),(150,330),(230,450),(330,280),(450,470),(555,380)],10)
    # 木々（ブラシ）
    for x in (110,170,420,480):
      await stroke([(x,560),(x,500)],6); 
    await D("Object.assign(ed.defaults.pen,{style:'air',color:'#3e8e5e',lw:30,alpha:85})"); await tool('pen')
    for x in (110,170,420,480): await stroke([(x+16*math.cos(t/10*2*math.pi)*(1-t/40), 478+20*math.sin(t/10*2*math.pi)*(1-t/40)) for t in range(21)],2)
    # 太陽：ペンで円 → バケツで塗る
    await D("Object.assign(ed.defaults.pen,{style:'pen',color:'#e8a33d',lw:4,alpha:100})"); await tool('pen')
    await stroke([(470+40*math.cos(t/24*2*math.pi), 205+40*math.sin(t/24*2*math.pi)) for t in range(26)],2)
    await D("Object.assign(ed.defaults.bucket,{color:'#ffd35c'})"); await tool('bucket'); await pg.mouse.click(X(470),Y(205)); await pg.wait_for_timeout(300)
    # 星（図形）→ バケツで色替え
    await tool('star'); await stroke([(255,600),(345,690)],4); await pg.wait_for_timeout(100)
    await D("Object.assign(ed.defaults.bucket,{color:'#ff7a59'})"); await tool('bucket'); await pg.mouse.click(X(300),Y(645)); await pg.wait_for_timeout(200)
    # 絵文字
    await D("Object.assign(ed.defaults.emoji,{text:'🌲',size:46})"); await tool('emoji'); await pg.mouse.click(X(70),Y(640)); await pg.mouse.click(X(510),Y(650))
    await D("Object.assign(ed.defaults.emoji,{text:'🐦',size:30})"); await tool('emoji'); await pg.mouse.click(X(250),Y(220))
    # ハンコ（花まる）
    await tool('stamp'); styles=await D("LIB.map(s=>s.style)"); await pg.locator('.lib button').nth(styles.index('hanamaru')).click(); await pg.mouse.click(X(150),Y(740))
    # 文字
    await D("Object.assign(ed.defaults.text,{text:'PDF_KOBO でお絵描き',size:26,font:'mincho',color:'#2f5d46'})"); await tool('text'); await pg.mouse.click(X(200),Y(760))
    await tool('select'); await pg.mouse.click(X(560),Y(820)); await pg.wait_for_timeout(300)
    await pg.screenshot(path='site_work/draw_full.png')
    await pg.screenshot(path='site_work/draw.png',clip={'x':X(0),'y':Y(30),'width':595.28*k,'height':780*k})
    # 2ページ同時表示
    pg2=await b.new_page(locale='ja-JP',viewport={'width':1280,'height':800},device_scale_factor=1.5)
    await pg2.goto(H); await pg2.set_input_files('#fileIn',['site_work/demo_ja.pdf']); await pg2.wait_for_timeout(1500)
    c=pg2.locator('.card'); await c.nth(0).click(); await c.nth(1).click(modifiers=['Control']); await pg2.wait_for_timeout(1200)
    b1=await pg2.locator('#edOv').bounding_box(); b2=await pg2.locator('#edOv2').bounding_box(); k1=b1['width']/595.28; k2=b2['width']/595.28
    await pg2.click('#toolbox button[data-t=stamp]'); st=await pg2.evaluate("LIB.map(s=>s.style)"); await pg2.locator('.lib button').nth(st.index('hanamaru')).click(); await pg2.mouse.click(b1['x']+380*k1,b1['y']+205*k1)
    await pg2.click('#toolbox button[data-t=note]'); await pg2.mouse.click(b2['x']+330*k2,b2['y']+430*k2); await pg2.wait_for_timeout(150)
    await pg2.keyboard.type('別紙の4番、数量の確認をお願いします'); await pg2.keyboard.press('Control+Enter')
    await pg2.click('#toolbox button[data-t=select]'); await pg2.keyboard.press('Escape'); await pg2.mouse.click(b2['x']+300*k2,b2['y']+780*k2); await pg2.wait_for_timeout(300)
    print('panes',await pg2.evaluate('ed.panes.length'))
    await pg2.screenshot(path='site_work/dual.png')
    await b.close()
asyncio.run(main())
