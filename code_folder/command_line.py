#!/usr/bin/env python
"""The command line system for the Choc_an System."""
import functions_list as f
import decimal as decimal


def intro():
    """The introduction text to the Choc_an system."""
    print """
            Welcome to the Choc_an system piece provided by Brian Breniser
            Here you will find the commands required to add members, providers,
            services, and create reports. Here are the commands:
            combine the first line and the second line in one word (example: addmember)
            (a)dd
                (m)ember
                (p)rovider
                (s)ervice
            (d)elete
                (m)ember
                (p)rovider
                (s)ervice
            (de)leteall
                (m)ember
                (p)rovider
                (s)ervice
            (di)splay
                (m)ember
                (p)roviderhe
                (s)ervice
            (m)odify
                (m)ember
                (p)rovider
                (s)ervice
            (p)provide
                (s)ervice
                (di)splayallservicesprovided
                (d)deleteallservices
            (r)unreports
            """


def commands():
    """The command list."""
    print """
            (a)dd
                (m)ember
                (p)rovider
                (s)ervice
            (d)elete
                (m)ember
                (p)rovider
                (s)ervice
            (de)leteall
                (m)ember
                (p)rovider
                (s)ervice
            (di)splay
                (m)ember
                (p)rovider
                (s)ervice
            (m)odify
                (m)ember
                (p)rovider
                (s)ervice
            (p)provide
                (s)ervice
                (di)splayallservicesprovided
                (d)deleteallservices
            (r)unreports
            """


def addmember():
    """the addmember function of the choc_an system."""
    name = raw_input("please enter the name of the person: ")
    number = int(raw_input("please enter the number of the person: "))
    address = raw_input("please enter the address of the person: ")
    city = raw_input("please enter the city of the person: ")
    state = raw_input("please enter the state of the person: ")
    zipcode = int(raw_input("please enter the zipcode of the person: "))
    return_code = f.member().addone(name=name, number=number, address=address, city=city, state=state, zipcode=zipcode)
    if return_code is not True:
        print return_code


def addprovider():
    """the addprovder function of the choc_an system."""
    name = raw_input("please enter the name of the person: ")
    number = int(raw_input("please enter the number of the person: "))
    address = raw_input("please enter the address of the person: ")
    city = raw_input("please enter the city of the person: ")
    state = raw_input("please enter the state of the person: ")
    zipcode = int(raw_input("please enter the zipcode of the person: "))
    return_code = f.provider().addone(name=name, number=number, address=address, city=city, state=state, zipcode=zipcode)
    if return_code is not True:
        print return_code


def addservice():
    """the addservice function of the choc_an system."""
    name = raw_input("please enter the name of the service: ")
    code = int(raw_input("please enter the code of the service: "))
    fee = decimal.Decimal(raw_input("please enter the fee of the service: "))
    return_code = f.service().addone(name=name, code=code, fee=fee)
    if return_code is not True:
        print return_code


def deletemember():
    """the delete member function of the choc_an system."""
    number = int(raw_input("please enter the number of the person you want to delete: "))
    return_code = f.member().deleteone(number=number)
    if return_code is not True:
        print return_code


def deleteprovider():
    """the delete provider function of the choc_an system."""
    number = int(raw_input("please enter the number of the person you want to delete: "))
    return_code = f.provider().deleteone(number=number)
    if return_code is not True:
        print return_code


def deleteservice():
    """the delete service function of the choc_an system."""
    number = int(raw_input("please enter the code of the service you want to delete: "))
    return_code = f.service().deleteone(code=number)
    if return_code is not True:
        print return_code


def deleteallmember():
    """the dellete all member function of the choc_an system."""
    return_code = f.member().deleteall()
    if return_code is not True:
        print return_code


def deleteallprovider():
    """the delete all provider function of the choc_an system."""
    return_code = f.provider().deleteall()
    if return_code is not True:
        print return_code


