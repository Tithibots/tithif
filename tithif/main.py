__all__ = ["Tithiwa"]

from .session import Session
from .messenger import Messenger

class Tithiwa(Session, Messenger):
    def __init__(self, browser=None):
        super().__init__(browser)

    # def __del__(self):
    #     self.browser.quit()