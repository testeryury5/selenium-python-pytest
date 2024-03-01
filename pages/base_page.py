class BasePage():

    def verify_page_title(self):
        assert self.browser.title == self.TITLE