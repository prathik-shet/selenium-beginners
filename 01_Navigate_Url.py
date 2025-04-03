"""
Learn to navigate to a URL using Selenium and Pytest

AUTHOR: Avinash Shetty (Modified for Pytest)
"""

import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    """Setup WebDriver and close after test"""
    driver = webdriver.Firefox()
    yield driver  # This will return the driver instance to the test function
    driver.quit()  # Cleanup after the test

def test_qxf2_navigation(browser):
    """Test to check if Qxf2 tutorial page opens correctly"""
    url = "http://qxf2.com/selenium-tutorial-main"
    expected_title = "Qxf2 Services: Selenium training main"

    browser.get(url)
    assert browser.title == expected_title, "Page title does not match!"

