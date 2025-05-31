import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCriarusuario():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_criar_usuario(self):
    self.driver.get("https://www.giulianaflores.com.br")
    self.driver.set_window_size(1656, 804)
    self.driver.find_element(By.ID, "perfil-hidden").click()
    self.driver.find_element(By.CSS_SELECTOR, "a[href='https://www.giulianaflores.com.br/login.aspx']").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "IDENTIFICAÇÃO"
    assert self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").text == "Criar cadastro"
    self.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "body > form:nth-child(8) > div:nth-child(14) > main:nth-child(5) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(2)").text == "MEU CADASTRO"
    self.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Liz Jéssica Alana Barbosa")
    self.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("152.860.837-22")
    self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("liz-barbosa92@advogadostb.com.br")
    self.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("NadaAuto140!")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("08450-000")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("615")
    self.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("61995473880")
    assert self.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").get_attribute("value") == "Finalizar Cadastro"
  
