#! /usr/bin/env python

import functions_list as f
from os import path, remove
from json import load

# testing tests please move on --------------------------------------------------

x = f.customers()
assert x.addcustomer() == "hello world", "customer != 'hello world'"

# done testing tests ------------------------------------------------------------

# tests of member() class -------------------------------------------------------

# add member test---------------------------------------------

# clear memberlist file
if path.exists(f.v.memberlist):
    remove(f.v.memberlist)

# test to see if adding from empty list works
f.member().addmember(name="joe", number="0123456789", address="101 n whatever street", city="portland", state="OR", zip="912345")
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

f.member().addmember(name="jeff", number="987654321", address="you better get this right", city="greshem", state="why not", zip="74635273849")
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
