import requests
import nguyenthanhngoc
from nguyenthanhngoc import *
import sys
import os
import time
from time import sleep
def check_password():
    expected_password = "NgocVipPro"
    password = input("\033[1;36mNhap Pass: ")
    if password == expected_password:
        print("\033[1;36mSuccess Full !")
        sleep(2)        
    else:
        print("Pass Not Found - You Not Have Pass ?:)))")
        exit()
check_password()
def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()

Write.Print(f"""
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJJJJ?????JJJJJJYYYYYYYYYYYYY55555555555555555555555555
YYYJYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJJ?77!~~~^^^^^^^~~~~!!!!!77??JJYYYYYYYYYYYYYYY5YY5555555555555
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ?7~^:::...:::::::^^^^~~~!!~!~~~~!!7?JJYYYYYYYYYYYYYYYYYYYYYYYYYYY
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ?7~:...    ......::^^^^^^^^~~~!!77!~~~!!7?JJJJYYYYYYYYYYYYYYYYYYYYYYY
JJJJJJJJJJJJJJJJJJJJJJJJJJJJJ?!^.....    . ....::^:^^^~~!!!7!!!77~~!!!!!!7??JJJJYYYYYYYYYYYYYYYYYYYY
JJJJJJJJJJJJJJJJJJJJJJJJJ??7~::.   ..   ..:^:.....:^~~~~~^:::^^~!!!!!77?7777??JJJJJJJYYYYYYYYYYYJYYY
JJJJJJJJJJ??JJJJJJJJJ?????~:::   .. ....::.   ...^~^::.........::^~!!!!!77?7?????JJJJJJJJJJJJJJJJJJJ
????????????????????????7~~?~...:......:.     .:^:...  ...:..:..:::^!!!!!!7??77????JJJJJJJJJJJJJJJJJ
???????????????????????7!?JJY~^^:...:::.     .^^..:.  ...:...^^..:::^!~~!!!7?77??7???JJJJJJJJJJJJJJJ
????????????????????77?!7?7J5Y!:......      :~:  ..  .. ~^ :.^!...:::~~^^~!!7???7?7???????JJJJJJJJJJ
777777????????77777!~~~!!7!77J^   .........^~....:   ^.^7..~.^7....:.^~^::^7!7??77777???????????????
7777777777777777!!^.:^:!J?JYJ7^:::::......!!:::.::. :^~7~ :7:7?::::::^~^~::^7!??7777777?????????????
777777777777777~~~. :^:~!~!!^^:..^^......!7^^~^^^:::~^!~^.~J~77^::^::^~!!^::~77??777777777??????????
777777777777!!^~!:  :::~:^:.^....^:::::.~7~^!~~!^^:^~^~:^:!J777!^~^^^~~7!!^:^77??77!7J5?777777777777
!!!!!!!!!!!!!^^!~.  .::~:..::...:::::::^7~^~!~!!^^^~~^::^:!???77~~~~~!~!7!~^^!7???77!?PPJ!7777777777
!!!!!!!!!!!!~^!!^.  ..^~:.::....::^::^:7!^~!^~:^~^^!~:.:^^!?J?7?!~~~~7~!!!~~~!77??77!7YYJ?!!77777777
!!!!!!!!!!!!^~~~::   .^!:.::.:::.:::^^~7~~!~~^:^!!^7!:.^^^!7J77?7~~!!7~!!!~!~!77??777!7JJ7!!!!!!!!!!
~~~~~~~~~~~~^~~~:^:  .^!:.:.::::::::^^!~~~:~^...^!^!!^^~~^!~?77??!!!!!~!~~!!!~77??77?77??7!!!!!!!!!!
~~~~~~~~~~~~~~~~^:^.. :!~::.:^^.:.::^^!~~..:. ...^~~~..:!^~:!!777!!7!~~!^~7!!!777?77??77777!!~!!!!!!
^^^^^^^^^^^^~^^^^::::. ~7~:.^^::..::^~!7??JJJ!^:...:^...:~~.~!!!~~!!^!!!^!7!!!?77?7!7??777!!!~~~~~~~
^^^^^^^^^^^^^^^^^^:^~^::~!~^^^.:  .::~Y5YPP#BG5P57~:.:....:.^~~~~~^.:!~::7!~!!777??!!??777!~~!~~~~~~
^^^^^^^^^^^^^^^^^::^~~~~~~!!!::.  .::^:^!YY5PYY5Y?Y7^........:::::..::..:!!!~!7!?7?7!7??77!~~!~^~~~~
^^^^^^^^^^^^^^^^^.:^~^^^^^^~^.^   .::::.~?!~!!?!: .:^............:.......^^^:!!777?7!77??77~^~~^^^^~
^^^^^^^^^^^^^^^^..:^::^^:.::..:   ..:::::~^::~~.  ..............:~7JJ??J7:.:^7?7!7?7!!77???7~~~^^^^^
:^^^^^^^^^^^^^^:.:^:.:^:.:::.:.   ...~^::^^^^^:................:JJPPP5P55P!^!??!!???!!7!???7!!!~^^^^
::::^^^^^^^^^^:..::.:^^::.^! :.    ..~~~^:^^^^:::..............~J?J?YJJ.:JPJ777!7?7?!!?77777!~~~~~^^
:::::^^^^^^^^:..^:.::^^::~~^ ^.  . ..^::^^:::::::.......::.....^^:^77: .^77777!7777?7!?!7!777^^^^^^^
:::::::::::^: .^:..^^^^^~^!:.^. :. ..:^ ......................::::^~:::~!~!7!!77777777?!!!^7!~^^^^^^
:::::::::::. :^:.:^^^:^^^~7:.~:.^:  :.~.........:^::::........:::^^^^^~!~~77!777!7777??!!!:~!~^::^^^
::::::::::..:~:..:^::.:^^!?.:~^:~~  :.^~  ......~7!777!~^......::::^^7!~~!!7!777~7!77??7!!::~~~:^^^^
:::::::^:.::^:...^:..:^^!?7.:~^^!7..:^.^~:. .....^~~!7J7:........::^!7!~~!77!!7~!!!!?J?7!~::^~~^^^^^
:::::::::::::...::..:^^!7?7.:~^^!?^ :^~.!7~^.......::::.......:::^~~~7!!!!77!!!~!!!7J??7~!^^:^^^:^^^
::^^^:::::::...::..:^^~7?!!.^~^^!?7.^^!~:!77!~^...........:::^^~~~~^~77!!!!77!~!!!!7JJJ7!~~~^^^^::::
^^^^:::::::...::..:^^!??!~!:^!^^!??!:~~!!^~77!7!~^:::^^^~~~~~~~~~^!~~7?!!!!!!~!7~~!?JJ?!!^::^~^^::::
^::::::::^...:...:^^!??!~!7^:!~^!?7?~!!~!!!~!7!!77!!!!!!7!!!!!!!~~!!~~?!!!!!!~!~~~7JJJ7!~^^:..:~::^:
^^^^^^^^^. ..:..:^^^~~~~!!!~^~~~~7?7?7?~~!!!!77!!????7777???!!!!!!!!!~!7!!!~!!~^~!JJJ?!~.:~^.^^..:~^
~~~~~~~~. ..::.^^^.  ...::~~^!77~!?77???~~!!!!!!!777777?????!!!!!!!~^^~~!!!!~^^~7J7??77^.~!^:7:^!~::
^^^^^^^. ..::.::~:        .:^!!~:^~77!7J?~~!~~!!!!!!!!!!!~!!~~~~~~^.:^~~~!~^^~!??~!?7!^~~!~!!!^:^!:~
^^^:^^....:^.^:  .:..      .^^.^^::^!!~!??!~~^^^^^:^~^^:::~:..:.^^:.:^^~~~~~~75577??!  .^^^:~:....  
^::^:..: .^:^~:.   ......   .^::^..:^~!~~!?7~~~^^:::.:...:^  ..:^: .:^~!!~~~?PGPYJ?!~       .:.     
::^:::^..^^^~^::..    ..::.. .^:^: ...:~!~~!!^::::......::. ..:^:  .:~!^::~JPP5Y5P5?~^        :.    
^^:^^:..!^^~::::::..     ..::..:^~:  ...^!!~^^^^:.......:^  .:^.  ..^^..:!YP55PGGPGPJ^.        ..   
^^^::..^~^^^.........        ....:~:.    .^~!!~^^^:::::^~7~.^^.   .::.:!YPPPPPPPPPGGPJ^...      ....
:::^..:~~^~^:.                    .:^:......:^~~~!~!!77!!!:^:    .^~!J5PPPPPPP5PPPPGPP!::::........:
^^^:.:^~~^!7Y?7!~^:..               ..........::!7!77777J^^:   :~7775P555PPPP555PPPGGP~:~^^^^:.....:
^^^..^:!~~!?5YYYYYYJJ??7!~^:..             ......:^~!7?JJ~~7~!?Y5PJ~!Y55555PPPP5PPPGGY~!?7!!!~^^::::
:^:.^::!~~!JYJJJJYYYYYYYYY5555YYJJ??7!!!~~!~~~~~~~~!?!7??YPGBP55555?~~Y55555PPPPGGPGGJ?JYY??77!~~~^^
:^::^:^!!!!YYJJYYJJYYYYYYYY55555555Y5Y777YP5YYYY55YY555PB##BBP555555J~!Y5555PPPPPGGGPYY555YJJJ?77!!!
^^^^^:^!!!!YYJJY55YYYY55YYY5555YYYYYYY77755YYYYYYYPBBB###BGPP55555555?~755555PPPPPGGG55PPP5YYYYJ???7
^^^~^^^!!~!YYYJJY5P5YY55YYY55YYYYYYYYY77755YYYYYYY5PG#@BGP555PP5555555?!?55555PPPPPGGPPPPG55555YYJJJ
^~~~^^^~!~!YYYJYYY5P5Y5PYYYYYYYYYYYYYY7!7PYYYYYYYY5YY5B555555555555555PJ!Y55555PPPPPPGPPPP555555YYYY
7!!!!!!!7~7YYYYYYYY5P5YPYYYYYYYYYYYYYY7!?GYYYYYYY5555555555555555555555P?755555PPPPPPPGPPP555P555555
!!!!!!!!77JYYYYJJYYYYP55YYYYYYYYYYYYYY7~JB5YYYYYY55555555555555555555555G?Y55555PPPP55PGPP555PP55555
!~!!~~!J55YYYYYYYYYYY5P5Y555YYYYYYYYYY!!5B5YYYYY555555555555555555555555GPJ555555PPP555PGP5555P55555
~~~~~7Y55YYYYYYYYYYYY5P555555555YYYYYY!!GG5YYYY5555555555555555555555555PG?Y555555PP5555PGP555PP5555
^^^!JY555YYYYYYYYYYY55555555555555YYYY~?GGPYY555555555555555555555555555PP7Y555555PP5PPPPGGPP5PPP555
^^7YY5PPYYY5YYYYYYY555P55555555555555J^YGGP55555555555555555555555555555G5!Y555555PP5PPPPPGGPPPPPPPP
!JY5555Y???J???JJJYY55PPP5555555555557~5GGP555555PP555555555555555555555GJ!5555555PP5PPPPGGGGGGPPPPP
J??7777!!77777???????JYY555P55PP55555!?PGGP55555PPP55555555555555555555PP??5555555PP5GGGPY7JGGGGGGGP
!!!!!!!~!7???JJJJJJJJJJJJJY5PPPPPPPP5!5PGGP5555PPP55555555555555555555PG5YJ555555PPPGGY!:::^JGGGGGGP
^~^~!!!!7777????JJYYY55YYYJJY5PPPPPPY?PPGGPP55PPP55555555555555555555PGP7Y55555PGBGY7:  ...:^YBGGGGG
...~7!~~!~~!7777???JY5555YYJJJJ5PPPPJ5PPGPPP5PPP5555555555555P5555555PPY?5555PGG57:.:   ..:::~5GGGGG
.^~!!!!!77?????JJYY55YJY555YYJ??YPPYJPPPGPPPPPP5555555555555PP5555555555P5PPG5?^.  :5J~:...::^!PGGGG
:!77!!7???7!!!!77?JY55YYP55YYJJ??J5?5PPGPPPPPP55555555555555PPP55555PP5PGGPJ~.     ^P555J!^::^~?GGGG
~!!7????!~~~!!~~!!7!7?YPP555YYJ??7!?PPPGPPPPPP55PPPPPPP55555PPPPPPPPPGGG57:        7PYYY555Y?!~~YGGG
!7??JJ7!^^^:.~!!!!!7777?YP55YYJJ?!~JPPGPPPPPP5PPPPPPPPPP55PPPPPPPPGGBPJ~.         .?5YYY5555PP5J?PPP
77??77!!.:!J?:^::::^^!7!!?55YYJ?!~!7PGPPPPPPPPPPPPPPPPPPPPPPPPPPGBG57~            :J5YY5555555PPPP55
77!!!!^...~^:~~7~!!~!^!!7~75YYJ!~~775GPPPPPPPPPPPPPPPPPPPPPPPPPBGY~::~~^^:..      ^5YYY55555555PPP5J
!77!!:       !7777??JJ?^^^7YYJ77^~7!YGPPPPPPPPPPPPPPPPPPPPPPGBP?^   .7PYYYYJJ??7!!?5YY5555555555PP5J
!!777^.   ....:^^^^^~~^^^^!JJ!7!!7!~YGPPPPPPPPPPPPPPPPPPPPGG5!.     .!5JJJJYYYYYYYYYYY5555555555PPP5
!!7777!~^:.::::::^^^^^~~~^~?7!!77!~~5GPPPPPPPPPPPPPPPPPPGB5!.       .7YJJJYYYYYYYYYYYY55555555555PP5\n""", Colors.pink, interval=0.00005)
    
