import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        url = "https://zealy.io/cw/travala/questboard/353b17d0-2884-425a-a3a4-c4659e0dac36/f79f9585-44bd-4e7f-8705-96f534ba16dc"
        await page.goto(url)
        await page.wait_for_timeout(5000)

        # Look for the quest card
        quest_id = "f79f9585-44bd-4e7f-8705-96f534ba16dc"
        card = page.locator(f'div[id="{quest_id}"]')

        # Find all badges/icons within the card
        icons = card.locator('span[data-scope="Badge"]')
        count = await icons.count()
        print(f"Found {count} icons on the quest card.")

        for i in range(count):
            icon = icons.nth(i)
            # Try to get aria-label or title or hover and wait for tooltip
            aria_label = await icon.get_attribute("aria-label")
            print(f"Icon {i} aria-label: {aria_label}")

            # Try to hover and see if any new text appears in the body (tooltips often appended to body)
            await icon.hover()
            await page.wait_for_timeout(500)

        # After hovering all, let is check the whole body for task related words
        body_text = await page.inner_text("body")
        for word in ["Reply", "Like", "Retweet", "Follow", "Post"]:
            if word in body_text:
                print(f"Found word in body after hovers: {word}")

        await browser.close()

asyncio.run(run())
