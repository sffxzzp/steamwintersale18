steamwintersale18
======
Bless Python script for https://store.steampowered.com/promotion/cottage_2018/;

**Only for personal use.**

STILL UNDER DEVELOPMENT. THINK TWICE BEFORE YOU USE IT.


Feature
------
Open cottage door only.
Will `NOT` explore queue. use ArchiSteamFarm instead.


Usage
------
Example for `Chrome` browser:
1. Login and open the `Network` page.
2. Refresh and you'll get a list of requests.
3. Select `Filter -> Doc`.
4. Click the `cottage-2018/` usually the first one in the list.
5. At the right panel select `Headers -> RequestHeaders -> Cookie`.
6. Copy it and paste in the `mybotname.txt` file you created.


Result
------
Example cofing file: `mybotname.txt`
```text
browserid=##############; sessionid=##############; timezoneOffset=#####,#; bShouldUseHTML5=#; SL_GWPT_Show_Hide_tmp=#; SL_wptGlobTipTmp=#; steamMachineAuth#############==##############;; BL_D_PROV=; BL_T_PROV=;
```


Needs?
------
**python3** and **requests**

* https://www.python.org/downloads/
* pip install requests

> Don't forget setup you PATH environment...
