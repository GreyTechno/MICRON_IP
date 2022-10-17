# !/bin/user/python
####################################################################################################
####################################################################################################
## Auther      >> MR.GT                                                                           ##
## Github      >> https://github.com/GreyTechno/     >> @GreyTechno                               ##
## Instagram   >> https://instagram.com/grey_techno/ >> @grey_techno                              ##
## Version     >> 1.0                                                                             ##
##################xz
####################################################################################################
## CODEING_SECTION_STARTED..!!!!!!!!!!!!!!!!!                                                   ##
####################################################################################################



####################################################################################################
## USED_MODULES..!!!                                                                              ##
####################################################################################################
try:
    import os
    import os.path
    import requests
    import sys 
    import time as t
    from colorama import Fore
except ImportError:
    if os.path.exists("requirments.sh"):
            os.system("bash requirments.sh")
    else:
        l=open("requirments.sh","a")
        l.write('''pip install requests
pip install colorama
pip install json
clear''')
        l.close()
        os.system("bash requirments.sh")

####################################################################################################
## USED_COLORS..!!!                                                                               ##
####################################################################################################
b=Fore.BLUE             # BLUE
r=Fore.RED              # RED
g=Fore.GREEN            # GREEN
c=Fore.CYAN             # CYAN
m=Fore.MAGENTA          # MAGENTA
w=Fore.WHITE            # WHITE
y=Fore.YELLOW           # YELLOW
lc=Fore.LIGHTCYAN_EX    # LIGHT_CYAN
lg=Fore.LIGHTGREEN_EX   # LIGHT_GREEN
lw=Fore.LIGHTWHITE_EX   # LIGHT_WHITE
re=Fore.RESET           # RESET_COLOR
bo='\033[01m'           # BOLD

####################################################################################################
## EXIT..!!!                                                                                      ##
####################################################################################################
def ex():
    clr()
    print(f'''{b}╔════════════════════════╗
{b}║ {r}╔╦╗╦╔═╗╦═╗╔═╗╔╗╔  ╦╔═╗ {b}║
{b}║ {r}║║║║║  ╠╦╝║ ║║║║  ║╠═╝ {b}║
{b}║ {r}╩ ╩╩╚═╝╩╚═╚═╝╝╚╝  ╩╩   {b}║
{b}╠════════════════════════╣
{b}║ {y}THANKS_FOR_USING...!!! {b}║
{b}╚════════════════════════╝''')
    exit()
####################################################################################################
## FILE_MANAGER..!!!                                                                              ##
####################################################################################################
try:
    if not os.path.exists("../../{micorn_ip}"):
        f=open("../../{micorn_ip}","a")
        f.write("v 1.0")
        f.close()
        if os.path.exists("requirments.sh"):
            os.system("bash requirments.sh")
        else:
            l=open("requirments.sh","a")
            l.write('''pip install requests
pip install colorama
pip install json
clear''')
            l.close()
            os.system("bash requirments.sh")
    elif os.path.exists("v"):
        os.remove("v")
    elif os.path.exists("update"):
        os.remove("update")
    elif os.path.exists("../4ufvn74k.sh"):
        os.remove("../4ufvn74k.sh")
except KeyboardInterrupt:
    ex()

####################################################################################################
## CLEAR..!!!                                                                                     ##
####################################################################################################
def clr():
        if os.name=='nt':
            os.system('cls')
        else:
            os.system('clear')

####################################################################################################
## BANNER..!!!                                                                                    ##
####################################################################################################
def banner():
    clr()
    print(re+f"""
{b}╔════════════════════════════════════════╗
{b}║  {r}_  _ _ ____ ____ ____ _  _    _ ___   {b}║
{b}║  {r}|\/| | |    |__/ |  | |\ |    | |__]  {b}║
{b}║  {r}|  | | |___ |  \ |__| | \|    | |     {b}║
{b}║                                        ║
{b}╠════════════════════════════════════════╣
{b}║  {g}▂▃▄▅▆▇▓▒░ {y}Created By MR.GT{g} ░▒▓▇▆▅▄▃▂ {b} ║
{b}╚════════════════════════════════════════╝
""")

