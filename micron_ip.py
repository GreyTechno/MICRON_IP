# !/bin/user/python
####################################################################################################
####################################################################################################
## Auther      >> MR.GT                                                                           ##
## Github      >> https://github.com/GreyTechno/     >> @GreyTechno                               ##
## Instagram   >> https://instagram.com/grey_techno/ >> @grey_techno                              ##
## Version     >> 1.0                                                                             ##
## Tool_Name   >> MICRON_IP                                                                       ##
## Interface   >> Command_Line_Interface (CLI)                                                    ##
####################################################################################################
## If You Can Use Any Part From This Code. So Give Me The Credits Read The License...!!!!         ##
####################################################################################################
####################################################################################################
## CODEING_SECTION_STARTED..!!!!!!!!!!!!!!!!!                                                     ##
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
    from fileinput import close
except ImportError:
    try:
        import subprocess
        import sys 
        os.system("clear")
        sys.stdout.write("\r\033[1;33mSOME DEPENDICIES COULD NOT BE INSTALLED..!!!\033[0m")
        t.sleep(2)
        sys.stdout.write("\r\033[1;32m▂▂▃▄▅▆▇▓▒░ \033[1;36mINSTALLING DEPENDICIES \033[1;32m░▒▓▇▆▅▄▃▂▂\033[0m\n\n")
        sys.stdout.write("\r\033[1;31m     Installing Requests...")
        subprocess.getoutput("pip install requests")
        sys.stdout.write("\r     \033[1;33mRequests Installed  \033[1;31m《  \033[1;32mSUCESS  \033[1;31m》\n")
        sys.stdout.write("\r\033[1;31m     Installing Colorama...")
        subprocess.getoutput("pip install colorama")
        sys.stdout.write("\r     \033[1;33mColorama Installed  \033[1;31m《  \033[1;32mSUCESS  \033[1;31m》\n")
        sys.stdout.write("\r\033[1;31m     Installing Json...")
        print("Installing Json...\n")
        sys.stdout.write("\r     \033[1;33mJson     Installed  \033[1;31m《  \033[1;32mSUCESS  \033[1;31m》\n")
        print("\033[1;34m--------------------------------------------")
        t.sleep(2)
        os.system('clear')
        print("\033[1;34mRestart MICRON_IP...!!!\n")
        print("\033[1;32mCOMMAND_01 \033[1;32m: \033[1;33mcd ..;cd MICRON_IP/micron_ip.py")
        print("\033[1;32mCOMMAND_02 \033[1;32m: \033[1;33mcd ../MICRON_IP/micron_ip.py")
        print("\033[1;32mCOMMAND_03 \033[1;32m: \033[1;33mcd ..&&cd MICRON_IP/micron_ip.py")
        exit()
    except KeyboardInterrupt:
        exit()

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
{b}╚════════════════════════╝'''+re)
    exit()
####################################################################################################
## FILE_MANAGER..!!!                                                                              ##
####################################################################################################
def manager02():
    if os.path.exists("v"):
        os.remove("v")
        manager02()
    elif os.path.exists("update"):
        os.remove("update")
        manager02()
    elif os.path.exists("../4ufvn74k.sh"):
        os.remove("../4ufvn74k.sh")
        manager02()
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
    print(f'''
{r}╔═════════════════════════════════════════════════════════════════╗
{r}║ {b}███    ███ ██  ██████ ██████   ██████  ███    ██     ██ ██████  {r}║
{r}║ {b}████  ████ ██ ██      ██   ██ ██    ██ ████   ██     ██ ██   ██ {r}║
{r}║ {b}██ ████ ██ ██ ██      ██████  ██    ██ ██ ██  ██     ██ ██████  {r}║
{r}║ {b}██  ██  ██ ██ ██      ██   ██ ██    ██ ██  ██ ██     ██ ██      {r}║
{r}║ {b}██      ██ ██  ██████ ██   ██  ██████  ██   ████     ██ ██      {r}║
{r}╠═════════════════════════════════════════════════════════════════╣
{r}║              {g}▂▃▄▅▆▇▓▒░ {lc}Created By MR.GT {g}░▒▓▇▆▅▄▃▂             {r}  ║
{r}╚═════════════════════════════════════════════════════════════════╝'''+re)

####################################################################################################
## TRACK_IP..!!!                                                                                  ##
####################################################################################################
def trackip():
    try:
        banner()
        usr=input(f"{r}╔══[{b}Enter Victim IP Address{r}]\n╚═════► {y}")
        banner()
        print(b+"WAIT JUST FEW SECONDS...!!!"+re)
        data1 = requests.get("http://ip-api.com/json/"+usr).json()
        data2 = requests.get("http://ipapi.co/"+usr+"/json/").json()
        data3 = requests.get("http://ipwho.is/"+usr).json()
        h=data3['flag']['img']
        io=h.replace("https://cdn.ipwhois.io/flags","https://tinyurl.com/ynap9h8u")
        sys.stdout.flush()
        banner()
        print(f"\n{r}╔═════════════════════════════════════════════════════════════════╗")
        print(f"{r}║                       {y}VICTIM IP DETAILS                         {r}║")
        print(f"{r}╚═════════════════════════════════════════════════════════════════╝\n"+re)
        print(f"{r}[{bo}{b}Internet_Protocol{re}{r}]═════►  {y}{data1['query']}")
        print(f"{r}[{bo}{b}Type{re}{r}]══════════════════►  {y}{data3['type']}")
        print(f"{r}[{bo}{b}Status{re}{r}]════════════════►  {y}{data1['status']}")
        print(f"{r}[{bo}{b}Sucess{re}{r}]════════════════►  {y}{data3['success']}")
        print("")
        print(f"{r}[{bo}{b}Continent{re}{r}]═════════════►  {y}{data3['continent']}")
        print(f"{r}[{bo}{b}Continent_Code{re}{r}]════════►  {y}{data2['continent_code']}")
        print(f"{r}[{bo}{b}Country{re}{r}]═══════════════►  {y}{data1['country']}")
        print(f"{r}[{bo}{b}Country_Code{re}{r}]══════════►  {y}{data1['countryCode']}")
        print("")
        print(f"{r}[{bo}{b}Country_Code_ISO3{re}{r}]═════►  {y}{data2['country_code_iso3']}")
        print(f"{r}[{bo}{b}Country_Code_TLD{re}{r}]══════►  {y}{data2['country_tld']}")
        print(f"{r}[{bo}{b}Flag_Image{re}{r}]════════════►  {y}{io}")
        print(f"{r}[{bo}{b}Flag_Emoji{re}{r}]════════════►  {y}{data3['flag']['emoji']}")
        print("")
        print(f"{r}[{bo}{b}Flag_Emoji_UNI_Code{re}{r}]═══►  {y}{data3['flag']['emoji_unicode']}")
        print(f"{r}[{bo}{b}Latitude{re}{r}]══════════════►  {y}{data2['latitude']}")
        print(f"{r}[{bo}{b}Longitude{re}{r}]═════════════►  {y}{data2['longitude']}")
        print(f"{r}[{bo}{b}Region_Name{re}{r}]═══════════►  {y}{data1['regionName']}")
        print("")
        print(f"{r}[{bo}{b}Region_Code{re}{r}]═══════════►  {y}{data2['region_code']}")
        print(f"{r}[{bo}{b}City_Name{re}{r}]═════════════►  {y}{data3['city']}")
        print(f"{r}[{bo}{b}Postal_Code{re}{r}]═══════════►  {y}{data3['postal']}")
        print(f"{r}[{bo}{b}Country_Capital{re}{r}]═══════►  {y}{data2['country_capital']}")
        print("")
        print(f"{r}[{bo}{b}Languages{re}{r}]═════════════►  {y}{data2['languages']}")
        print(f"{r}[{bo}{b}Country_Calling_Code{re}{r}]══►  {y}{data2['country_calling_code']}")
        print(f"{r}[{bo}{b}Currency{re}{r}]══════════════►  {y}{data2['currency']}")
        print(f"{r}[{bo}{b}Currency_Name{re}{r}]═════════►  {y}{data2['currency_name']}")
        print("")
        print(f"{r}[{bo}{b}IN_EU{re}{r}]═════════════════►  {y}{data2['in_eu']}")
        print(f"{r}[{bo}{b}IS_EU{re}{r}]═════════════════►  {y}{data3['is_eu']}")
        print(f"{r}[{bo}{b}ISP{re}{r}]═══════════════════►  {y}{data3['connection']['isp']}")
        print(f"{r}[{bo}{b}ASN{re}{r}]═══════════════════►  {y}{data2['asn']}")
        print("")
        print(f"{r}[{bo}{b}TimeZone{re}{r}]══════════════►  {y}{data1['timezone']}")
        print(f"{r}[{bo}{b}Time_ABBR{re}{r}]═════════════►  {y}{data3['timezone']['abbr']}")
        print(f"{r}[{bo}{b}Time_OFFSET{re}{r}]═══════════►  {y}{data3['timezone']['offset']}")
        print(f"{r}[{bo}{b}Time_UTC{re}{r}]══════════════►  {y}{data3['timezone']['utc']}")
        print("")
        print(f"{r}[{bo}{b}Time_IS_DST{re}{r}]═══════════►  {y}{data3['timezone']['is_dst']}")
        print(f"{r}[{bo}{b}Current_Time{re}{r}]══════════►  {y}{data3['timezone']['current_time']}")
        print(f"{r}[{bo}{b}Borders{re}{r}]═══════════════►  {y}{data3['borders']}")
        print("")
        print(f"{r}[{bo}{b}Connection_Domin{re}{r}]══════►  {y}{data3['connection']['domain']}")
        print(f"{r}[{bo}{b}Google_Maps{re}{r}]═══════════►  {y}https://maps.google.com/?q={data2['longitude']},{data2['latitude']}")
        print(f"\n\n{r}╔═════════════════════════════════════════════════════════════════╗")
        print(f"{r}║                        {b}[ {g}01 {b}] {y} BACK TO MAIN MENU                {r}║")
        print(f"{r}║                        {b}[ {g}02 {b}] {y} EXIT                             {r}║")
        print(f"{r}╠═════════════════════════════════════════════════════════════════╝"+re)
        nm=input(f"{r}╠══[{b}Choose An Option{r}]\n╚═════► {y}")
        if nm=='1' or nm=='01' or nm=='one' or nm=='back':
            menu()
        elif nm=='2' or nm=='02' or nm=='two' or nm=='exit':
            ex()
        else:
            print(r+"Invalid Option...!!!"+re)
            t.sleep(2)
            menu()
    except requests.exceptions.ConnectionError :
        banner()
        connection()
        trackip()
    except KeyboardInterrupt:
        ex()
    except:
        banner()
        sys.stdout.write(r+"\rInvalid IP Address...!!!"+re)
        t.sleep(2)
        sys.stdout.write(y+"\rTry Again...!!!         "+re)
        t.sleep(2)
        trackip()

####################################################################################################
## USER_IP..!!!                                                                                   ##
####################################################################################################
def userip():
    try:
        banner()
        print(b+"WAIT JUST FEW SECONDS...!!!"+re)
        usr=""
        data1 = requests.get("http://ip-api.com/json/"+usr).json()
        data2 = requests.get("http://ipapi.co/"+usr+"/json/").json()
        data3 = requests.get("http://ipwho.is/"+usr).json()
        h=data3['flag']['img']
        io=h.replace("https://cdn.ipwhois.io/flags","https://tinyurl.com/ynap9h8u")
        sys.stdout.flush()
        banner()
        print(f"\n{r}╔═════════════════════════════════════════════════════════════════╗")
        print(f"{r}║                         {y}YOUR IP DETAILS                         {r}║")
        print(f"{r}╚═════════════════════════════════════════════════════════════════╝\n"+re)
        print(f"{r}[{bo}{b}Internet_Protocol{re}{r}]═════►  {y}{data1['query']}")
        print(f"{r}[{bo}{b}Type{re}{r}]══════════════════►  {y}{data3['type']}")
        print(f"{r}[{bo}{b}Status{re}{r}]════════════════►  {y}{data1['status']}")
        print(f"{r}[{bo}{b}Sucess{re}{r}]════════════════►  {y}{data3['success']}")
        print("")
        print(f"{r}[{bo}{b}Continent{re}{r}]═════════════►  {y}{data3['continent']}")
        print(f"{r}[{bo}{b}Continent_Code{re}{r}]════════►  {y}{data2['continent_code']}")
        print(f"{r}[{bo}{b}Country{re}{r}]═══════════════►  {y}{data1['country']}")
        print(f"{r}[{bo}{b}Country_Code{re}{r}]══════════►  {y}{data1['countryCode']}")
        print("")
        print(f"{r}[{bo}{b}Country_Code_ISO3{re}{r}]═════►  {y}{data2['country_code_iso3']}")
        print(f"{r}[{bo}{b}Country_Code_TLD{re}{r}]══════►  {y}{data2['country_tld']}")
        print(f"{r}[{bo}{b}Flag_Image{re}{r}]════════════►  {y}{io}")
        print(f"{r}[{bo}{b}Flag_Emoji{re}{r}]════════════►  {y}{data3['flag']['emoji']}")
        print("")
        print(f"{r}[{bo}{b}Flag_Emoji_UNI_Code{re}{r}]═══►  {y}{data3['flag']['emoji_unicode']}")
        print(f"{r}[{bo}{b}Latitude{re}{r}]══════════════►  {y}{data2['latitude']}")
        print(f"{r}[{bo}{b}Longitude{re}{r}]═════════════►  {y}{data2['longitude']}")
        print(f"{r}[{bo}{b}Region_Name{re}{r}]═══════════►  {y}{data1['regionName']}")
        print("")
        print(f"{r}[{bo}{b}Region_Code{re}{r}]═══════════►  {y}{data2['region_code']}")
        print(f"{r}[{bo}{b}City_Name{re}{r}]═════════════►  {y}{data3['city']}")
        print(f"{r}[{bo}{b}Postal_Code{re}{r}]═══════════►  {y}{data3['postal']}")
        print(f"{r}[{bo}{b}Country_Capital{re}{r}]═══════►  {y}{data2['country_capital']}")
        print("")
        print(f"{r}[{bo}{b}Languages{re}{r}]═════════════►  {y}{data2['languages']}")
        print(f"{r}[{bo}{b}Country_Calling_Code{re}{r}]══►  {y}{data2['country_calling_code']}")
        print(f"{r}[{bo}{b}Currency{re}{r}]══════════════►  {y}{data2['currency']}")
        print(f"{r}[{bo}{b}Currency_Name{re}{r}]═════════►  {y}{data2['currency_name']}")
        print("")
        print(f"{r}[{bo}{b}IN_EU{re}{r}]═════════════════►  {y}{data2['in_eu']}")
        print(f"{r}[{bo}{b}IS_EU{re}{r}]═════════════════►  {y}{data3['is_eu']}")
        print(f"{r}[{bo}{b}ISP{re}{r}]═══════════════════►  {y}{data3['connection']['isp']}")
        print(f"{r}[{bo}{b}ASN{re}{r}]═══════════════════►  {y}{data2['asn']}")
        print("")
        print(f"{r}[{bo}{b}TimeZone{re}{r}]══════════════►  {y}{data1['timezone']}")
        print(f"{r}[{bo}{b}Time_ABBR{re}{r}]═════════════►  {y}{data3['timezone']['abbr']}")
        print(f"{r}[{bo}{b}Time_OFFSET{re}{r}]═══════════►  {y}{data3['timezone']['offset']}")
        print(f"{r}[{bo}{b}Time_UTC{re}{r}]══════════════►  {y}{data3['timezone']['utc']}")
        print("")
        print(f"{r}[{bo}{b}Time_IS_DST{re}{r}]═══════════►  {y}{data3['timezone']['is_dst']}")
        print(f"{r}[{bo}{b}Current_Time{re}{r}]══════════►  {y}{data3['timezone']['current_time']}")
        print(f"{r}[{bo}{b}Borders{re}{r}]═══════════════►  {y}{data3['borders']}")
        print("")
        print(f"{r}[{bo}{b}Connection_Domin{re}{r}]══════►  {y}{data3['connection']['domain']}")
        print(f"{r}[{bo}{b}Google_Maps{re}{r}]═══════════►  {y}https://maps.google.com/?q={data2['longitude']},{data2['latitude']}")
        print(f"\n\n{r}╔═════════════════════════════════════════════════════════════════╗")
        print(f"{r}║                        {b}[ {g}01 {b}] {y} BACK TO MAIN MENU                {r}║")
        print(f"{r}║                        {b}[ {g}02 {b}] {y} EXIT                             {r}║")
        print(f"{r}╠═════════════════════════════════════════════════════════════════╝"+re)
        nm=input(f"{r}╠══[{b}Choose An Option{r}]\n╚═════► {y}")
        if nm=='1' or nm=='01' or nm=='one' or nm=='back':
            menu()
        elif nm=='2' or nm=='02' or nm=='two' or nm=='exit':
            ex()
        else:
            print(r+"Invalid Option...!!!"+re)
            t.sleep(2)
            menu()
    except requests.exceptions.ConnectionError :
        banner()
        connection()
        userip()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## CHECK_INTERNET_CONNECTION..!!!                                                                 ##
####################################################################################################
def connection():
    try:
        requests.get('https://www.google.com')
        close()
    except requests.exceptions.ConnectionError :
        try:
            chars = "-\|/"
            for char in chars:
                sys.stdout.write("\r"+b+"Check Your Internet Connection..."+y+char+" ")
                t.sleep(0.1)
                sys.stdout.flush()
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
        i=0
        while i<6:
            chars = "-\|/"
            for char in chars:
                sys.stdout.write("\r"+b+"Restarting..."+y+char+" "+re)
                t.sleep(0.1)
                sys.stdout.flush()
            i+=1
        menu()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## UPDATE..!!!                                                                                    ##
####################################################################################################
def update():
    try:
        if not os.path.exists("../4ufvn74k.sh"):
            try:
                if not os.path.exists("update"):
                    banner()
                    connection()
                    banner()
                    print(b+"Updateing...\n"+y)
                    s=open("../4ufvn74k.sh","w")
                    s.write('''rm -rf MICRON_IP\ngit clone https://github.com/GreyTechno/MICRON_IP.git''')
                    s.close()
                    d=open("update","w")
                    d.write("cd ..\nbash 4ufvn74k.sh")
                    d.close()
                    os.system("bash update")
                    banner()
                    print("\033[1;34mRestart MICRON_IP...!!!\n")
                    print("\033[1;32mCOMMAND_01 \033[1;32m: \033[1;33mcd ..;cd MICRON_IP/micron_ip.py")
                    print("\033[1;32mCOMMAND_02 \033[1;32m: \033[1;33mcd ../MICRON_IP/micron_ip.py")
                    print("\033[1;32mCOMMAND_03 \033[1;32m: \033[1;33mcd ..&&cd MICRON_IP/micron_ip.py")
                    exit()
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
    connection()
    try:
        print("")
        sys.stdout.write(f"\r{b}[{g}*{b}]  {y}Checking_Updates..."+re)
        version = requests.get("https://raw.githubusercontent.com/GreyTechno/MICRON_IP/main/v").json()
        version = version['version']
        if version != "v 1.0" :
            sys.stdout.write(b+"\rUPDATES_ARE_AVAILABLE_VERSION_"+y+version+re)
            t.sleep(2)
            update()
        else:
            sys.stdout.write("\r"+re)
    except requests.exceptions.ConnectionError :
        connection()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## MORE..!!!                                                                                      ##
