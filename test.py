from browsers import chrome_mocking_mobile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.gouzhang import Goushang

driver = chrome_mocking_mobile.get_driver()

gouzhang = Goushang(driver)

gouzhang.start()

print(123)

driver.quit()

