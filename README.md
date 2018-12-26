steamwintersale18
======
Bless Python script for [https://store.steampowered.com/promotion/cottage_2018/](https://store.steampowered.com/promotion/cottage_2018/)

**Only for personal use.**


Feature
------
Open cottage door only.
Will `NOT` explore queue. use ArchiSteamFarm instead.


Usage
------
Example for `Chrome` browser:
1. *Login and logout.*
2. Login *again with `Remember me on this computer` checked* and open the `Network` page.
3. Refresh and you'll get a list of requests.
4. Select `Filter -> Doc`.
5. Click the `cottage-2018/` usually the first one in the list.
6. At the right panel select `Headers -> RequestHeaders -> Cookie`.
7. Copy it and paste in the `mybotname.txt` file you created.
8. *To add a another account, open `Application` page in `DevTools`, and clear cookies instead of logout. (Logout will let your previous work wasted.*

*The italic words above are optional.*


Result
------
Example config file: `mybotname.txt`
```text
browserid=##########; steamLoginSecure=##########; sessionid=##########; steamMachineAuth##########=##########; steamRememberLogin=##########
```

**Please note that `steamRememberLogin` part is optional.**


Needs?
------
**python3** and **requests**

* https://www.python.org/downloads/
* pip install requests

> Don't forget to setup your PATH environment variable...