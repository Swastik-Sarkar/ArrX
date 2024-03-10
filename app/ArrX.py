import os
import ipinfo
import ipaddress
import socket
import time
import sys

def ipa(enteredData):
    key = "KEY" #Get Your Own Key Form ipinfo.
    h = ipinfo.getHandler(key)
    dt = h.getDetails(enteredData)
    return dt.all

def resolve_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        print(f"\nCould not resolve domain: {domain}")
        return None

def exitProgram():
    while True:
        exitQuestion = input("\nExit? (y=yes, n=no) : ").lower()
        if exitQuestion == "n":
            os.system("cls" if os.name == "nt" else "clear")
            main()
        elif exitQuestion == "y":
            print("Exiting Application")
            exit()
        else:
            print("Expected answers: 'y' or 'n'")

def animate_loading():
    chars = "/—\|"
    for char in chars:
        sys.stdout.write('\r' + 'Resolving IP address or domain... ' + char)
        sys.stdout.flush()
        time.sleep(0.1)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print("ArrX IP Lookup\n[GitHub : https://www.github.com/Swastik-Sarkar/ArrX]\n") 
    enteredData = input("Enter IP address or domain: ").strip()
    if not enteredData:
        print("\nPlease enter a valid IP address or domain.")
        exitProgram()
    
    animate_loading()
    try:
        ipaddress.ip_address(enteredData)
    except ValueError:
        ip_address = resolve_domain(enteredData)
        if ip_address is None:
            print(f"Invalid IP address or domain: {enteredData}")
            exitProgram()
    else:
        ip_address = enteredData
    
    print("\n=========================")
    print("Gathered info:")
    print("=========================\n")
    info = ipa(ip_address)
    for key, value in info.items():
        print(f"{key.capitalize()}: {value}")
    exitProgram()

if __name__ == "__main__":
    main()