def deleteallservice():
    """the delete all service function of the choc_an system."""
    return_code = f.service().deleteall()
    if return_code is not True:
        print return_code


def displaymember():
    """the display member function of the choc_an system."""
    if f.member().display() is f.v.displayerror:
        print "there is no file to display the contents of yet, try adding some data to it first"


def displayprovider():
    """the display provider function of the choc_an system."""
    if f.provider().display() is f.v.displayerror:
        print "there is no file to display the contents of yet, try adding some data to it first"


def displayservice():
    """the display service function of the choc_an system."""
    if f.service().display() is f.v.displayerror:
        print "there is no file to display the contents of yet, try adding some data to it first"


def modifymember():
    """the modify member function of the choc_an system."""
    print "Please enter blank input if you DON'T wan't to change that input"
    print "you must enter the number of the person you are trying to modify"
    print "if you need to modify member numbers, please delete that member and start over"
    number = int(raw_input("please enter the number of the person you would like to modify: "))
    name = raw_input("please enter the name of the person: ")
    if str(name) == "":
        name = None
    address = raw_input("please enter the address of the person: ")
    if str(address) == "":
        address = None
    city = raw_input("please enter the city of the person: ")
    if str(city) == "":
        city = None
    state = raw_input("please enter the state of the person: ")
    if str(state) == "":
        state = None
    zipcode = int(raw_input("please enter the zipcode of the person: "))
    if str(zipcode) == "":
        zipcode = None
    return_code = f.member().modifyone(name=name, number=number, address=address, city=city, state=state, zipcode=zipcode)
    if return_code is not True:
        print return_code


def modifyprovider():
    """the modify provider function of the choc_an system."""
    print "Please enter blank input if you DON'T wan't to change that input"
    print "you must enter the number of the person you are trying to modify"
    print "if you need to modify provider numbers, please delete that provider and start over"
    number = int(raw_input("please enter the number of the person you would like to modify: "))
    name = raw_input("please enter the name of the person: ")
    if str(name) == "":
        name = None
    address = raw_input("please enter the address of the person: ")
    if str(address) == "":
        address = None
    city = raw_input("please enter the city of the person: ")
    if str(city) == "":
        city = None
    state = raw_input("please enter the state of the person: ")
    if str(state) == "":
        state = None
    zipcode = int(raw_input("please enter the zipcode of the person: "))
    if str(zipcode) == "":
        zipcode = None
    return_code = f.provider().modifyone(name=name, number=number, address=address, city=city, state=state, zipcode=zipcode)
    if return_code is not True:
        print return_code


def modifyservice():
    """the modify service function of the choc_an system."""
    print "Please enter blank input if you DON'T wan't to change that input"
    print "you must enter the code of the person you are trying to modify"
    print "if you need to modify service codes, please delete that member and start over"
    code = int(raw_input("please enter the code of the person you would like to modify: "))
    name = raw_input("please enter the name of the person: ")
    if str(name) == "":
        name = None
    fee = decimal.Decimal(raw_input("please enter the zipcode of the person: "))
    if str(fee) == "":
        fee = None
    return_code = f.service().modifyone(code=code, name=name, fee=fee)
    if return_code is not True:
        print return_code


def runreports():
    """run all the reports of the choc_an system."""
    return_code = f.report().summaryreport()
    if return_code is not True:
        return return_code


def provideservice():
    """the add weeklyservices function of the choc_an system."""
    dmonth = int(raw_input("please enter the month of the service provided today: "))
    dday = int(raw_input("please enter the day of the service provided today: "))
    dyear = int(raw_input("please enter the year of the service provided today: "))
    pnumber = int(raw_input("please enter the number of the provider today: "))
    mnumber = int(raw_input("please enter the number of the member today: "))
    code = int(raw_input("please enter the code of the service provided today: "))
    comments = raw_input("please enter any comments: ")
    return_code = f.weeklyservice().addone(dmonth=dmonth, dday=dday, dyear=dyear, pnumber=pnumber, mnumber=mnumber, code=code, comments=comments)
    if return_code is not True:
        print return_code


