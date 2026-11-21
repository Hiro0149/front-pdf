import asyncio, os, sys
from playwright.async_api import async_playwright
H='file://'+os.path.abspath('out/PDF_KOBO.html')+'#nowelcome'
async def shot(b,lang):
    pg=await b.new_page(locale='ja-JP' if lang=='ja' else 'en-US',viewport={'width':1400,'height':860},device_scale_factor=1.5)
    await pg.goto(H); await pg.select_option('#langSel',lang)
    await pg.set_input_files('#fileIn',[f'site_work/demo_{lang}.pdf']); await pg.wait_for_timeout(1800)
    box=await pg.locator('#edOv').bounding_box(); k=box['width']/595.28; X=lambda x:box['x']+x*k; Y=lambda y:box['y']+y*k
    async def tool(t): await pg.click(f'#toolbox button[data-t={t}]'); await pg.wait_for_timeout(80)
    await tool('marker'); await pg.mouse.move(X(48),Y(203)); await pg.mouse.down(); await pg.mouse.move(X(300 if lang=='ja' else 250),Y(220),steps=6); await pg.mouse.up()
    await tool('stamp'); styles=await pg.evaluate("LIB.map(s=>s.style)")
    await pg.locator('.lib button').nth(styles.index('hanamaru')).click(); await pg.mouse.click(X(370),Y(205))
    await tool('stamp'); await pg.locator('.lib button').nth(styles.index('date')).click(); await pg.mouse.click(X(515),Y(92))
    await tool('pen'); await pg.mouse.move(X(400),Y(332)); await pg.mouse.down()
    for i in range(0,26): await pg.mouse.move(X(400+i*3),Y(332+ (3 if i%2 else -3)*0)+0)
    await pg.mouse.up()
    await tool('note'); await pg.mouse.click(X(400),Y(560)); await pg.wait_for_timeout(150)
    await pg.keyboard.type('単価の再確認をお願いします。\n納期は12月第2週希望です。' if lang=='ja' else 'Please double-check the unit price.\nDelivery wanted by mid-Dec.')
    await pg.keyboard.press('Control+Enter'); await pg.wait_for_timeout(100)
    await tool('select'); await pg.mouse.click(X(560),Y(820)); await pg.wait_for_timeout(300)
    await pg.screenshot(path=f'site_work/screenshot_{lang}.png'); await pg.close()
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
    for l in ['ja','en']: await shot(b,l)
    await b.close()
asyncio.run(main())
