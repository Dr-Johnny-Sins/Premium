import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[1;97m [\x1b[38;5;48m•\033[1;97m] \x1b[38;5;48mJoin Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/BmxmNHAMjLj5i59vqB2uKw')
tokyo=platform.architecture()[0]
if tokyo=="32bit":
    os.system('clear')
    print('\033[1;97m [\x1b[38;5;48m•\033[1;97m] \x1b[38;5;196m32 Bit Device Not Working')
elif tokyo=="64bit":
    __import__("tokyo")
