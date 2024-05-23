from selenium.webdriver.common.by import By
from .usuarios_actions import UsuariosActions
from selenium.common.exceptions import NoSuchElementException


class TwitterPage(UsuariosActions):
    # Todos los elementos necesarios para la automatizar el inicio de sesión y el bloqueo.
    USERNAME_INPUT = (By.NAME, "text")

    PASSWORD_INPUT = (By.NAME, "password")

    MORE_OPTIONS_BUTTON = (By.CSS_SELECTOR, '[data-testid="userActions"]')

    BLOCK_OPTION = (By.XPATH, '//span[contains(text(), "Bloquear a @")]')
    UNBLOCK_OPTION = (By.XPATH, '//span[contains(text(), "Desbloquear a @")]')

    BLOQUEAR_BOTON = (By.XPATH, '//button[@data-testid="confirmationSheetConfirm"]//span[text()="Bloquear"]')



    def navigate_to_login_page(self):
        self.navigate_to("https://twitter.com/i/flow/login")

        
    def block_user(self, user_profile_url):
        self.navigate_to(user_profile_url)
        self.click(self.MORE_OPTIONS_BUTTON)
        
        # Verificar si el botón de desbloqueo está presente
        if self.is_element_clickable(self.UNBLOCK_OPTION):
            # Si el botón de desbloqueo está presente, la cuenta ya está bloqueada, no hacer nada
            return
        else:
            # Si el botón de desbloqueo no está presente, bloquear la cuenta
            self.click(self.BLOCK_OPTION)
            self.click(self.BLOQUEAR_BOTON)