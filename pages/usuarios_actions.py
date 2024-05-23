from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UsuariosActions():
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def type_text_and_enter(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text + Keys.RETURN)


