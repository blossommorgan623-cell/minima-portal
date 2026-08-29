const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://zealy.io/cw/travala/questboard/353b17d0-2884-425a-a3a4-c4659e0dac36/f79f9585-44bd-4e7f-8705-96f534ba16dc');
  await page.waitForTimeout(5000); // Wait for scripts to execute

  const content = await page.content();
  fs.writeFileSync('quest_debug.html', content);

  const questData = await page.evaluate(() => {
    // Try to find the quest in common Next.js state locations
    return window.__NEXT_DATA__ || window.__next_f || 'Not found in window';
  });

  fs.writeFileSync('quest_data.json', JSON.stringify(questData, null, 2));

  await browser.close();
})();
