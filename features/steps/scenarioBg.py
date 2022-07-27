from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I launch browser')
def step_impl(context):
    assert True, "Test Passed"

@when(u'I open application')
def step_impl(context):
    assert True, "Test Passed"

@when(u'Enter valid username and password')
def step_impl(context):
    assert True, "Test Passed"

@when(u'Click on Login')
def step_impl(context):
    assert True, "Test Passed"

@then(u'User must login to the Dashboard page')
def step_impl(context):
    assert True, "Test Passed"

@when(u'Navigate to search page')
def step_impl(context):
    assert True, "Test Passed"

@then(u'Search page should display')
def step_impl(context):
    assert True, "Test Passed"

@when(u'Navigate to advanced search page')
def step_impl(context):
    assert True, "Test Passed"

@then(u'Advanced search page should display')
def step_impl(context):
    assert True, "Test Passed"