####################################################################################################
def more():
    try:
        banner()
        if os.name == 'posix':
            os.system("termux-open-url https://github.com/GeyTechno/")
        print(f'''
{r}╔═════════════════════════════════════════════════════════════════╗
{r}║                          {b}MORE...!!!              {r}               ║
{r}╠═════════════════════════════════════════════════════════════════╣
{r}║  {y}             https://tinyurl.com/26r62bk2                    {r}  ║
{r}╚═════════════════════════════════════════════════════════════════╝

{r}╔═════════════════════════════════════════════════════════════════╗
{r}║                        {b}[ {g}01 {b}] {y} BACK TO MAIN MENU                {r}║
{r}║                        {b}[ {g}02 {b}] {y} EXIT                             {r}║
{r}╠═════════════════════════════════════════════════════════════════╝''')
        nm=input(f"{r}╠══[{b}Choose An Option{r}]\n╚═════► {y}")
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
## FOLLOW..!!!                                                                                    ##
####################################################################################################
def follow():
    try:
        banner()
        if os.name == 'posix':
            os.system("termux-open-url https://instagram.com/grey_techno/")
        print(f'''
{r}╔═════════════════════════════════════════════════════════════════╗
{r}║                          {b}FOLLOW...!!!              {r}             ║
{r}╠═════════════════════════════════════════════════════════════════╣
{r}║  {y}   Github     >>  https://github.com/GeyTechno/        {r}        ║
{r}║  {y}   Instagram  >>  https://instagram.com/grey_techno/   {r}        ║
{r}╚═════════════════════════════════════════════════════════════════╝

{r}╔═════════════════════════════════════════════════════════════════╗
{r}║                        {b}[ {g}01 {b}] {y} BACK TO MAIN MENU                {r}║
{r}║                        {b}[ {g}02 {b}] {y} EXIT                             {r}║
{r}╠═════════════════════════════════════════════════════════════════╝''')
        nm=input(f"{r}╠══[{b}Choose An Option{r}]\n╚═════► {y}")
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
## MAIN_MENU..!!!                                                                                 ##
####################################################################################################
def menu():
    try:
        banner()
        print(f'''
        {b}                 [ {g}01 {b}]  {y}Track Victim IP
        {b}                 [ {g}02 {b}]  {y}Your IP
        {b}                 [ {g}03 {b}]  {y}Update
        {b}                 [ {g}04 {b}]  {y}About
        {b}                 [ {g}05 {b}]  {y}Restart
        {b}                 [ {g}06 {b}]  {y}More
        {b}                 [ {g}07 {b}]  {y}Follow
        {b}                 [ {g}08 {b}]  {y}Exit
{r}═══════════════════════════════════════════════════════════════════'''+re)
        action=input(f"{r}\n[{b}Choose An Option{r}]═════► {y}")
        if action=='1' or action=='01' or action=='one' or action=='tarckip':
            trackip()
        elif action=='2' or action=='02' or action=='two' or action=='myip':
            userip()
        elif action=='3' or action=='03' or action=='three' or action=='update':
            update()
        elif action=='4' or action=='04' or action=='four' or action=='about':
            about()
        elif action=='5' or action=='05' or action=='five' or action=='restart':
            restart()
        elif action=='6' or action=='06' or action=='six' or action=='more':
            more()
        elif action=='7' or action=='07' or action=='seven' or action=='follow':
            follow()
        elif action=='8' or action=='08' or action=='eight' or action=='exit':
                ex()
        else:
            print(r+"Invalid_Option...!!!"+re)
            t.sleep(2)
            menu()
    except KeyboardInterrupt:
        ex()