proxies = []

# Get proxies from raw text files
raw_proxy_sites = ["https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
                   "https://api.openproxylist.xyz/http.txt",
                   "http://alexa.lr2b.com/proxylist.txt",
                   "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                   "http://worm.rip/http.txt",
                   "https://proxy-spider.com/api/proxies.example.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://proxyspace.pro/http.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
                   "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
                   "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
                   "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
                   "https://firet.io/firetx_retro/datacanthiet/proxies.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
                   "https://openproxylist.xyz/http.txt",
                   "https://dodanhtai.site/proxy/http.txt",
                   "http://worm.rip/http.txt",
                   "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
                   "http://rootjazz.com/proxies/proxies.txt",
                   "https://api.proxyscrape.com/?request=displayproxies&proxytype=https",
                   "https://www.proxy-list.download/api/v1/get?type=http",
                   "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
                   "https://api.openproxylist.xyz/http.tx",
                   "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
                   "http://alexa.lr2b.com/proxylist.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
                   "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
                   "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
                   "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
                   "https://proxy-spider.com/api/proxies.example.txt",
                   "https://multiproxy.org/txt_all/proxy.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://proxyspace.pro/http.txt",
                   "https://proxyspace.pro/https.txt",
                   "https://proxyspace.pro/https.txt",
                   "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
                   "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
                   "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
                   "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
                   "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
                   "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                   "https://rootjazz.com/proxies/proxies.txt",
                   "https://www.proxy-list.download/api/v1/get?type=https",
                   "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt",
                   "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
                   "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
                   "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
                   "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
                   "https://sunny9577.github.io/proxy-scraper/proxies.txt",
                   "https://api.getproxylist.com/proxy?protocol[]=http&anonymity[]=high&allowsHttps=true&allowsPost=true&maxConnectTime=1&maxSecondsToFirstByte=1",]

