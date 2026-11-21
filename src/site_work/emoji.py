import asyncio, os
from playwright.async_api import async_playwright
H='file://'+os.path.abspath('out/PDF_KOBO.html')+'#nowelcome'
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    pg=await b.new_page(locale='ja-JP',viewport={'width':1280,'height':860},device_scale_factor=1.5)
    await pg.goto(H); await pg.set_input_files('#fileIn',['site_work/demo_ja.pdf']); await pg.wait_for_timeout(1500)
    await pg.click('#toolbox button[data-t=emoji]'); await pg.wait_for_timeout(300)
    pb=await pg.locator('.props').bounding_box()
    await pg.screenshot(path='site_work/emoji_panel.png',clip={'x':pb['x'],'y':pb['y'],'width':pb['width'],'height':min(pb['height'],560)})
    await b.close()
asyncio.run(main())
