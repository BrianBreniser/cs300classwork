"""The command line system for the Choc_an System."""
import functions_list as f


def intro():
    """The introduction text to the Choc_an system."""
    print """
            Welcome to the Choc_an system piece provided by Brian Breniser
            Here you will find the commands required to add members, providers,
            services, and create reports. Here are the commands:
            add
                members
                providers
                services
            delete
                members
                providers
                services
            deleteall
                members
                providers
                services
            display
                members
                providers
                services
            modify
                members
                providers
                services
            create
                memberreport
                providerreport
                servicereport
            """


def help():
    """The command list."""
    print """
            add
                members
                providers
                services
            delete
                members
                providers
                services
            deleteall
                members
                providers
                services
            display
                members
                providers
                services
            modify
                members
                providers
                services
            create
                memberreport
                providerreport
                servicereport
            """


def addmember():
    """the addmember function of the choc_an system."""
    f.member()


def addprovider():
    """the addprovder function of the choc_an system."""
    f.provider()


def addservice():
    """the addservice function of the choc_an system."""
    f.service()


def deletemember():
    """the delete member function of the choc_an system."""
    f.member()


def deleteprovider():
    """the delete provider function of the choc_an system."""
    f.provider()


def deleteservice():
    """the delete service function of the choc_an system."""
    f.service()


def deleteallmember():
    """the dellete all member function of the choc_an system."""
    f.member()


def deleteallprovider():
    """the delete all provider function of the choc_an system."""
    f.provider()


def deleteallservice():
    """the delete all service function of the choc_an system."""
    f.service()


def displaymember():
    """the display member function of the choc_an system."""
    f.member()


def displayprovider():
    """the display provider function of the choc_an system."""
    f.provider()


def displayservice():
    """the display service function of the choc_an system."""
    f.service()


def modifymember():
    """the modify member function of the choc_an system."""
    f.member()


def modifyprovider():
    """the modify provider function of the choc_an system."""
    f.provider()


def modifyservice():
    """the modify service function of the choc_an system."""
    f.service()


def main():
    """The commands of the Choc_an system."""
    intro()
    command = None
    while command is not "exit":
        command = input("Please enter your command (help for a list of commands): ")
        if command == "help":
            help()
        if command == "addmember":
            addmember()
        if command == "addprovider":
            addprovider()
        if command == "addservice":
            addservice()
        if command == "deletemember":
            deletemember()
        if command == "deleteprovider":
            deleteprovider()
        if command == "deleteservice":
            deleteservice()
        if command == "deleteallmember":
            deleteallmember()
        if command == "deleteallprovider":
            deleteallprovider()
        if command == "deleteallservice":
            deleteallservice()
        if command == "displaymember":
            displaymember()
        if command == "displayprovider":
            displayprovider()
        if command == "displayservice":
            displayservice()
        if command == "modifymember":
            modifymember()
        if command == "modifyprovider":
            modifyprovider()
        if command == "modifyservice":
            modifyservice()


main()