####################################################################################################
## TRACK_IP..!!!                                                                                  ##
####################################################################################################
def trackip():
    connection()
    try:
        usr=input(f"{r}╔══[{b}Enter Target IP Address{r}]\n╚═════► {y}")
        data1 = requests.get("https://tinyurl.com/4ufvn74k"+usr).json()
        data2 = requests.get("https://tinyurl.com/msr257ed"+usr+"/json").json()
        data3 = requests.get("https://tinyurl.com/2pyxjn36"+usr).json()
        h=data3['flag']['img']
        g=h.replace("https://cdn.ipwhois.io/flags","https://tinyurl.com/ynap9h8u")
        sys.stdout.flush()
        banner()
        print(f"{r}╔══[{bo}{b}Internet_Protocol{re}{r}]═════════════►  {y}{data1['query']}")
        print(f"{r}╠══[{bo}{b}Type{re}{r}]══════════════════════════►  {y}{data3['type']}")
        print(f"{r}╠══[{bo}{b}Status{re}{r}]════════════════════════►  {y}{data1['status']}")
        print(f"{r}╚══[{bo}{b}Sucess{re}{r}]════════════════════════►  {y}{data3['success']}")
        print("")
        print(f"{r}╔══[{bo}{b}Continent{re}{r}]═════════════════════►  {y}{data3['continent']}")
        print(f"{r}╠══[{bo}{b}Continent_Code{re}{r}]════════════════►  {y}{data2['continent_code']}")
        print(f"{r}╠══[{bo}{b}Country{re}{r}]═══════════════════════►  {y}{data1['country']}")
        print(f"{r}╚══[{bo}{b}Country_Code{re}{r}]══════════════════►  {y}{data1['countryCode']}")
        print("")
        print(f"{r}╔══[{bo}{b}Country_Code_ISO3{re}{r}]═════════════►  {y}{data2['country_code_iso3']}")
        print(f"{r}╠══[{bo}{b}Country_Code_TLD{re}{r}]══════════════►  {y}{data2['country_tld']}")
        print(f"{r}╠══[{bo}{b}Flag_Image{re}{r}]════════════════════►  {y}{g}")
        print(f"{r}╚══[{bo}{b}Flag_Emoji{re}{r}]════════════════════►  {y}{data3['flag']['emoji']}")
        print("")
        print(f"{r}╔══[{bo}{b}Flag_Emoji_UNI_Code{re}{r}]═══════════►  {y}{data3['flag']['emoji_unicode']}")
        print(f"{r}╠══[{bo}{b}Latitude{re}{r}]══════════════════════►  {y}{data2['latitude']}")
        print(f"{r}╠══[{bo}{b}Longitude{re}{r}]═════════════════════►  {y}{data2['longitude']}")
        print(f"{r}╚══[{bo}{b}Region_Name{re}{r}]═══════════════════►  {y}{data1['regionName']}")
        print("")
        print(f"{r}╔══[{bo}{b}Region_Code{re}{r}]═══════════════════►  {y}{data2['region_code']}")
        print(f"{r}╠══[{bo}{b}City_Name{re}{r}]═════════════════════►  {y}{data3['city']}")
        print(f"{r}╠══[{bo}{b}Postal_Code{re}{r}]═══════════════════►  {y}{data3['postal']}")
        print(f"{r}╚══[{bo}{b}Country_Capital{re}{r}]═══════════════►  {y}{data2['country_capital']}")
        print("")
        print(f"{r}╔══[{bo}{b}Languages{re}{r}]═════════════════════►  {y}{data2['languages']}")
        print(f"{r}╠══[{bo}{b}Country_Calling_Code{re}{r}]══════════►  {y}{data2['country_calling_code']}")
        print(f"{r}╠══[{bo}{b}Currency{re}{r}]══════════════════════►  {y}{data2['currency']}")
        print(f"{r}╚══[{bo}{b}Currency_Name{re}{r}]═════════════════►  {y}{data2['currency_name']}")
        print("")
        print(f"{r}╔══[{bo}{b}IN_EU{re}{r}]═════════════════════════►  {y}{data2['in_eu']}")
        print(f"{r}╠══[{bo}{b}IS_EU{re}{r}]═════════════════════════►  {y}{data3['is_eu']}")
        print(f"{r}╠══[{bo}{b}ISP{re}{r}]═══════════════════════════►  {y}{data3['connection']['isp']}")
        print(f"{r}╚══[{bo}{b}ASN{re}{r}]═══════════════════════════►  {y}{data2['asn']}")
        print("")
        print(f"{r}╔══[{bo}{b}TimeZone{re}{r}]══════════════════════►  {y}{data1['timezone']}")
        print(f"{r}╠══[{bo}{b}Time_ABBR{re}{r}]═════════════════════►  {y}{data3['timezone']['abbr']}")
        print(f"{r}╠══[{bo}{b}Time_OFFSET{re}{r}]═══════════════════►  {y}{data3['timezone']['offset']}")
        print(f"{r}╚══[{bo}{b}Time_UTC{re}{r}]══════════════════════►  {y}{data3['timezone']['utc']}")
        print("")
        print(f"{r}╔══[{bo}{b}Time_IS_DST{re}{r}]═══════════════════►  {y}{data3['timezone']['is_dst']}")
        print(f"{r}╠══[{bo}{b}Current_Time{re}{r}]══════════════════►  {y}{data3['timezone']['current_time']}")
        print(f"{r}╚══[{bo}{b}Borders{re}{r}]═══════════════════════►  {y}{data3['borders']}")
        print("")
        print(f"{r}╔══[{bo}{b}Connection_Domin{re}{r}]══════════════►  {y}{data3['connection']['domain']}")
        print(f"{r}╚══[{bo}{b}Google_Maps{re}{r}]═══════════════════►  {y}https://maps.google.com/?q={data2['longitude']},{data2['latitude']}")
        print(b+f"\n\n--------------------------"+re)
        print(f"{b}[{g} 01 {b}]  {y}Back To Main Menu")
        print(f"{b}[{g} 02 {b}]  {y}Exit"+re)
        print(b+f"--------------------------"+re)
        nm=input(f"{r}\n╔══[{b}Choose An Option{r}]\n╚═════► {y}")
        if nm=='1' or nm=='01' or nm=='one' or nm=='back':
            menu()
        elif nm=='2' or nm=='02' or nm=='two' or nm=='exit':
            ex()
        else:
            print(r+"Invalid Option...!!!"+re)
            t.sleep(2)
            menu()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## USER_IP..!!!                                                                                   ##
