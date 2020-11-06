__all__ = ["FBObject"]

from selenium import webdriver
from .constants import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FBObject:
    def __init__(self, browser=None):
        self.browser = browser
        self.browser = self._open_browser_if_not_opened()
        self._open_facebook_if_not_opened()

    def quit(self, _shouldoutput=(True, True)):
        if _shouldoutput[0] and DEFAULT_SHOULD_OUTPUT:
            print(f'Quiting tithif', end="...")
        self.browser.quit()
        if _shouldoutput[1] and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')


    def _open_browser_if_not_opened(self):
        if self.browser == None:
            self.browser = webdriver.Chrome()
        return self.browser

    def _open_facebook_if_not_opened(self):
        if self.browser.current_url.find("facebook") == -1:
            self.browser.get("https://www.facebook.com/")

    def _wait_for_presence_of_an_element(self, selector):
        element = None
        try:
            element = WebDriverWait(self.browser, INTEGERS.DEFAULT_WAIT).until(
                EC.presence_of_element_located(selector)
            )
        except:
            pass
        finally:
            return element

    def _wait_for_presence_of_all_elements(self, selector):
        elements = None
        try:
            elements = WebDriverWait(self.browser, INTEGERS.DEFAULT_WAIT).until(
                EC.presence_of_all_elements_located(selector)
            )
        except:
            pass
        finally:
            return elements

    def _wait_for_presence_of_an_element_in_other_element(self, selector, element):
        relement = None
        while True:
            try:
                relement = element.find_element(*selector)
            except:
                pass
            finally:
                return relement

    def _wait_for_an_element_to_be_clickable(self, selector):
        element = None
        try:
            element = WebDriverWait(self.browser, INTEGERS.DEFAULT_WAIT).until(
                EC.element_to_be_clickable(selector)
            )
        except:
            pass
        finally:
            return element

    def _wait_for_an_element_to_deattached(self, element):
        while True:
            try:
                element.is_displayed()
            except:
                break
            finally:
                pass

    def _race_for_presence_of_two_elements(self, selector1, selector2):
        selector1orselector2 = selector1 + ", " + selector2
        winnerelement = self._wait_for_presence_of_an_element(selector1orselector2)
        element1 = None
        try:
            element1 = self.browser.find_element(*selector1)
        except:
            pass
        element2 = None
        try:
            element2 = self.browser.find_element(*selector2)
        except:
            pass
        if winnerelement == element1:
            return winnerelement, 0
        elif winnerelement == element2:
            return winnerelement, 1
        else:
            return None, -1
