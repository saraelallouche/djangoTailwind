from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By


class TestBlog(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get("http://127.0.0.1:8000/crud")

        # Request page for the Post list
        alert = self.browser.find_element(By.CLASS_NAME, "container")
        self.assertEquals(alert.find_element(By.TAG_NAME, "h2").text, "Blog List")

    def test_click_on_author_name_directs_to_post_details(self):
        self.browser.get("http://127.0.0.1:8000/crud")

        add_url = "http://127.0.0.1:8000/crud/post/1/"
        self.browser.find_element(By.TAG_NAME, "a").click()
        self.assertEquals(self.browser.current_url, add_url)
