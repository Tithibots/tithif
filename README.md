<img src="./logo/tithif.png" alt="logo" width="233"/>

# tithif

Automate the Facebook website with selenium in python.

Full explained Videos on that project are coming soon. Stay tune with our youtube channel [Noobie Techs](https://www.youtube.com/c/NoobieTechsTithi_mukherjee/)

Table of contents
  * [Contribution and creativity points](#contribution)
  * [Automation ideas](#automation-ideas)
  * [Installation](#installation)
  
## Contribution and creativity points
Selenium automation creativity points 
1. **Debugging** [Example](https://github.com/Tithibots/tithiwa/issues/50#issuecomment-710778130)<br> We can create breakpoints to pause execution at any time then we can try to run some python code in the console to find a way to do something. That helps to develop efficiently.  
2. **CTRL + Left mouse click** [Example](https://github.com/Tithibots/tithiwa/issues/50#issuecomment-710779007)<br> We can see the definitions or references or usages of any function or variable in our IDE like PyCharm. That helps to understand the existing code base efficiently.
3. **Inspect elements and console** [Example](https://github.com/Tithibots/tithiwa/issues/50#issuecomment-710781167)<br> In chrome, we can inspect HTML elements and run javascript code inside console. That helps up to find better selectors and automations steps efficiently.

NOTE: By pressing UP key we can see the history about what codes we had run during Python debugging and inside Chrome's console.<br> 
NOTE: If you are running javascript code inside selenium chromedriver's console then it will **NOT** keep history.<br>
Good luck :)
  
## Automation ideas

* ✔ `generate_session(sessionfilename)`: To generate session files with extension `.fb` 
* ✔ `open_session(sessionfilename)`: To open session files with extension `.fb`
* `open_chat_to_fb_numeric_id(number)`: To open chatroom to someone by using facebook numeric id.
* `open_chat_to_username(username)`: To open chatroom to someone by username
* `open_chat_to_profile_url(url)`: To open chat to someone from profile url
* `send_message_to_currently_opened_chat(message)`: To Send message to currently opened chatroom
* `send_message_to(nameorusername, message)`: To send message to someone
* `scrape_likes_from_first_n_posts(url)`: To scrape likes of posts of someone  
* `track_online_status(url)`: To track online status for someone and save the data in a file 
* `create_3_days_online_status_wallpaper_from_url(url)`: to show an image visually showing online status for 3-days
* `create_3_days_online_status_wallpaper_from_file(url)`: to show an image visually showing online status for 3-days
* ``

