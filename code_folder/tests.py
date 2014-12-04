#! /usr/bin/env python

import functions_list as f
from os import path, remove
from json import load

# tests of member() class -------------------------------------------------------


def addonemembertest():
    """ testing member functions. """
    # clear memberlist file
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)

    # test to see if adding from empty list works
    assert f.member().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345) is True
    fp = open(f.v.memberlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "joe"
    assert mylist[0]["number"] == 12345678
    assert mylist[0]["address"] == "101 n whatever street"
    assert mylist[0]["city"] == "portland"
    assert mylist[0]["state"] == "OR"
    assert mylist[0]["zipcode"] == 12345

    # test to see if addine a second one works

    assert f.member().addone(name="jeff", number=123456, address="new address", city="greshem", state="WA", zipcode=543) is True
    fp = open(f.v.memberlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[1]["name"] == "jeff"
    assert mylist[1]["number"] == 123456
    assert mylist[1]["address"] == "new address"
    assert mylist[1]["city"] == "greshem"
    assert mylist[1]["state"] == "WA"
    assert mylist[1]["zipcode"] == 543

    assert f.member().addone(name="bob", number=123456, address="bob", city="bob", state="OR", zipcode=123) is f.v.alreadyfound

    assert f.member().addone(name="bob", address="bob", city="bob", state="OR", zipcode=123) is f.v.missingdata

    assert f.member().addone(name="bob", number=1234567890, address="bob", city="bob", state="OR", zipcode=123) is f.v.toolongdata

    # clean up after test
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)


def displaymembertest():
    """ testing display function. """
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)  # remove file if exists
    assert f.member().display() == f.v.fileerror
    fp = open(f.v.memberlist, 'w+b')  # create empty file
    fp.close()  # close 'cuz we don't really need it
    assert f.member().display() == f.v.displayerror
    # commented out display test since I don't want to see it every time, uncomment to test
    f.member().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345)
    f.member().addone(name="jeff", number=9876543, address="new address", city="greshem", state="WA", zipcode=543)
    assert f.member().display() is True

    # clean up after test
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)


def deleteallmembertest():
    """ test delete all member function. """
    f.member().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345)
    f.member().addone(name="jeff", number=9876543, address="new address", city="greshem", state="WA", zipcode=543)
    assert f.member().deleteall() is True
    assert f.member().display() is f.v.displayerror

    # clean up after test
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)


def deleteonemembertest():
    """ test delete one member function. """
    f.member().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345)
    f.member().addone(name="jeff", number=9876543, address="new address", city="greshem", state="WA", zipcode=543)
    f.member().addone(name="jeff", number=6496743, address="my address0", city="greshem", state="WA", zipcode=543)
    assert f.member().deleteone(9876543) is True
    assert f.member().deleteone("1029384") is f.v.nonefound
    assert f.member().deleteone(None) is f.v.missingdata

    fp = open(f.v.memberlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "joe"
    assert mylist[0]["number"] == 12345678
    assert mylist[0]["address"] == "101 n whatever street"
    assert mylist[0]["city"] == "portland"
    assert mylist[0]["state"] == "OR"
    assert mylist[0]["zipcode"] == 12345

    assert mylist[1]["name"] == "jeff"
    assert mylist[1]["number"] == 6496743
    assert mylist[1]["address"] == "my address0"
    assert mylist[1]["city"] == "greshem"
    assert mylist[1]["state"] == "WA"
    assert mylist[1]["zipcode"] == 543

    # clean up after test
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)


