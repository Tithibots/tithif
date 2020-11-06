__all__ = ['']

from .fbobject import FBObject

class Messenger(FBObject):

    def __init__(self, browser=None):
        super().__init__(browser)


    def open_chat_to(self, nameorusername):
        self._open_messenger_if_not_opened()


    def _open_messenger_if_not_opened(self):
        if self.browser.current_url.find("www.facebook.com/messages") == -1:
            self.browser.get("https://www.facebook.com/messages")
            self.browser.get("https://www.facebook.com/messages")