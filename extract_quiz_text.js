const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  try {
    await page.goto('https://zealy.io/cw/chainersnft/questboard/f6185b3a-a38d-4ca1-9c06-874d12a2f70c/543a36a0-2435-4290-9047-d1a892fa27b3', { waitUntil: 'networkidle' });
    await page.waitForTimeout(5000);
    const text = await page.innerText('body');
    console.log('--- BODY TEXT START ---');
    console.log(text);
    console.log('--- BODY TEXT END ---');
    await page.screenshot({ path: 'chainers_quiz_v2.png', fullPage: true });
  } catch (e) {
    console.log('Error: ' + e.message);
  }
  await browser.close();
})();
