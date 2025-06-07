from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given(u'que acesso o site Giuliana Flores')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.giulianaflores.com.br")


@given(u'clico em perfil')
def step_impl(context):
    context.driver.find_element(By.ID, "perfil-hidden").click()
    context.driver.find_element(By.CSS_SELECTOR, "a[href='https://www.giulianaflores.com.br/login.aspx']").click()


@when(u'sou redirecionado para a pagina de identificacao')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".titulo-dept").text == "IDENTIFICAÇÃO"


@when(u'clico em Criar Cadastro')
def step_impl(context):
    assert context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").text == "Criar cadastro"
    context.driver.find_element(By.ID, "ContentSite_ibtNewCustomer").click()


@then(u'sou redirecionado para a pagina de Cadastro')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "body > form:nth-child(8) > div:nth-child(14) > main:nth-child(5) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > h2:nth-child(2)").text == "MEU CADASTRO"


@then(u'preencho os campos de nome, cpf, e-mail, senha e endereco')
def step_impl(context):
    context.driver.find_element(By.ID, "ContentSite_txtName").send_keys("Liz Jéssica Alana Barbosa")
    context.driver.find_element(By.ID, "ContentSite_txtCpf").send_keys("152.860.837-22")
    context.driver.find_element(By.ID, "ContentSite_txtEmail").send_keys("liz-barbosa92@advogadostb.com.br")
    context.driver.find_element(By.ID, "ContentSite_txtPasswordNew").send_keys("NadaAuto140!")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtZip").send_keys("08450-000")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtAddressNumber").send_keys("615")
    context.driver.find_element(By.ID, "ContentSite_CustomerAddress_txtPhoneCelularNum").send_keys("61995473880")


@then(u'verifico o botao de finalizar cadastro')
def step_impl(context):
    assert context.driver.find_element(By.ID, "ContentSite_btnCreateCustomer").get_attribute("value") == "Finalizar Cadastro"
    context.driver.quit()


    