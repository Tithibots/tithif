__all__ = ["Session"]

from .constants import *
from .fbobject import FBObject
import os
import platform
import subprocess



class Session(FBObject):

    def __init__(self, sessiondir=None, browser=None):
        super().__init__(browser)
        self.sessiondir = sessiondir
        if sessiondir == None:
            self.sessiondir = SESSIONDIR

    def generate_session(self, sessionfilename=None, shouldclosebrowser=False,
                         shouldshowfilelocation=True, _shouldoutput=True):
        os.makedirs(self.sessiondir, exist_ok=True)
        if sessionfilename == None:
            sessionfilename = self._create_valid_session_file_name(self.sessiondir)
        else:
            sessionfilename = self._add_file_extension(sessionfilename)
        if _shouldoutput and DEFAULT_SHOULD_OUTPUT:
            print("Waiting for QR code scan", end="... ")
        cookies = self.browser.get_cookies()
        sessionfilelocation = os.path.realpath(os.path.join(self.sessiondir, sessionfilename))
        with open(sessionfilelocation, 'w',
                  encoding='utf-8') as sessionfile:
            sessionfile.write(str(cookies))
        if _shouldoutput and DEFAULT_SHOULD_OUTPUT:
            print('Your session file is saved to: ' + sessionfilelocation)
        if shouldshowfilelocation:
            self._show_file_location(self.sessiondir)
        if shouldclosebrowser:
            self.browser.quit()
        if _shouldoutput and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def open_session(self, sessionfilename=None, _shouldoutput=True):
        if sessionfilename == None:
            sessionfilename = self._get_last_created_session_file(self.sessiondir)
        else:
            sessionfilename = self._validate_session_file(sessionfilename, self.sessiondir)
        cookies = None
        with open(sessionfilename, "r", encoding="utf-8") as sessionfile:
            try:
                cookies = eval(sessionfile.read())
            except:
                raise IOError('"' + sessionfilename + '" is invalid file.')
        if _shouldoutput and DEFAULT_SHOULD_OUTPUT:
            print("Injecting session", end="... ")
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        self.browser.refresh()
        if _shouldoutput and DEFAULT_SHOULD_OUTPUT:
            print(f'{STRINGS.CHECK_CHAR} Done')

    def _add_file_extension(self, sessionfilename):
        return sessionfilename + ".fb" if sessionfilename[-3:] != ".fb" else sessionfilename

    def _create_valid_session_file_name(self, sessiondir):
        n = len(os.listdir(sessiondir))
        sessionfilename = "%02d" % n + ".fb"
        while os.path.exists(sessionfilename):
            n += 1
            sessionfilename = "%02d" % n + ".fb"
        sessionfilename = self._add_file_extension(sessionfilename)

        return sessionfilename

    def _get_last_created_session_file(self, sessiondir):
        if not os.path.exists(sessiondir):
            raise IOError('No session file is exists. Generate session file by using generate_session().')
        files = os.listdir(sessiondir)
        paths = [os.path.join(sessiondir, basename) for basename in files]
        sessionfilename = max(paths, key=os.path.getctime)
        if not os.path.exists(sessionfilename):
            raise IOError('No session file is exists. Generate session file by using generate_session().')
        return sessionfilename

    def _validate_session_file(self, sessionfilename, sessiondir):
        if sessionfilename[-3:] != ".fb":
            sessionfilename += ".fb"
        possible_paths = [
            os.path.join(sessiondir, sessionfilename), sessionfilename
        ]
        possibleSessionfilePath = None
        for path in possible_paths:
            if os.path.exists(path):
                possibleSessionfilePath = path
        if possibleSessionfilePath == None:
            raise IOError(
                f'Session file "{sessionfilename}" is not exist. Generate that session file by using generate_session(\'{sessionfilename}\')')
        return possibleSessionfilePath

    def _show_file_location(self, path):
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

# browser = generate_session("03")
# browser.quit()
# open_session("03")
# input("PRESS ENTER")
