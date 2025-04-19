from multiprocessing import Pool
import requests
import sys

file = input("Where is the file with the URLs  >>  ")
try:
    file = open(file, 'r').readlines()
except:
    print("Error opening the file!")
    quit()
save = input("Where do you want to save the output? leave in blank if you don't want to save  >>  ")


open('urls.txt', 'r').readlines()
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
    with Pool(processes=4) as pool:
        pool.map(requester, file)
except:
    pass