def modifyonemembertest():
    """ Test modify member function. """
    f.member().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345)
    f.member().addone(name="jeff", number=6496743, address="my address0", city="greshem", state="WA", zipcode=543)
    f.member().addone(name="mark", number=12345610, address="101 n whatever street", city="portland", state="OR", zipcode=12345)

    assert f.member().modifyone(number=12345678) is True
    assert f.member().modifyone(number=6496743, name="foobar") is True
    assert f.member().modifyone(number=12345610, name="mark0", address="101 n whatever street0", city="portland0", state="OR", zipcode=12340) is True

    assert f.member().modifyone(number=1234569, name="mark", state="WA") is f.v.nonefound
    assert f.member().modifyone(number=None, name="sarah", state="NY") is f.v.missingdata

    fp = open(f.v.memberlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "joe"
    assert mylist[0]["number"] == 12345678
    assert mylist[0]["address"] == "101 n whatever street"
    assert mylist[0]["city"] == "portland"
    assert mylist[0]["state"] == "OR"
    assert mylist[0]["zipcode"] == 12345

    assert mylist[1]["name"] == "foobar"
    assert mylist[1]["number"] == 6496743
    assert mylist[1]["address"] == "my address0"
    assert mylist[1]["city"] == "greshem"
    assert mylist[1]["state"] == "WA"
    assert mylist[1]["zipcode"] == 543

    assert mylist[2]["name"] == "mark0"
    assert mylist[2]["number"] == 12345610
    assert mylist[2]["address"] == "101 n whatever street0"
    assert mylist[2]["city"] == "portland0"
    assert mylist[2]["state"] == "OR"
    assert mylist[2]["zipcode"] == 12340

    # clean up after test
    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)


# tests of provider() class -------------------------------------------------------


def addoneprovidertest():
    """ testing member functions. """
    # clear memberlist file
    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)

    # test to see if adding from empty list works
    assert f.provider().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345) is True
    fp = open(f.v.providerlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "joe"
    assert mylist[0]["number"] == 12345678
    assert mylist[0]["address"] == "101 n whatever street"
    assert mylist[0]["city"] == "portland"
    assert mylist[0]["state"] == "OR"
    assert mylist[0]["zipcode"] == 12345

    # test to see if addine a second one works

    assert f.provider().addone(name="jeff", number=123456, address="new address", city="greshem", state="WA", zipcode=543) is True
    fp = open(f.v.providerlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[1]["name"] == "jeff"
    assert mylist[1]["number"] == 123456
    assert mylist[1]["address"] == "new address"
    assert mylist[1]["city"] == "greshem"
    assert mylist[1]["state"] == "WA"
    assert mylist[1]["zipcode"] == 543

    assert f.provider().addone(name="bob", number=123456, address="bob", city="bob", state="OR", zipcode=123) is f.v.alreadyfound

    assert f.provider().addone(name="bob", address="bob", city="bob", state="OR", zipcode="bob") is f.v.missingdata

    assert f.provider().addone(name="bob", number=1234567890, address="bob", city="bob", state="OR", zipcode=123) is f.v.toolongdata

    # clean up after test
    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)


def displayprovidertest():
    """ testing display function. """
    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)  # remove file if exists
    assert f.provider().display() == f.v.fileerror
    fp = open(f.v.providerlist, 'w+b')  # create empty file
    fp.close()  # close 'cuz we don't really need it
    assert f.provider().display() == f.v.displayerror
    # commented out display test since I don't want to see it every time, uncomment to test
    f.provider().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345)
    f.provider().addone(name="jeff", number=9876543, address="new address", city="greshem", state="WA", zipcode=543)
    assert f.provider().display() is True

    # clean up after test
    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)


def deleteallprovidertest():
    """ test delete all member function. """
    f.provider().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345)
    f.provider().addone(name="jeff", number=9876543, address="new address", city="greshem", state="WA", zipcode=543)
    assert f.provider().deleteall() is True
    assert f.provider().display() is f.v.displayerror

    # clean up after test
    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)


def deleteoneprovidertest():
    """ test delete one member function. """
    f.provider().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345)
    f.provider().addone(name="jeff", number=9876543, address="new address", city="greshem", state="WA", zipcode=543)
    f.provider().addone(name="jeff", number=6496743, address="my address0", city="greshem", state="WA", zipcode=543)
    assert f.provider().deleteone(9876543) is True
    assert f.provider().deleteone("1029384") is f.v.nonefound
    assert f.provider().deleteone(None) is f.v.missingdata

    fp = open(f.v.providerlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "joe"
    assert mylist[0]["number"] == 12345678
    assert mylist[0]["address"] == "101 n whatever street"
    assert mylist[0]["city"] == "portland"
    assert mylist[0]["state"] == "OR"
    assert mylist[0]["zipcode"] == 12345

    assert mylist[1]["name"] == "jeff"
    assert mylist[1]["number"] == 6496743
    assert mylist[1]["address"] == "my address0"
    assert mylist[1]["city"] == "greshem"
    assert mylist[1]["state"] == "WA"
    assert mylist[1]["zipcode"] == 543

    # clean up after test
    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)


