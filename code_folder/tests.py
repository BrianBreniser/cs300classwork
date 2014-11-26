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
    assert f.member().addmember(name="joe", number="0123456789", address="101 n whatever street", city="portland", state="OR", zip="912345") == True
    fp = open(f.v.memberlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "joe"
    assert mylist[0]["number"] == "0123456789"
    assert mylist[0]["address"] == "101 n whatever street"
    assert mylist[0]["city"] == "portland"
    assert mylist[0]["state"] == "OR"
    assert mylist[0]["zip"] == "912345"

    # test to see if addine a second one works

    assert f.member().addmember(name="jeff", number="987654321", address="you better get this right", city="greshem", state="why not", zip="74635273849") == True
    fp = open(f.v.memberlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[1]["name"] == "jeff"
    assert mylist[1]["number"] == "987654321"
    assert mylist[1]["address"] == "you better get this right"
    assert mylist[1]["city"] == "greshem"
    assert mylist[1]["state"] == "why not"
    assert mylist[1]["zip"] == "74635273849"

    # clean up after tes
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
    # f.member().addmember(name="joe", number="0123456789", address="101 n whatever street", city="portland", state="OR", zip="912345")
    # f.member().addmember(name="jeff", number="987654321", address="you better get this right", city="greshem", state="why not", zip="74635273849")
    # assert f.member().display() == True


def deletealltest():
    """ test delete all funciton. """
    f.member().addmember(name="joe", number="0123456789", address="101 n whatever street", city="portland", state="OR", zip="912345")
    f.member().addmember(name="jeff", number="987654321", address="you better get this right", city="greshem", state="why not", zip="74635273849")
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
