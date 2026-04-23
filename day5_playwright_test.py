from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) #opens real browser
        page = browser.new_page()

        page.goto("https://www.google.com")

    # Accept cookies if popup appears
    # try:
    #     page.click("button:has-text('Accept')")
    # except:
    #     pass



    #Search
        page.fill("textarea[name = 'q']", "Python Automation jobs")
        page.keyboard.press("Enter")

        print("Results found:", page.locator("a h3").count())

        #Wait for search results to load properly
        page.click("h3")

        #Click FIRST result specifically
        #page.locator("a h3").first.click()

        results = page.locator("a h3")

        if results.count() > 0:
            results.first.click()
        else:
            print("No results found - likely blocked or page not loaded")

        #Wait to see result
        page.wait_for_timeout(5000) #wait for 5 seconds to see the results

    
        print(page.title())

        browser.close()


test_google_search()

