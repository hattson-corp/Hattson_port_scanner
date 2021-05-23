#!/usr/bin/env pyhton3
import os
import socket as sc
import argparse


# 
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--terminal", help="for activate this mode (1) disable (0)", type=int, choices=[0, 1], required=True)
parser.add_argument("-P", "--programpath", help="the path of the ip checker program ")
parser.add_argument("-c", "--country",  help="the country name it should be the same with the ip range file name without the number.")
parser.add_argument("-a", "--path", help="the path of ip rage .")
parser.add_argument("-A", "--PATH", help="the path and rage like (path-usa1-1-4) it mean usa1 usa2 usa3 usa4 .")
parser.add_argument("-p", "--port", help="the port for scanning .", type=int)
parser.add_argument("-v", "--visible", help="this option make ethe down try's visible 0 disable and 1 for activate it 1 by default .", choices=[0, 1], type=int, default=1)
parser.add_argument("-V", "--voice", help="active(1) or disable(0) the voice it's disabled by default .", type=int, choices=[0, 1], default=0)
args = parser.parse_args()


terminalMode_flag = True
if args.terminal == 0:
    terminalMode_flag = False
elif args.terminal == 1:
    terminalMode_flag = True
    if terminalMode_flag:
        global path
        global port
        global multiPath
        global countryName
        global programPath
        programPath = args.programpath
        countryName = args.country
        path = args.path
        port = args.port
        multiPath = args.PATH

if args.visible == 1:
    visiability_flag = True
else:
    visiability_flag = False

multiIpRange = False
singleIpRange = False

if args.PATH != None:
    multiIpRange = True
else:
    multiIpRange = False

if args.path != None:
    singleIpRange = True
else:
    singleIpRange = False


if args.voice:
    voice_flag = True
else:
    voice_flag = False

def NoneTerminal():
    #banner
    print("HATTSONAPK")
    programPath = input("[*] Enter the program path >>>")
    countryName = input("[*] enter the country name >>> ")
    path = input("[*] Enter the ip range file path >>> ")
    port = int(input("[*] Enter the port for scanning >>> "))

if not terminalMode_flag:
    NoneTerminal()

def ROOT(ipPath):
    try:
        os.mkdir("result")
    except:
        pass
    os.chdir("result")
    file_check = os.path.isfile("openIps")
    exists_flag = False
    if file_check:
        exists_flag = True
        result = open("openIps", "a")
    if not file_check:
        exists_flag = False
        result = open("openIps", "w+")
        result.close()
        result = open("openIps", "a")

    def ipChecker(ip, port):
        s = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, port))
            s.shutdown(2)
            print(f"[+]ip {ip} is up and open for attack !")
            try:
                if args.voice:
                    os.system("espeak 'find'")
            except:
                pass
            return True
        except:
            if args.visible:
                print(f"[X]ip {ip} is down!\r", end="")
            return False
        finally:
            s.close()


    ip_file = open(f"{ipPath}", "r")
    def ipMaker():
        for line in ip_file.readlines():
            line = line.strip()
            line = line.split("-")
            ip1 = line[0]
            ip1 = ip1.split(".")
            ip2 = line[1]
            ip2 = ip2.split(".")

        #if statements
            if int(ip1[1]) == int(ip2[1]):
                if int(ip1[2]) == int(ip2[2]):
                    if int(ip1[3]) == int(ip2[3]):
                        checkip  = f"{ip2[0]}.{ip2[1]}.{ip2[2]}.{ip2[3]}"
                        if ipChecker(checkip, port):
                            result = open("openIps", "a")
                            result.write(f"{checkip}\n")
                            #
                            result.close()
                            result = open("openIps", "a")
            if int(ip1[1]) == int(ip2[1]):
                if int(ip1[2]) == int(ip2[2]):
                    if int(ip1[3]) != int(ip2[3]):
                        for ip in range( int(ip1[3]), 256):
                            checkip = f"{ip2[0]}.{ip2[1]}.{ip2[2]}.{ip}"
                            if ipChecker(checkip, port):
                                result = open("openIps", "a")
                                result.write(f"{checkip}\n")
                                #
                                result.close()
                                result = open("openIps","a")
            if int(ip1[1]) == int(ip2[1]):
                if int(ip1[2]) != int(ip2[2]):
                    for ip3 in range(int(ip1[2]), 256):
                        for ip4 in range( 0, 256):
                            checkip = f"{ip2[0]}.{ip2[1]}.{ip3}.{ip4}"
                            if ipChecker(checkip, port):
                                result = open("openIps", "a")
                                result.write(f"{checkip}\n")
                                #
                                result.close()
                                result = open("openIps","a")
            if int(ip1[1]) != int(ip2[1]):
                for ip_2 in range(int(ip1[1]), 256):
                    for ip3 in range(0, 256):
                        for ip4 in range(0, 256):
                            checkip = f"{ip2[0]}.{ip_2}.{ip3}.{ip4}"
                            if ipChecker(checkip, port):
                                result = open("openIps", "a")
                                result.write(f"{checkip}\n")
                                #
                                result.close()
                                result = open("openIps","a")


    ipMaker()
    try:
        os.system("wc -l result/opneIps")
    except:
        pass
    os.remove(ipPath)
    print("\n[+]all done and ^ ips founded for attack ! \n")

if singleIpRange:
    ipPath = path
    ROOT(ipPath)
if multiIpRange:
    multiPath = multiPath.split("-")
    multiPathStart = multiPath[2]
    multiPathEnd = multiPath[3]
    multiIpPath = multiPath[0]
    workerCount = 0
    print("[*] Starting the multi worker mode .....")
    for check in range(int(multiPathStart), int(multiPathEnd)):
        os.system(f"python3 {programPath} -c {countryName} -p {port} -a {multiIpPath}{countryName}{check} -t 1 & ")
        workerCount += 1
        print(f"worker {workerCount} start it work")

