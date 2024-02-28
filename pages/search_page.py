class SearchPage:

    def __init__(self, browser):
        self.browser = browser


    URL = "https://www.ebay.com/sch/i.html"
    TITLE = "Tiffany for sale | eBay"

    # Element Locators


    # Methods
    def verify_title(self):
        assert self.browser.title == self.TITLE
