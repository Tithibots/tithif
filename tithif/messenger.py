__all__ = ['']

from .fbobject import FBObject

class Messenger(FBObject):

    def __init__(self, browser=None):
        super().__init__(browser)


    def open_chat_to_fb_numeric_id(self, number):
        self._open_messenger_if_not_opened()
        self.browser.get(f'https://www.facebook.com/messages/t/{number}')


    def _open_messenger_if_not_opened(self):
        if self.browser.current_url.find("www.facebook.com/messages") == -1:
            self.browser.get("https://www.facebook.com/messages")