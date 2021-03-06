import os

from selenium.webdriver.common.by import By

MODULEDIR = os.path.dirname(__file__)
OUTPUT_FOLDER_NAME = "output"
OUTPUT_FOLDER_DIR = os.path.join(MODULEDIR, OUTPUT_FOLDER_NAME)
SESSIONDIR = os.path.join(OUTPUT_FOLDER_DIR, 'sessions')
DEFAULT_SHOULD_OUTPUT = True


class SELECTORS(object):
    MESSENGER__SEARCHBOX = (By.CSS_SELECTOR, '')


class INTEGERS(object):
    TURN_OFF_NOTIFICATIONS_FOR_8_HOURS = 0
    TURN_OFF_NOTIFICATIONS_FOR_1_WEEK = 1
    TURN_OFF_NOTIFICATIONS_FOR_ALWAYS = 2
    DEFAULT_WAIT = 89


class STRINGS(object):
    CHECK_CHAR = '✔'
    CROSS_CHAR = '❌'
