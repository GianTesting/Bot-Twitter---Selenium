from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class UsuariosActions():
    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def is_element_clickable(self, locator, timeout=3):
        try:
            # Intentar esperar a que el elemento sea visible y habilitado para clic
            return self.wait_for_element(locator, timeout).is_enabled()
        except TimeoutException:
            # Si se lanza una excepción de tiempo de espera, devolver False
            return False
    
    def click(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def type_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text + Keys.RETURN)