def modifyoneprovidertest():
    """ Test modify member function. """
    f.provider().addone(name="joe", number=12345678, address="101 n whatever street", city="portland", state="OR", zipcode=12345)
    f.provider().addone(name="jeff", number=6496743, address="my address0", city="greshem", state="WA", zipcode=543)
    f.provider().addone(name="mark", number=12345610, address="101 n whatever street", city="portland", state="OR", zipcode=12345)

    assert f.provider().modifyone(number=12345678) is True
    assert f.provider().modifyone(number=6496743, name="foobar") is True
    assert f.provider().modifyone(number=12345610, name="mark0", address="101 n whatever street0", city="portland0", state="OR", zipcode=12340) is True

    assert f.provider().modifyone(number=1234569, name="mark", state="WA") is f.v.nonefound
    assert f.provider().modifyone(number=None, name="sarah", state="NY") is f.v.missingdata

    fp = open(f.v.providerlist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "joe"
    assert mylist[0]["number"] == 12345678
    assert mylist[0]["address"] == "101 n whatever street"
    assert mylist[0]["city"] == "portland"
    assert mylist[0]["state"] == "OR"
    assert mylist[0]["zipcode"] == 12345

    assert mylist[1]["name"] == "foobar"
    assert mylist[1]["number"] == 6496743
    assert mylist[1]["address"] == "my address0"
    assert mylist[1]["city"] == "greshem"
    assert mylist[1]["state"] == "WA"
    assert mylist[1]["zipcode"] == 543

    assert mylist[2]["name"] == "mark0"
    assert mylist[2]["number"] == 12345610
    assert mylist[2]["address"] == "101 n whatever street0"
    assert mylist[2]["city"] == "portland0"
    assert mylist[2]["state"] == "OR"
    assert mylist[2]["zipcode"] == 12340

    # clean up after test
    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)

# tests of service() class -------------------------------------------------------


def addoneservicetest():
    """ testing service functions. """
    # clear memberlist file
    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)

    # test to see if adding from empty list works
    assert f.service().addone(name="massage", code=12345678, fee=400.00) is True
    fp = open(f.v.servicelist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "massage"
    assert mylist[0]["code"] == 12345678
    assert mylist[0]["fee"] == "400"

    # test to see if addine a second one works

    assert f.service().addone(name="jeff", code=123456, fee=543) is True
    fp = open(f.v.servicelist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[1]["name"] == "jeff"
    assert mylist[1]["code"] == 123456
    assert mylist[1]["fee"] == "543"

    assert f.service().addone(name="bob", code=123456, fee=123) is f.v.alreadyfound

    assert f.service().addone(name="bob") is f.v.missingdata

    assert f.service().addone(name="bob", code=121212, fee=1234345677) is f.v.toolongdata

    # clean up after test
    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)


def displayservicetest():
    """ testing display function. """
    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)  # remove file if exists
    assert f.service().display() == f.v.fileerror
    fp = open(f.v.servicelist, 'w+b')  # create empty file
    fp.close()  # close 'cuz we don't really need it
    assert f.service().display() == f.v.displayerror
    # commented out display test since I don't want to see it every time, uncomment to test
    f.service().addone(name="massage", code=12345678, address="101 n whatever street", city="portland", state="OR", fee=400.00)
    f.service().addone(name="jeff", code=9876543, address="new address", city="greshem", state="WA", fee=543)
    assert f.service().display() is True

    # clean up after test
    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)


def deleteallservicetest():
    """ test delete all service function. """
    f.service().addone(name="massage", code=12345678, fee=400.00)
    f.service().addone(name="jeff", code=9876543, fee=543)
    assert f.service().deleteall() is True
    assert f.service().display() is f.v.displayerror

    # clean up after test
    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)


def deleteoneservicetest():
    """ test delete one service function. """
    f.service().addone(name="massage", code=12345678, fee=400.00)
    f.service().addone(name="jeff", code=9876543, fee=543)
    f.service().addone(name="jeff", code=6496743, fee=543)

    assert f.service().deleteone(9876543) is True
    assert f.service().deleteone("1029384") is f.v.nonefound
    assert f.service().deleteone(None) is f.v.missingdata

    fp = open(f.v.servicelist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "massage"
    assert mylist[0]["code"] == 12345678
    assert mylist[0]["fee"] == "400"

    assert mylist[1]["name"] == "jeff"
    assert mylist[1]["code"] == 6496743
    assert mylist[1]["fee"] == "543"

    # clean up after test
    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)