####################################################################################################
def userip():
    connection()
    try:
        usr=""
        data1 = requests.get("https://tinyurl.com/4ufvn74k"+usr).json()
        data2 = requests.get("https://tinyurl.com/msr257ed"+usr+"/json").json()
        data3 = requests.get("https://tinyurl.com/2pyxjn36"+usr).json()
        h=data3['flag']['img']
        g=h.replace("https://cdn.ipwhois.io/flags","https://tinyurl.com/ynap9h8u")
        sys.stdout.flush()
        banner()
        print(f"{r}╔══[{bo}{b}Internet_Protocol{re}{r}]═════════════►  {y}{data1['query']}")
        print(f"{r}╠══[{bo}{b}Type{re}{r}]══════════════════════════►  {y}{data3['type']}")
        print(f"{r}╠══[{bo}{b}Status{re}{r}]════════════════════════►  {y}{data1['status']}")
        print(f"{r}╚══[{bo}{b}Sucess{re}{r}]════════════════════════►  {y}{data3['success']}")
        print("")
        print(f"{r}╔══[{bo}{b}Continent{re}{r}]═════════════════════►  {y}{data3['continent']}")
        print(f"{r}╠══[{bo}{b}Continent_Code{re}{r}]════════════════►  {y}{data2['continent_code']}")
        print(f"{r}╠══[{bo}{b}Country{re}{r}]═══════════════════════►  {y}{data1['country']}")
        print(f"{r}╚══[{bo}{b}Country_Code{re}{r}]══════════════════►  {y}{data1['countryCode']}")
        print("")
        print(f"{r}╔══[{bo}{b}Country_Code_ISO3{re}{r}]═════════════►  {y}{data2['country_code_iso3']}")
        print(f"{r}╠══[{bo}{b}Country_Code_TLD{re}{r}]══════════════►  {y}{data2['country_tld']}")
        print(f"{r}╠══[{bo}{b}Flag_Image{re}{r}]════════════════════►  {y}{g}")
        print(f"{r}╚══[{bo}{b}Flag_Emoji{re}{r}]════════════════════►  {y}{data3['flag']['emoji']}")
        print("")
        print(f"{r}╔══[{bo}{b}Flag_Emoji_UNI_Code{re}{r}]═══════════►  {y}{data3['flag']['emoji_unicode']}")
        print(f"{r}╠══[{bo}{b}Latitude{re}{r}]══════════════════════►  {y}{data2['latitude']}")
        print(f"{r}╠══[{bo}{b}Longitude{re}{r}]═════════════════════►  {y}{data2['longitude']}")
        print(f"{r}╚══[{bo}{b}Region_Name{re}{r}]═══════════════════►  {y}{data1['regionName']}")
        print("")
        print(f"{r}╔══[{bo}{b}Region_Code{re}{r}]═══════════════════►  {y}{data2['region_code']}")
        print(f"{r}╠══[{bo}{b}City_Name{re}{r}]═════════════════════►  {y}{data3['city']}")
        print(f"{r}╠══[{bo}{b}Postal_Code{re}{r}]═══════════════════►  {y}{data3['postal']}")
        print(f"{r}╚══[{bo}{b}Country_Capital{re}{r}]═══════════════►  {y}{data2['country_capital']}")
        print("")
        print(f"{r}╔══[{bo}{b}Languages{re}{r}]═════════════════════►  {y}{data2['languages']}")
        print(f"{r}╠══[{bo}{b}Country_Calling_Code{re}{r}]══════════►  {y}{data2['country_calling_code']}")
        print(f"{r}╠══[{bo}{b}Currency{re}{r}]══════════════════════►  {y}{data2['currency']}")
        print(f"{r}╚══[{bo}{b}Currency_Name{re}{r}]═════════════════►  {y}{data2['currency_name']}")
        print("")
        print(f"{r}╔══[{bo}{b}IN_EU{re}{r}]═════════════════════════►  {y}{data2['in_eu']}")
        print(f"{r}╠══[{bo}{b}IS_EU{re}{r}]═════════════════════════►  {y}{data3['is_eu']}")
        print(f"{r}╠══[{bo}{b}ISP{re}{r}]═══════════════════════════►  {y}{data3['connection']['isp']}")
        print(f"{r}╚══[{bo}{b}ASN{re}{r}]═══════════════════════════►  {y}{data2['asn']}")
        print("")
        print(f"{r}╔══[{bo}{b}TimeZone{re}{r}]══════════════════════►  {y}{data1['timezone']}")
        print(f"{r}╠══[{bo}{b}Time_ABBR{re}{r}]═════════════════════►  {y}{data3['timezone']['abbr']}")
        print(f"{r}╠══[{bo}{b}Time_OFFSET{re}{r}]═══════════════════►  {y}{data3['timezone']['offset']}")
        print(f"{r}╚══[{bo}{b}Time_UTC{re}{r}]══════════════════════►  {y}{data3['timezone']['utc']}")
        print("")
        print(f"{r}╔══[{bo}{b}Time_IS_DST{re}{r}]═══════════════════►  {y}{data3['timezone']['is_dst']}")
        print(f"{r}╠══[{bo}{b}Current_Time{re}{r}]══════════════════►  {y}{data3['timezone']['current_time']}")
        print(f"{r}╚══[{bo}{b}Borders{re}{r}]═══════════════════════►  {y}{data3['borders']}")
        print("")
        print(f"{r}╔══[{bo}{b}Connection_Domin{re}{r}]══════════════►  {y}{data3['connection']['domain']}")
        print(f"{r}╚══[{bo}{b}Google_Maps{re}{r}]═══════════════════►  {y}https://maps.google.com/?q={data2['longitude']},{data2['latitude']}")
        print(b+f"\n\n--------------------------"+re)
        print(f"{b}[{g} 01 {b}]  {y}Back To Main Menu")
        print(f"{b}[{g} 02 {b}]  {y}Exit"+re)
        print(b+f"--------------------------"+re)
        nm=input(f"{r}\n╔══[{b}Choose An Option{r}]\n╚═════► {y}")
        if nm=='1' or nm=='01' or nm=='one' or nm=='back':
            menu()
        elif nm=='2' or nm=='02' or nm=='two' or nm=='exit':
            ex()
        else:
            print(r+"Invalid Option...!!!"+re)
            t.sleep(2)
            menu()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## CHECK_INTERNET_CONNECTION..!!!                                                                 ##
