import asyncio, os
from playwright.async_api import async_playwright
H='file://'+os.path.abspath('out/PDF_KOBO.html')+'#nowelcome'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    for skin in ['modern','dark','98','aqua','gba']:
      pg=await b.new_page(locale='ja-JP',viewport={'width':1280,'height':800},device_scale_factor=1)
      await pg.goto(H); await pg.select_option('#skinSel',skin)
      await pg.set_input_files('#fileIn',['site_work/demo_ja.pdf']); await pg.wait_for_timeout(1500)
      await pg.click('#toolbox button[data-t=select]'); await pg.wait_for_timeout(200)
      await pg.screenshot(path=f'site_work/skin_{skin}.png'); await pg.close()
    # table copy demo: select rows in text-select mode
    pg=await b.new_page(locale='ja-JP',viewport={'width':1280,'height':800},device_scale_factor=1.5)
    await pg.goto(H); await pg.set_input_files('#fileIn',['site_work/demo_ja.pdf']); await pg.wait_for_timeout(1500)
    box=await pg.locator('#edOv').bounding_box(); k=box['width']/595.28; X=lambda x:box['x']+x*k; Y=lambda y:box['y']+y*k
    await pg.click('#toolbox button[data-t=textsel]') if await pg.locator('#toolbox button[data-t=textsel]').count() else None
    tools=await pg.evaluate("[...document.querySelectorAll('#toolbox button')].map(b=>b.dataset.t)")
    print(tools)
    await b.close()
asyncio.run(main())