def modifyoneservicetest():
    """ Test modify service function. """
    f.service().addone(name="massage", code=12345678, fee=400.00)
    f.service().addone(name="jeff", code=6496743, fee=543)
    f.service().addone(name="mark", code=12345610, fee=400.00)

    assert f.service().modifyone(code=12345678, fee=120) is True
    assert f.service().modifyone(code=6496743, name="foobar") is True
    assert f.service().modifyone(code=12345610, name="mark0", fee=200) is True

    assert f.service().modifyone(code=1234569, name="mark") is f.v.nonefound
    assert f.service().modifyone(code=None, name="sarah") is f.v.missingdata

    fp = open(f.v.servicelist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["name"] == "massage"
    assert mylist[0]["code"] == 12345678
    assert mylist[0]["fee"] == "120"

    assert mylist[1]["name"] == "foobar"
    assert mylist[1]["code"] == 6496743
    assert mylist[1]["fee"] == "543"

    assert mylist[2]["name"] == "mark0"
    assert mylist[2]["code"] == 12345610
    assert mylist[2]["fee"] == "200"

    # clean up after test
    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)


# tests of weeklyservices() class -------------------------------------------------------


def addoneweeklyservicestest():
    """ testing service functions. """
    # clear memberlist file
    if path.exists(f.v.weekservicelist):
        remove(f.v.weekservicelist)

    # clear other working files
    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)

    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)

    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)

    # initiate some values for the other 3 files we need to check from
    assert f.member().addone(name="brian", number=12345, address="new addr0", city="portland", state="OR", zipcode=97227) is True
    assert f.member().addone(name="jeoff", number=54321, address="new addr1", city="greshem", state="WA", zipcode=72279) is True

    assert f.provider().addone(name="dr.1", number=56789, address="new addr2", city="ptown", state="OR", zipcode=5647) is True
    assert f.provider().addone(name="dr.2", number=98765, address="new addr3", city="gtown", state="WA", zipcode=7465) is True

    assert f.service().addone(name="massage", code=890123, fee=50) is True
    assert f.service().addone(name="therapy", code=321098, fee=75) is True

    # test to see if adding from empty list works
    assert f.weeklyservices().addone(dmonth=10, dday=25, dyear=2014, pnumber=56789, mnumber=12345, code=321098, comments="this is not a comment") is True

    fp = open(f.v.weekservicelist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[0]["dateofservice"] == "10-25-2014"
    assert mylist[0]["pnumber"] == 56789
    assert mylist[0]["mnumber"] == 12345
    assert mylist[0]["code"] == 321098
    assert mylist[0]["comments"] == "this is not a comment"

    # test to see if addine a second one works
    assert f.weeklyservices().addone(dmonth=10, dday=26, dyear=2013, pnumber=98765, mnumber=54321, code=890123, comments="no comment") is True

    fp = open(f.v.weekservicelist, 'rb')
    try:
        mylist = load(fp)
    except ValueError:
        print "load failed"

    assert mylist[1]["dateofservice"] == "10-26-2013"
    assert mylist[1]["pnumber"] == 98765
    assert mylist[1]["mnumber"] == 54321
    assert mylist[1]["code"] == 890123
    assert mylist[1]["comments"] == "no comment"

    # these assertions should fail
    assert f.weeklyservices().addone(dmonth="10", dday=26, dyear=2013, pnumber=98765, mnumber=54321, code=890123, comments="no comment") is f.v.typeerror

    assert f.weeklyservices().addone(dmonth=14, dday=26, dyear=2014, pnumber=98765, mnumber=54321, code=890123, comments="no comment") is f.v.toolongdata
    assert f.weeklyservices().addone(dmonth=10, dday=32, dyear=2014, pnumber=98765, mnumber=54321, code=890123, comments="no comment") is f.v.toolongdata
    assert f.weeklyservices().addone(dmonth=10, dday=26, dyear=2015, pnumber=98765, mnumber=54321, code=890123, comments="no comment") is f.v.toolongdata
    assert f.weeklyservices().addone(dmonth=0, dday=26, dyear=2014, pnumber=98765, mnumber=54321, code=890123, comments="no comment") is f.v.toolongdata
    assert f.weeklyservices().addone(dmonth=10, dday=6, dyear=2014, pnumber=98765, mnumber=54321, code=890123, comments="no comment") is f.v.toolongdata
    assert f.weeklyservices().addone(dmonth=10, dday=26, dyear=201, pnumber=98765, mnumber=54321, code=890123, comments="no comment") is f.v.toolongdata

    assert f.weeklyservices().addone(dmonth=10, dday=26, dyear=2013, pnumber=00000, mnumber=54321, code=890123, comments="no comment") is f.v.pmcnotfound
    assert f.weeklyservices().addone(dmonth=10, dday=26, dyear=2013, pnumber=98765, mnumber=11111, code=890123, comments="no comment") is f.v.pmcnotfound
    assert f.weeklyservices().addone(dmonth=10, dday=26, dyear=2013, pnumber=98765, mnumber=54321, code=555555, comments="no comment") is f.v.pmcnotfound

    # clean up after test
    if path.exists(f.v.weekservicelist):
        remove(f.v.weekservicelist)

    # clean up other working files
    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)

    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)

    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)


