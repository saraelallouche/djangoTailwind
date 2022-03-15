from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestBlog(StaticLiveServerTestCase):
    @classmethod
    def setUp(cls):
        super().setUpClass()

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        # options.add_argument('--headless')

        cls.browser = webdriver.Chrome(
            chrome_options=options, executable_path=ChromeDriverManager().install()
        )

    @classmethod
    def tearDown(cls):
        cls.browser.quit()

    def test_login_element(self):

        username = "test"
        password = "test123"

        print(self.live_server_url)

        # opening the website
        self.browser.get("http://127.0.0.1:8000/crud")
        wait = WebDriverWait(self.browser, 20)
        self.browser.find_element(By.ID, "to_log_in").click()

        # doing the login
        self.browser.find_element(By.ID, "inputUsername").send_keys(username)
        self.browser.find_element(By.ID, "inputPassword").send_keys(password)
        self.browser.find_element(By.ID, "login_button").click()

        # post add button
        self.browser.find_element(By.ID, "post_add").click()

        # adding a post
        self.browser.find_element(By.ID, "title").send_keys("sometext")
        self.browser.find_element(By.ID, "body").send_keys("this is body")
        self.browser.find_element(By.ID, "submit_add_post").click()

        # Button to go to Detail view
        self.browser.find_element(By.ID, "post_detail").click()
        self.browser.execute_script("window.history.go(-1)")

        # Button to go to Edit view
        self.browser.find_element(By.ID, "post_edit").click()

        # Editing a post
        self.browser.find_element(By.ID, "title").send_keys("change title")
        self.browser.find_element(By.ID, "body").send_keys("you can edit")
        self.browser.find_element(By.ID, "submit_edit_post").click()

        # Button to go to Delete view
        self.browser.find_element(By.ID, "post_delete").click()

        # Delete button
        self.browser.find_element(By.ID, "submit_delete_post").click()

        # Logout button
        self.browser.find_element(By.ID, "logout").click()
        self.browser.delete_all_cookies()
