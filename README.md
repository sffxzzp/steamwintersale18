steamwintersale18
======
Python script for personal use.

STILL UNDER DEVELOPMENT. THINK TWICE BEFORE YOU USE IT.

Feature
======
Open cottage door only.

Will `NOT` explore queue. use ArchiSteamFarm instead.

Usage
======
Use `Chrome -> DevTools -> Network` to get cookies, and directly save the raw cookies to `.txt` file `UNDER` configs folder.

The exact steps are:
1. Login and open the `Network` page.
2. Refresh and you'll get a list of requests.
3. Click the `cottage-2018/` usually the first one in the list, and the cookies is at the right panel that just shows up.
4. Copy it and paste in the `.txt` file you created.

What it should looks like in `"username.txt"`

    browserid=1212121212121212; steamCountry=CN%7Casdfasdfasdfasdf; sessionid=asdfasdfasdfasdf; timezoneOffset=28800,0; steamLoginSecure=ASDFASDFASDFASDF; steamMachineAuth1234123412341234=ASDFASDFASDFASDFF

needs?
======
* python3
* requests module
