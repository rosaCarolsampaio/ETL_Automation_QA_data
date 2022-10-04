"""
This module contains step definitions for prototype.feature.
"""

from operator import imod
import string
from tokenize import Number
from traceback import extract_stack
import pytest
import papermill as pm
from functools import partial
from pytest import mark
# from pytest_bdd import (
#     given,
#     then,
#     when,
#     scenarios,
#     parsers,
#     scenario,
# ) 
from behave import given, when, then


# # Scenario
# scenarios('../features/prototype.feature')

# @scenario('../features/prototype.feature',"Basic validatioon of null values per fields")


# @pytest.mark.filterwarnings("error")
# @given(parsers.cfparse('I connect the database "{database}"'))
@given(u'I connect the database "{database}"')
def i_connect_the_database(context, database):
    pm.execute_notebook(
        './notebooks/connection.ipynb',
        './reports/connection_report.ipynb',
        kernel_name="python3",
        parameters={'db':database},
        log_output=True,
    ) 


# @when('check if have any null values in the "items"')
# def check_if_have_any_null_values_in_the_items():
#     """check if have any null values in the "items"."""
#     raise NotImplementedError



# @then('the result is showin and should not have any null values')
# def the_result_is_showin_and_should_not_have_any_null_values():
#     """the result is showin and should not have any null values."""
#     raise NotImplementedError
















# Fixtures
 
# @pytest.fixture
# def browser():
#     b = webdriver.Firefox()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()
 
# # Given Steps
 
# @given('the DuckDuckGo home page is displayed')
# def ddg_home(browser):
#     browser.get(DUCKDUCKGO_HOME)
 
# # When Steps
 
# @when(parsers.parse('the user searches for "{phrase}"'))
# def search_phrase(browser, phrase):
#     search_input = browser.find_element_by_id('search_form_input_homepage')
#     search_input.send_keys(phrase + Keys.RETURN)
 
# # Then Steps
 
# @then(parsers.parse('results are shown for "{phrase}"'))
# def search_results(browser, phrase):
#     # Check search result list
#     # (A more comprehensive test would check results for matching phrases)
#     # (Check the list before the search phrase for correct implicit waiting)
#     links_div = browser.find_element_by_id('links')
#     assert len(links_div.find_elements_by_xpath('//div')) > 0
#     # Check search phrase
#     search_input = browser.find_element_by_id('search_form_input')
#     assert search_input.get_attribute('value') == phrase