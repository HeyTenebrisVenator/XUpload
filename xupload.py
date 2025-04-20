from multiprocessing import Pool
import requests
from colorama import Fore

file = input(Fore.GREEN + "Where is the file with the URLs  >>  " + Fore.RESET)
try:
    file = open(file, 'r').readlines()
except:
    print(Fore.RED + "Error opening the file!" + Fore.RESET)
    quit()
save = input(Fore.GREEN + "Where do you want to save the output? leave in blank if you don't want to save  >>   " + Fore.RESET)

if save != "":
    try:
        open(save, 'w').write("")
    except:
        print(Fore.RED + "Error!" + Fore.RESET)
        quit()

try:
    processes = int(input(Fore.GREEN + "How many processes do you want? (Recomended: 4)  >>  " + Fore.RESET))
    if processes == "":
        processes = 4
except:
    print(Fore.RED + "Error! the value must be an int" + Fore.RESET)
    quit()

def requester(url):
    already_printed = False
    url = url.replace("\n", '')
    req = requests.get(url).text.split(">")
    for line in req:
        if "<input" in line and "type=\"file\"" in line or "<input type=\'file\'" in line:
            if already_printed == False:
                if save != "" and save != " " and save != None:
                    open(save, "a").write("\n" + url)
                print(url)
                already_printed = True
try:
    with Pool(processes=processes) as pool:
        pool.map(requester, file)
except:
    pass
