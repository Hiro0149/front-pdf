import asyncio, os
from playwright.async_api import async_playwright
H='file://'+os.path.abspath('out/PDF_KOBO.html')+'#nowelcome'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    ctx=await b.new_context(locale='ja-JP',viewport={'width':1280,'height':860},device_scale_factor=1.5); await ctx.grant_permissions(['clipboard-read','clipboard-write'])
    pg=await ctx.new_page(); await pg.goto(H); await pg.set_input_files('#fileIn',['site_work/demo_ja.pdf']); await pg.wait_for_timeout(1500)
    await pg.select_option('#zoomSel','1') if await pg.locator('#zoomSel').count() else None
    box=await pg.locator('#edOv').bounding_box(); k=box['width']/595.28; X=lambda x:box['x']+x*k; Y=lambda y:box['y']+y*k
    await pg.click('#toolbox button[data-t=tsel]'); await pg.wait_for_timeout(100)
    await pg.mouse.move(X(46),Y(256)); await pg.mouse.down(); await pg.mouse.move(X(552),Y(418),steps=8); await pg.mouse.up(); await pg.wait_for_timeout(300)
    await pg.keyboard.press('Control+c'); await pg.wait_for_timeout(200)
    try: print(repr((await pg.evaluate('navigator.clipboard.readText()'))[:300]))
    except Exception as e: print('clip err',e)
    await pg.screenshot(path='site_work/tsel_full.png')
    await pg.screenshot(path='site_work/tsel.png',clip={'x':X(30),'y':Y(240),'width':(552-30+16)*k,'height':(430-240)*k})
    await b.close()
asyncio.run(main())
