__all__ = ['']

from .fbobject import FBObject

class Messenger(FBObject):

    def __init__(self, browser=None):
        super().__init__(browser)

    def open_chat_to_fb_numeric_id_or_username(self, numberorusername):
        self._open_messenger_if_not_opened()
        self.browser.get(f'https://www.facebook.com/messages/t/{numberorusername}')


    def _open_messenger_if_not_opened(self):
        if self.browser.current_url.find("www.facebook.com/messages") == -1:
            self.browser.get("https://www.facebook.com/messages")

    def open_chat_to_profile_url(self, url):
        url=''
        if url.find('?id=') == -1:
            0
        else:
            0

        #https://www.facebook.com/profile.php?id=100003803338568&sk=about
        #https://www.facebook.com/navpreetdevpuri/