####################################################################################################
## ABOUT..!!!                                                                                     ##
####################################################################################################
def about():
    try:
        banner()
        print(f'''
{r}╔═════════════════════════════════════════════════════════════════╗
{r}║                     {b}ABOUT MICRON_IP...!!!              {r}         ║
{r}╠═════════════════════════════════════════════════════════════════╣
{r}║  {y}      This Micron_IP Is An Python Based Scripted Tool.       {r}  ║
{r}║  {y} Which Helps You Stay Safe Online By Learning About Which Of {r}  ║
{r}║  {y}          Your Personal Information Is Accessible !          {r}  ║
{r}║  {y}      Which Can Be Used To IP Lookup , DNS Lookup And        {r}  ║
{r}║  {y}         To Get Information Of Perticualar Target IP         {r}  ║
{r}║  {y}            In Just Few Steps Without Any Issue.             {r}  ║
{r}╚═════════════════════════════════════════════════════════════════╝

{r}╔═════════════════════════════════════════════════════════════════╗
{r}║                        {b}[ {g}01 {b}] {y} BACK TO MAIN MENU                {r}║
{r}║                        {b}[ {g}02 {b}] {y} EXIT                             {r}║
{r}╠═════════════════════════════════════════════════════════════════╝''')
        nm=input(f"{r}╠══[{b}Choose An Option{r}]\n╚═════► {y}")
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
## CALLING_DEF..!!!                                                                               ##
####################################################################################################
manager02()
version()
menu()