def displayweeklyservicestest():
    """ testing display function. """
    if path.exists(f.v.weekservicelist):
        remove(f.v.weekservicelist)  # remove file if exists
    assert f.weeklyservices().display() == f.v.fileerror
    fp = open(f.v.weekservicelist, 'w+b')  # create empty file
    fp.close()  # close 'cuz we don't really need it
    assert f.weeklyservices().display() == f.v.displayerror
    # commented out display test since I don't want to see it every time, uncomment to test
    f.service().addone(name="massage", code=12345678, address="101 n whatever street", city="portland", state="OR", fee=400.00)
    f.service().addone(name="jeff", code=9876543, address="new address", city="greshem", state="WA", fee=543)
    assert f.service().display() is True

    # clean up after test
    if path.exists(f.v.weekservicelist):
        remove(f.v.weekservicelist)


def deleteallweeklyservicestest():
    """ test delete all weeklyservices function. """
    # initiate files

    # cleear initial working files
    if path.exists(f.v.weekservicelist):
        remove(f.v.weekservicelist)

    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)

    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)

    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)

    # initiate some values for the other 3 files we need to reference
    assert f.member().addone(name="brian", number=12345, address="new addr0", city="portland", state="OR", zipcode=97227) is True
    assert f.member().addone(name="jeoff", number=54321, address="new addr1", city="greshem", state="WA", zipcode=72279) is True

    assert f.provider().addone(name="dr.1", number=56789, address="new addr2", city="ptown", state="OR", zipcode=5647) is True
    assert f.provider().addone(name="dr.2", number=98765, address="new addr3", city="gtown", state="WA", zipcode=7465) is True

    assert f.service().addone(name="massage", code=890123, fee=50) is True
    assert f.service().addone(name="therapy", code=321098, fee=75) is True

    # add some data
    assert f.weeklyservices().addone(dmonth=10, dday=25, dyear=2014, pnumber=56789, mnumber=12345, code=321098, comments="this is not a comment") is True
    assert f.weeklyservices().addone(dmonth=10, dday=26, dyear=2013, pnumber=98765, mnumber=54321, code=890123, comments="no comment") is True

    # test deleting is True
    assert f.weeklyservices().deleteall() is True
    # test display error on no file
    assert f.weeklyservices().display() is f.v.displayerror

    # clean up after test
    if path.exists(f.v.weekservicelist):
        remove(f.v.weekservicelist)

    if path.exists(f.v.servicelist):
        remove(f.v.servicelist)

    if path.exists(f.v.providerlist):
        remove(f.v.providerlist)

    if path.exists(f.v.memberlist):
        remove(f.v.memberlist)

# run main----------------------------------------------------


def main():
    """ main testing function. """
    addonemembertest()
    displaymembertest()
    deleteallmembertest()
    deleteonemembertest()
    modifyonemembertest()

    addoneprovidertest()
    displayprovidertest()
    deleteallprovidertest()
    deleteoneprovidertest()
    modifyoneprovidertest()

    addoneservicetest()
    displayservicetest()
    deleteallservicetest()
    deleteoneservicetest()
    modifyoneservicetest()

    addoneweeklyservicestest()
    displayweeklyservicestest()
    deleteallweeklyservicestest()


# done with main

main()