def displayprovidedservices():
    """the display weekly services function of the choc_an system."""
    if f.member().display() is f.v.displayerror:
        print "there is no file to display the contents of yet, try adding some data to it first"


def deleteprovidedservices():
    """the delete all provider function of the choc_an system."""
    return_code = f.provider().deleteall()
    if return_code is not True:
        print return_code


def main():
    """The commands of the Choc_an system."""
    intro()
    command = None
    while command is not "exit":
        command = str(raw_input("Please enter your command (commands for a list of commands): "))
        if command == "commands":
            commands()
        elif command == "addmember" or command == "addmembers" or command == "am":
            try:
                addmember()
            except:
                print "something went wrong"
        elif command == "addprovider" or command == "addproviders" or command == "ap":
            try:
                addprovider()
            except:
                print "something went wrong"
        elif command == "addservice" or command == "addservices" or command == "as":
            try:
                addservice()
            except:
                print "something went wrong"
        elif command == "deletemember" or command == "deletemembers " or command == "dm":
            try:
                deletemember()
            except:
                print "something went wrong"
        elif command == "deleteprovider" or command == "deleteproviders" or command == "dp":
            try:
                deleteprovider()
            except:
                print "something went wrong"
        elif command == "deleteservice" or command == "deleteservices" or command == "ds":
            try:
                deleteservice()
            except:
                print "something went wrong"
        elif command == "deleteallmember" or command == "deleteallmembers" or command == "dem":
            accept = raw_input("are you sure you want to delete EVERYONE? (y/n)")
            if accept == "y":
                try:
                    deleteallmember()
                except:
                    print "something went wrong"
            else:
                continue
        elif command == "deleteallprovider" or command == "deleteallproviders" or command == "dep":
            accept = raw_input("are you sure you want to delete EVERYONE? (y/n)")
            if accept == "y":
                try:
                    deleteallprovider()
                except:
                    print "something went wrong"
            else:
                continue
        elif command == "deleteallservice" or command == "deleteallservices" or command == "des":
            accept = raw_input("are you sure you want to delete EVERYONE? (y/n)")
            if accept == "y":
                try:
                    deleteallservice()
                except:
                    print "something went wrong"
            else:
                continue
        elif command == "displaymember" or command == "displaymembers" or command == "dim":
            try:
                displaymember()
            except:
                print "something went wrong"
        elif command == "displayprovider" or command == "displayproviders" or command == "dip":
            try:
                displayprovider()
            except:
                print "something went wrong"
        elif command == "displayservice" or command == "displayservices" or command == "dis":
            try:
                displayservice()
            except:
                print "something went wrong"
        elif command == "modifymember" or command == "modifymembers" or command == "mm":
            try:
                modifymember()
            except:
                print "something went wrong"
        elif command == "modifyprovider" or command == "modifyproviders" or command == "mp":
            try:
                modifyprovider()
            except:
                print "something went wrong"
        elif command == "modifyservice" or command == "modifyservices" or command == "ms":
            try:
                modifyservice()
            except:
                print "something went wrong"
        elif command == "runreports" or command == "run" or command == "r":
            try:
                runreports()
            except:
                print "something went wrong"
        elif command == "provideservice" or command == "provide" or command == "ps":
            try:
                provideservice()
            except:
                print "something went wrong"
        elif command == "displayprovidedservices" or command == "displayprovidedservice" or command == "pdi":
            try:
                displayprovidedservices()
            except:
                print "something went wrong"
        elif command == "deleteprovidedservices" or command == "deleteprovidedservices" or command == "pd":
            try:
                deleteprovidedservices()
            except:
                print "something went wrong"
        elif command == "exit" or command == "quit" or command == "q":
            break
        else:
            print "no command recognized"


main()
