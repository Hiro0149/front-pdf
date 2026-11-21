import asyncio, os
from playwright.async_api import async_playwright
H='file://'+os.path.abspath('out/PDF_KOBO.html')+'#nowelcome'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=await b.new_page(locale='ja-JP',viewport={'width':1280,'height':860},device_scale_factor=1.5)
    await pg.goto(H); await pg.set_input_files('#fileIn',['site_work/demo_ja.pdf']); await pg.wait_for_timeout(1500)
    await pg.locator('.card').nth(1).click(); await pg.wait_for_timeout(800)
    await pg.set_input_files('#imgIn','site_work/snip.png'); await pg.wait_for_timeout(800)
    box=await pg.locator('#edOv').bounding_box(); k=box['width']/595.28; X=lambda x:box['x']+x*k; Y=lambda y:box['y']+y*k
    o=await pg.evaluate("(()=>{const o=ed.p.objects[ed.p.objects.length-1];return [o.type,o.x,o.y,o.w,o.h]})()"); print(o)
    # move image to lower area
    await pg.evaluate("(()=>{const o=ed.p.objects[ed.p.objects.length-1];const r=o.h/o.w;o.w=380;o.h=380*r;o.x=105;o.y=430;edRedraw();})()")
    await pg.click('#toolbox button[data-t=note]'); await pg.mouse.click(X(420),Y(250)); await pg.wait_for_timeout(150)
    await pg.keyboard.type('Snipping Tool のグラフを Ctrl+V で貼り付け'); await pg.keyboard.press('Control+Enter')
    await pg.click('#toolbox button[data-t=select]'); await pg.keyboard.press('Escape'); await pg.mouse.click(X(560),Y(820)); await pg.wait_for_timeout(300)
    await pg.screenshot(path='site_work/paste.png',clip={'x':X(0),'y':Y(0),'width':595.28*k,'height':720*k})
    await b.close()
asyncio.run(main())
