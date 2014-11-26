"""the business logic for Choc-An system."""

from json import load, dump
from os import path


class v(object):

    """standard variables used in this program."""

    memberlist = "memberlist.json"


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

    def display(self):
        """display all members of the choc-an members list."""
        if not path.exists(v.memberlist):
            print "There is no member file! Try adding members first!"
        else:
            fp = open(v.memberslist, 'rb')

            try:
                displaylist = load(fp)
            except ValueError:
                print "There are no members to display currently, Try adding members first!"
            else:
                for m in displaylist:
                    print m["name"]
                    print m["number"]
                    print m["address"]
                    print m["city"]
                    print m["state"]
                    print m["zip"]
