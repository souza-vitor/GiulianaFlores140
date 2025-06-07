from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@when(u'preencho o campo e-mail e senha')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".txt_newlogin").text == "Olá, digite seus dados:"
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("nashton.braxley@dsitip.com")
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("SempreAuto10!")
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()


@then(u'sou redirecionado para a pagina principal e faço logout')
def step_impl(context):
    context.driver.find_element(By.ID, "perfil-hidden").click()
    context.driver.find_element(By.CSS_SELECTOR, "a[href='javascript:Logout();void 0;']").click()

# login com senha invalida

@when(u'preencho errado o campo e-mail e senha')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("liz-barbosa92@advogadostb.com.br")
    context.driver.find_element(By.ID, "ContentSite_txtPassword").send_keys("NadaAuto140!")
    context.driver.find_element(By.ID, "ContentSite_ibtContinue").click()


@then(u'recebo um aviso de erro no login')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "span[class='aviso-erro'] strong").text == "ATENÇÃO"
    context.driver.quit()