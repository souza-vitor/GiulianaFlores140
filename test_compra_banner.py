import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestComprausuario():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_compra_banner(self):
    self.driver.get("https://www.giulianaflores.com.br")
    self.driver.set_window_size(1800, 1024)
    self.driver.find_element(By.CSS_SELECTOR, "div.swiper-slide.swiper-slide-active a").click()

    assert self.driver.find_element(By.CSS_SELECTOR, ".opt-popup-title").text == "Para onde deseja enviar?"
    self.driver.find_element(By.ID, "inputSearchAddress").send_keys("06149-110")
    self.driver.find_element(By.CSS_SELECTOR, ".itemAddress").click()
    self.driver.find_element(By.CSS_SELECTOR, ".apply-button").click()
    self.driver.find_element(By.CSS_SELECTOR, "body > form:nth-child(8) > div:nth-child(12) > main:nth-child(5) > div:nth-child(3) > div:nth-child(1) > section:nth-child(6) > section:nth-child(2) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(4) > li:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h2:nth-child(2)").click()
    self.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
    self.driver.find_element(By.CSS_SELECTOR, "body > form:nth-child(8) > div:nth-child(13) > main:nth-child(5) > div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(11) > div:nth-child(5) > div:nth-child(6) > div:nth-child(1) > ul:nth-child(3) > li:nth-child(5) > span:nth-child(2) > strong:nth-child(1)").click()
    self.driver.find_element(By.ID, "btConfirmShippingData").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".titulo-dept.title-defaut-interna").text == "MEU CARRINHO"
    assert self.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_rptBasketItems_0_nuQty_0").get_attribute("value") == "1"





