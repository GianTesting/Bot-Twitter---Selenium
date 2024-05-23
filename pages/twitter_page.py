from selenium.webdriver.common.by import By
from .usuarios_actions import UsuariosActions

class TwitterPage(UsuariosActions):
    # Todos los elementos necesarios para la automatizar el inicio de sesión y el bloqueo.
    USERNAME_INPUT = (By.NAME, "text")
    PASSWORD_INPUT = (By.NAME, "password")
    MORE_OPTIONS_BUTTON = (By.CSS_SELECTOR, '[data-testid="userActions"]')
    BLOCK_OPTION = (By.CSS_SELECTOR, '[data-testid="block"]')
    BLOQUEAR_BOTON = (By.XPATH, '//span[text()="Bloquear"]')


    def navigate_to_login_page(self):
        self.navigate_to("https://twitter.com/i/flow/login")

    def block_user(self, user_profile_url):
        self.navigate_to(user_profile_url)
        self.click(self.MORE_OPTIONS_BUTTON)
        self.click(self.BLOCK_OPTION)
        self.click(self.BLOQUEAR_BOTON)

        