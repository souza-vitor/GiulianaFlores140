import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogarusuario():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_falha_autenticar_usuario(self):
    self.driver.get("https://www.giulianaflores.com.br")
    self.driver.set_window_size(1656, 804)
    self.driver.find_element(By.ID, "perfil-hidden").click()
    self.driver.find_element(By.CSS_SELECTOR, "a[href='https://www.giulianaflores.com.br/login.aspx']").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "IDENTIFICAÇÃO"
    assert self.driver.find_element(By.CSS_SELECTOR, ".txt_newlogin").text == "Olá, digite seus dados:"
    self.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("liz-barbosa92@advogadostb.com.br")
    self.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("NadaAuto140!")
    self.driver.find_element(By.ID, "ContentSite_ibtContinue").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "span[class='aviso-erro'] strong").text == "ATENÇÃO"