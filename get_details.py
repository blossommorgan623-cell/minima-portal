import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        url = "https://zealy.io/cw/travala/questboard/353b17d0-2884-425a-a3a4-c4659e0dac36/f79f9585-44bd-4e7f-8705-96f534ba16dc"
        await page.goto(url)
        await page.wait_for_timeout(5000)

        try:
            await page.click('button:has-text("Accept all")', timeout=2000)
        except:
            pass
        await page.wait_for_timeout(2000)

        # Take screenshot of the board
        await page.screenshot(path="board_view.png")

        # Try to find the quest card and its text
        quest_card = page.locator('div:has-text("The Final Quest")').last
        if await quest_card.count() > 0:
            text = await quest_card.inner_text()
            print("Quest Card Text:")
            print(text)

            # Try to click it to see if a modal opens with more details
            try:
                await quest_card.click()
                await page.wait_for_timeout(3000)
                await page.screenshot(path="quest_modal.png")
                modal_text = await page.locator('div[role="dialog"]').inner_text()
                print("\nModal Text:")
                print(modal_text)
            except Exception as e:
                print(f"\nCould not click or read modal: {e}")
        else:
            print("Quest card not found by text.")

        await browser.close()

asyncio.run(run())
