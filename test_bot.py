import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.twitter_page import TwitterPage
import time

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_block_accounts(browser):
    # Acá es donde tenés que poner tus datos
    username = "ACAESCRIBIRUSUARIO"
    password = "ACAESCRIBIRCONTRASEÑA"
    
    # Inicializo twitter_page_actions
    twitter_page_actions = TwitterPage(browser)
    
    twitter_page_actions.navigate_to_login_page()
    
    twitter_page_actions.type_text(twitter_page_actions.USERNAME_INPUT, username)

    twitter_page_actions.type_text(twitter_page_actions.PASSWORD_INPUT, password)

    time.sleep(5)

    #Acá cambiar la ruta por la tuya donde tenés guardado el csv.
    with open(r'C:\Users\gian_\Desktop\Twitter\Cuentas\CuentasTwitter.csv', newline='') as csvfile:
        for account_url in csvfile:
            twitter_page_actions.block_user(account_url.strip())
            