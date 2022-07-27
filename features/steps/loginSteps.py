from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when('I open Orange HRM homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@when('Enter username "{user}" and password "{pwd}"')
def enterCredentials(context, user, pwd):
    context.driver.find_element(By.ID, "txtUsername").send_keys(user)
    context.driver.find_element(By.ID, "txtPassword").send_keys(pwd)

@when('Click on Login button')
def clickLogin(context):
    context.driver.find_element(By.ID, "btnLogin").click()

@then('User must successfully login to the Dashboard page')
def verifyDashboard(context):
    try:
        text = context.driver.find_element(By.XPATH, "//h1[normalize-space()='Dashboard']").text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"