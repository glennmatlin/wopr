const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  // Collect all console messages
  page.on('console', msg => console.log(`BROWSER CONSOLE [${msg.type()}]: ${msg.text()}`));
  page.on('pageerror', err => console.error(`BROWSER ERROR: ${err.message}`));

  try {
    await page.goto('http://localhost:5173/');
    // Wait for a second to let React render
    await page.waitForTimeout(2000);
    await page.screenshot({ path: 'screenshot.png' });
    console.log('Screenshot saved to screenshot.png');
  } catch (err) {
    console.error('Failed to load page:', err);
  } finally {
    await browser.close();
  }
})();
