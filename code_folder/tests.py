#! /usr/bin/env python

import functions_list as f
from os import path, remove
from json import load

# tests of member() class -------------------------------------------------------


def addmembertest():
    """ testing member functions. """
    # clear memberlist file
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)

    # test to see if adding from empty list works
    assert f.member().addmember(name="joe", number="12345678", address="101 n whatever street", city="portland", state="OR", zipcode="12345") is True
    fp = open(f.v.memberlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "joe"
    assert mylist[0]["number"] == "12345678"
    assert mylist[0]["address"] == "101 n whatever street"
    assert mylist[0]["city"] == "portland"
    assert mylist[0]["state"] == "OR"
    assert mylist[0]["zipcode"] == "12345"

    # test to see if addine a second one works

    assert f.member().addmember(name="jeff", number="123456", address="new address", city="greshem", state="WA", zipcode="543") is True
    fp = open(f.v.memberlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[1]["name"] == "jeff"
    assert mylist[1]["number"] == "123456"
    assert mylist[1]["address"] == "new address"
    assert mylist[1]["city"] == "greshem"
    assert mylist[1]["state"] == "WA"
    assert mylist[1]["zipcode"] == "543"

    assert f.member().addmember(name="bob", number="123456", address="bob", city="bob", state="OR", zipcode="bob") is f.v.memberalreadyfound

    assert f.member().addmember(name="bob", address="bob", city="bob", state="OR", zipcode="bob") is f.v.missingdata

    assert f.member().addmember(name="bob", number="1234567890", address="bob", city="bob", state="OR", zipcode="bob") is f.v.toolongdata

    # clean up after test
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)


def displaymembertest():
    """ testing display function. """
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)  # remove file if exists
    assert f.member().display() == f.v.memberfileerror
    fp = open(f.v.memberlist, 'w+b')  # create empty file
    fp.close()  # close 'cuz we don't really need it
    assert f.member().display() == f.v.displayerror
    # commented out display test since I don't want to see it every time, uncomment to test
    # f.member().addmember(name="joe", number="12345678", address="101 n whatever street", city="portland", state="OR", zipcode="12345")
    # f.member().addmember(name="jeff", number="9876543", address="new address", city="greshem", state="WA", zipcode="543")
    # assert f.member().display() == True


def deletealltest():
    """ test delete all funciton. """
    f.member().addmember(name="joe", number="12345678", address="101 n whatever street", city="portland", state="OR", zipcode="12345")
    f.member().addmember(name="jeff", number="9876543", address="new address", city="greshem", state="WA", zipcode="543")
    assert f.member().deleteall() is True
    assert f.member().display() is f.v.displayerror

# run main----------------------------------------------------


def main():
    """ main testing function. """
    addmembertest()
    displaymembertest()
    deletealltest()


# done with main

main()
