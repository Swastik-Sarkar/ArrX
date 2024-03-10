import os
import ipinfo

def ipa(enteredData):
    key = "KEY" #Get your key for ipinfo website
    h = ipinfo.getHandler(key)
    dt = h.getDetails(enteredData)
    return dt.all

def exitProgram():
    exitQuestion = input("Exit? (y=yes, n=no) : ")
    if exitQuestion == "n":
        os.system("cls")
        main()
    elif exitQuestion == "y":
        print("Exiting Application")
        exit()
    else:
        print("Expected answers : 'y' or 'n'")
        exitProgram()

def main():
    os.system("cls")
    print("ArrX IP Lookup\n") 
    try:
        enteredData = input("Enter IP : ")
        r = ipa(enteredData)
    except ValueError:
        print(f"{enteredData} is not a valid ipv4 or ipv6 address.")
        exitProgram()
    print("=========================\nGathered info :\n=========================\n\n")
    for key, value in r.items():
        print(f"{key} : {value}")
    exitProgram()
   
if __name__ == "__main__":
    main()
