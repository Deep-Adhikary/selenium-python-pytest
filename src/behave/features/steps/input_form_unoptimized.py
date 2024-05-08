import sys
import os

sys.path.append(os.path.abspath(__file__))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from behave import *



@given(u'user is in LambdaTest Selenium Playground Page')
def user_is_in_lambda_test_selenium_page(context):
    context.driver.get("https://www.lambdatest.com/selenium-playground/")


@given(u'user has navigated to the form demo Page')
def step_impl(context):
    wait: WebDriverWait = context.wait
    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Input Form Submit'))).click()


@when(u'user enters name "{name}"')
def step_impl(context, name):
    wait: WebDriverWait = context.wait
    wait.until(EC.presence_of_element_located((By.ID, 'name'))).send_keys(name)


@when(u'user enters email "{email}"')
def step_impl(context, email):
    context.wait.until(EC.presence_of_element_located(
        (By.ID, 'inputEmail4'))).send_keys(email)


@when(u'user enters password "{passwd}"')
def step_impl(context, passwd):
    context.wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '* [name="password"]'))).send_keys(passwd)


@when(u'user enters company "{company_name}"')
def step_impl(context, company_name):
    context.wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@name="company"]'))).send_keys(company_name)


@when(u'user enters website "{website}"')
def step_impl(context, website):
    context.wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@for="inputWebsite"]/following-sibling::input'))).send_keys(website)


@when(u'user selects country as "{country}"')
def step_impl(context, country):
    select.Select(
        context.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[.="Country*"]/following-sibling::select')))).select_by_visible_text(country)


@when(u'user enters city as "{city}"')
def step_impl(context, city):
    context.wait.until(EC.visibility_of_element_located(
        (By.NAME, 'city'))).send_keys(city)


@when(u'user enters address line 1 as "{address}"')
def step_impl(context, address):
    context.wait.until(EC.visibility_of_element_located(
        (By.NAME, 'address_line1'))).send_keys(address)


@when(u'user enters address line 2 as "{address}"')
def step_impl(context, address):
    context.wait.until(EC.visibility_of_element_located(
        (By.NAME, 'address_line2'))).send_keys(address)


@when(u'user enter state as "{state}"')
def step_impl(context, state):
    context.wait.until(EC.visibility_of_element_located(
        (By.ID, 'inputState'))).send_keys(state)


@when(u'user enters zip code as "{zip}"')
def step_impl(context, zip):
    context.wait.until(EC.visibility_of_element_located(
        (By.ID, 'inputZip'))).send_keys(zip)


@when(u'user clicks on submit button')
def step_impl(context):
    context.wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, '.loginform button'))).click()


@then(u'Form should be submitted')
def step_impl(context):
    element = context.driver.find_element(By.CSS_SELECTOR, '.loginform button')
    assert element.is_displayed() == False


@then(u'success message "{successmsg}" is displayed')
def step_impl(context, successmsg):
    assert context.wait.until(EC.presence_of_element_located(
        (By.XPATH, f'//*[.="{successmsg}"]'))).is_displayed() == True


@when(u'user enters personal informations')
def step_impl(context):
    objDict = {row['Field']: row['Value'] for row in context.table}
    context.input_form_action.enter_personal_info(
        objDict['name'], objDict['email'], objDict['password'], objDict['company'], objDict['website'])


@when(u'user enters address informations')
def step_impl(context):
    objDict = {row['Field']: row['Value'] for row in context.table}
    context.input_form_action.enter_address_info(
        objDict['country'], objDict['city'], objDict['address line 1'], objDict['address line 2'], objDict['state'], objDict['zip'])
