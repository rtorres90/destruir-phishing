from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Goushang():
    page_url = "https://cl.gouzhang.top/slot"
    first_button_xpath = "//a[text()='Programa tu entrega']"
    email_xpath = "//input[@id='emlInput']"
    nombre_xpath = "//input[@id='txtNombre']"
    apellido_xpath = "//input[@id='txtApellido']"
    celular_xpath = "//input[@id='txtCelular']"
    comuna_xpath = "//input[@id='txtComuna']"
    ciudad_xpath = "//input[@name='city']"
    codigo_postal_xpath = "//input[@name='zip']"
    calle_xpath = "//input[@id='txtCalle']"
    numero_calle_xpath = "//input[@name='street_1']"

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, timeout=60)

    def start(self):
        self.driver.get(self.page_url)
        self.wait_for_page_load()
        self.driver.find_element(By.XPATH, self.first_button_xpath).click()


    def wait_for_page_load(self):
        button = self.wait.until(EC.presence_of_element_located((By.XPATH, self.first_button_xpath)))
        self.wait.until(EC.visibility_of(button))