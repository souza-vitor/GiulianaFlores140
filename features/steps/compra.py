from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'clico no banner')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "div.swiper-slide.swiper-slide-active a").click()


@when(u'preencho o campo endereco')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "li[class='opt-cep-container optCepDesk'] div span").click()
    context.driver.find_element(By.ID, "inputSearchAddress").send_keys("06149-110")
    context.driver.find_element(By.CSS_SELECTOR, ".itemAddress").click()
    context.driver.find_element(By.CSS_SELECTOR, ".apply-button").click()


@when(u'seleciono o produto')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "img[alt='Namorados']").click()
    context.driver.find_element(By.CSS_SELECTOR, ".item:nth-child(1) .image-content").click()
    context.driver.find_element(By.ID, "ContentSite_lbtBuy").click()
    

@then(u'confirmo uma data de entrega')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "body > form:nth-child(8) > div:nth-child(13) > main:nth-child(5) > div:nth-child(10) > div:nth-child(1) > div:nth-child(2) > div:nth-child(11) > div:nth-child(5) > div:nth-child(6) > div:nth-child(1) > ul:nth-child(3) > li:nth-child(5) > span:nth-child(2) > strong:nth-child(1)").click()
    context.driver.find_element(By.ID, "btConfirmShippingData").click()


@then(u'checo o carrinho de compras')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".titulo-dept.title-defaut-interna").text == "MEU CARRINHO"
    assert context.driver.find_element(By.ID, "ContentSite_Basketcontrol1_rptBasket_rptBasketItems_0_nuQty_0").get_attribute("value") == "1"
    context.driver.quit()
    