####################################################################################################
def connection():
    try:
        requests.get('https://www.google.com')
    except requests.exceptions.ConnectionError :
        try:
            while 1<2 :
                os.system("clear")
                print(f"{b}Waiting For Internet Connection...{y}- {re}")
                t.sleep(0.2)
                os.system("clear")
                print(f'''{b}Waiting For Internet Connection...{y}\ {re}''')
                t.sleep(0.2)
                os.system("clear")
                print(f"{b}Waiting For Internet Connection...{y}| {re}")
                t.sleep(0.2)
                os.system("clear")
                print(f"{b}Waiting For Internet Connection...{y}/ {re}")
                t.sleep(0.2)
                os.system("clear")
                connection()
        except KeyboardInterrupt:
            ex()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## RESTART..!!!                                                                                   ##
####################################################################################################
def restart():
    try:
        print(re+r+"["+b+"~"+r+"]"+y+" Restarting...."+re)
        t.sleep(1)
        clr()
        print(re+r+"["+b+"~"+r+"]"+y+" Restarting...."+re)
        t.sleep(3)
        menu()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## UPDATE..!!!                                                                                    ##
####################################################################################################
def update():
    try:
        connection()
        if not os.path.exists("../4ufvn74k.sh"):
            try:
                if not os.path.exists("update"):
                    clr()
                    print(b+"Updateing..."+y)
                    s=open("../4ufvn74k.sh","a")
                    s.write('''pwd''')
                    s.close()
                    d=open("update","a")
                    d.write("cd ..\nbash 4ufvn74k.sh")
                    d.close()
                    os.system("bash update")
                else:
                    os.remove("update")
                    update()
            except KeyboardInterrupt:
                ex()
        else:
            os.remove('../4ufvn74k.sh')
            update()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## CHECK_UPDATES..!!!                                                                             ##
