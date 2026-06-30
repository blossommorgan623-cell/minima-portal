import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        url = "https://zealy.io/cw/travala/questboard/353b17d0-2884-425a-a3a4-c4659e0dac36/f79f9585-44bd-4e7f-8705-96f534ba16dc"
        await page.goto(url)

        # Wait for potential redirects or loading
        await page.wait_for_timeout(5000)

        # Try to click "Accept all" cookies if it appears
        try:
            await page.click('button:has-text("Accept all")', timeout=2000)
        except:
            pass

        await page.wait_for_timeout(2000)

        # Take a screenshot of what we see
        await page.screenshot(path="quest_view.png")

        # Look for quest details
        quest_title = await page.inner_text('h1') if await page.query_selector('h1') else "No H1"
        print(f"Title found: {quest_title}")

        # Look for description
        content = await page.content()
        with open("quest_full_content.html", "w") as f:
            f.write(content)

        # Try to find specific social task indicators
        twitter_icons = await page.query_selector_all('svg')
        print(f"Number of SVGs: {len(twitter_icons)}")

        # Check for specific text
        texts = ["Twitter", "Reply", "Post", "Retweet", "Like", "Follow"]
        for text in texts:
            found = await page.get_by_text(text, exact=False).count()
            print(f"Found '{text}': {found} times")

        await browser.close()

asyncio.run(run())
