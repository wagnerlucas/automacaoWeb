import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Vagno\PycharmProjects\automacaoWeb\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_cadastro_de_novo_usuario_com_sucesso(self):
        driver = self.driver
        driver.get("https://testingandplay.com/example/form")
        self.driver.implicitly_wait(20)

        email = driver.find_element_by_xpath("//input[@name='email']")
        email.send_keys("wagnerlucas.smr@gmail.com")

        autocomplete = driver.find_element_by_xpath("//input[@id='typeahead-basic']")
        autocomplete.send_keys("Alab")

        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ngb-typeahead-0-0']")))

        city = driver.find_element_by_xpath("//button[@id='ngb-typeahead-0-0']")
        city.click()

        select = driver.find_element_by_xpath("//select[@id='select-input']")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            if option.text == '2':
                option.click()

        text_area = driver.find_element_by_xpath("//textarea[@id='textarea-input']")
        text_area.send_keys("Lorem ipsum dolor sit amet")

        file_input = driver.find_element_by_xpath("//input[@id='file-input']")
        file_input.send_keys("C:\\Users\\Vagno\\Documents\\Lucas\\ambev_engenharia_logo.png")

        password = driver.find_element_by_xpath("//input[@placeholder='Senha']")
        password.send_keys("12345678")

        radio = driver.find_element_by_xpath("//input[@id='radios2-input']")
        radio.click()

        check = driver.find_element_by_xpath("//input[@id='check-input']")
        check.click()

        button = driver.find_element_by_xpath("//button[@id='submit-input']")
        button.click()

        self.assertIn("Sucesso",
                      driver.find_element_by_xpath("//ngb-alert[@class='alert alert-success alert-dismissible']").text)

    def test_cadastro_de_novo_usuario_campos_vazios(self):
        driver = self.driver
        driver.get("https://testingandplay.com/example/form")
        self.driver.implicitly_wait(10)

        button = driver.find_element_by_xpath("//button[@id='submit-input']")
        button.click()

        self.assertIn("Formulário inválido",
                      driver.find_element_by_xpath("//ngb-alert[@class='alert alert-danger alert-dismissible']").text)

    def test_cadastro_de_novo_usuario_email_invalido(self):
        driver = self.driver
        driver.get("https://testingandplay.com/example/form")
        self.driver.implicitly_wait(20)

        email = driver.find_element_by_xpath("//input[@name='email']")
        email.send_keys("wag")

        invalid_email_message = driver.find_element_by_xpath("//div[@class='invalid-feedback']")

        autocomplete = driver.find_element_by_xpath("//input[@id='typeahead-basic']")
        autocomplete.send_keys("Alab")

        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='ngb-typeahead-0-0']")))

        city = driver.find_element_by_xpath("//button[@id='ngb-typeahead-0-0']")
        city.click()

        select = driver.find_element_by_xpath("//select[@id='select-input']")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            if option.text == '2':
                option.click()

        text_area = driver.find_element_by_xpath("//textarea[@id='textarea-input']")
        text_area.send_keys("Lorem ipsum dolor sit amet")

        file_input = driver.find_element_by_xpath("//input[@id='file-input']")
        file_input.send_keys("C:\\Users\\Vagno\\Documents\\Lucas\\ambev_engenharia_logo.png")

        password = driver.find_element_by_xpath("//input[@placeholder='Senha']")
        password.send_keys("12345678")

        radio = driver.find_element_by_xpath("//input[@id='radios2-input']")
        radio.click()

        check = driver.find_element_by_xpath("//input[@id='check-input']")
        check.click()

        button = driver.find_element_by_xpath("//button[@id='submit-input']")
        button.click()

        self.assertIn("Formulário inválido",
                      driver.find_element_by_xpath("//ngb-alert[@class='alert alert-danger alert-dismissible']").text)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