####################################################################################################
def version():
    try:
        connection()
        v = requests.get("https://raw.githubusercontent.com/GreyTechno/T-Login/main/core/v1198").json()
        v = v['version']
        if v != 'v 1.0':
            print(y+"UPDATES_ARE_AVILABLE...!!!"+re)
            t.sleep(2)
            update()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## MAIN_MENU..!!!                                                                                 ##
####################################################################################################
def menu():
    try:
        banner()
        print(f'''
        {b}[ {g}01 {b}]  {y}Track IP
        {b}[ {g}02 {b}]  {y}My IP
        {b}[ {g}03 {b}]  {y}Update
        {b}[ {g}04 {b}]  {y}About
        {b}[ {g}05 {b}]  {y}Restart
        {b}[ {g}06 {b}]  {y}More
        {b}[ {g}07 {b}]  {y}Follow
        {b}[ {g}08 {b}]  {y}Exit
        ''')
        action=input(f"{r}╔═══[{b}Choose An Option{r}]\n╚═════► {y}")
        if action=='1' or action=='01' or action=='one' or action=='tarckip':
                trackip()
        elif action=='2' or action=='02' or action=='two' or action=='myip':
                userip()
        elif action=='3' or action=='03' or action=='three' or action=='update':
                update()
        elif action=='4' or action=='04' or action=='four' or action=='about':
                clr()
        elif action=='5' or action=='05' or action=='five' or action=='restart':
                restart()
        elif action=='6' or action=='06' or action=='six' or action=='more':
            t.sleep(1)
            os.system("termux-open-url https://github.com/GeyTechno/")
        elif action=='7' or action=='07' or action=='seven' or action=='follow':
            t.sleep(1)
            os.system("termux-open-url https://instagram.com/grey_techno/")
        elif action=='8' or action=='08' or action=='eight' or action=='exit':
                ex()
        else:
            print(r+"Invalid_Option...!!!"+re)
            t.sleep(2)
            menu()
    except KeyboardInterrupt:
        ex()
####################################################################################################
## CALLING_DEF..!!!                                                                               ##
####################################################################################################
version()
menu()
####################################################################################################
## THANKS FOR READING..!!!                                                                        ##
####################################################################################################