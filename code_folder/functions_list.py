#! /usr/bin/env python

from json import load, dump
from os import remove, path


class v(object):

    """standard variables used in this program."""

    memberlist = "memberlist.json"


class customers(object):

    """a list of customers."""

    def addcustomer(self):
        """my docstring."""
        return "hello world"


class member(object):

    """a member of the choc-an system."""

    def addmember(self, name=None, number=None, address=None, city=None, state=None, zip=None):
        """add a member to the members file, creates the file if it does not exist."""
        listitem = {"name": name,
                    "number": number,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zip": zip}

        if not path.exists(v.memberlist):
            fp = open(v.memberlist, 'w+b')
            fp.close()
        fp = open(v.memberlist, 'rb')

        try:
            memberlist = load(fp)
        except ValueError:
            memberlist = list()
        except:
            print "unhandled exception occured"

        fp.close()
        fp = open(v.memberlist, 'w+b')
        memberlist.append(listitem)
        dump(memberlist, fp)
        fp.close()