for site in raw_proxy_sites:
    response = requests.get(site)
    for line in response.text.split('\n'):
        if ':' in line:
            ip, port = line.split(':', maxsplit=2)[:2]
            proxies.append(f'{ip}:{port}')
    
proxy_count = 500000
with open('Ca.txt', 'w') as f:
    for proxy in proxies:
        f.write(proxy + '\n')
        print("\033[1;36mAdm: 𓂄𓆩 Cá 𓆪𓂁︎ \033[1;32m| \033[1;36mProxy Save File Ca.txt")
        print("\033[1;36mTele: @thanhngocc2806")
def clear():
    os.system("cls" if os.name == "nt" else "clear")
clear()
Write.Print(f"""
██╗   ██╗███████╗    ████████╗███████╗ █████╗ ███╗   ███╗
██║   ██║██╔════╝    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
██║   ██║███████╗       ██║   █████╗  ███████║██╔████╔██║
╚██╗ ██╔╝╚════██║       ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
 ╚████╔╝ ███████║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║
  ╚═══╝  ╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
  
┌───────────────────└┐ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 └┐──────────────────┐
│
│   𝐓𝐎𝐎𝐋 𝐍𝐀𝐌𝐄: VIRUS TEAM
│   𝐕𝐄𝐑𝐒𝐈𝐎𝐍: 4.0 - Save File Ca.txt
│   𝐔𝐏𝐃𝐀𝐓𝐄𝐃 𝐎𝐍 𝐃𝐀𝐓𝐄: 04/06/2024
│   𝐒𝐔𝐏𝐏𝐎𝐑𝐓 𝐆𝐑𝐎𝐔𝐏: zalo.me/g/hbcumm801
│   𝐓𝐎𝐎𝐋 𝐀𝐃𝐌𝐈𝐍: 𓂄𓆩 Cá 𓆪𓂁︎ x Tmr Virus
│
└──────────────────────────────────────────────────┘
====================================================
             Thanks For Usesing My Tool
====================================================\n""", Colors.red, interval=0.003)