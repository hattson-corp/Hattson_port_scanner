import os

countryName = input("[*] Enter the country name >>> ")
path = input("[*] Enter the ip rage file path >>> ")
mainIpFile = open(f"{path}", "r")

try:
    os.mkdir(f"{countryName}")
    os.chdir(f"{countryName}")
except:
    os.chdir(f"{countryName}")

nameNum = 1
def existsCeck(num):
    exists_flag = True
    while exists_flag:
        checkFile = os.path.isfile("1")
        if checkFile:
            num += 1
            continue
        elif not checkFile:
            exists_flag = False
            return num


nameNum = existsCeck(nameNum)
file = open(f"{countryName+str(nameNum)}", "w+")
file.close()

counter = 1
for line in mainIpFile.readlines():
    line = line.strip()
    file = open(f"{countryName+str(nameNum)}", "a")
    file.write(f"{line}\n")
    file.close()
    counter += 1
    if counter == 15:
        nameNum += 1
        print(f"[+] file {nameNum} is made")
        counter = 1



print("[+]all done !!!")







