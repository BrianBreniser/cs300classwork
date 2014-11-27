"""the business logic for Choc-An system."""

from json import load, dump
from os import path, remove


class v(object):

    """standard variables and error messages used in this program."""

    memberlist = "memberlist.json"
    memberfileerror = "memberfileerror"
    displayerror = "displayerror"
    memberalreadyfound = "memberalreadyfound"
    missingdata = "missingdata"
    toolongdata = "toolongdata"


class member(object):

    """a member of the choc-an system."""

    def addmember(self, name=None, number=None, address=None, city=None, state=None, zipcode=None):
        """add a member to the members file, creates the file if it does not exist."""

        if name is None or number is None or address is None or city is None or state is None or zipcode is None:
            return v.missingdata

        if len(name) > 25 or len(number) > 9 or len(address) > 25 or len(city) > 14 or len(state) > 2 or len(zipcode) > 5:
            return v.toolongdata

        listitem = {"name": name,
                    "number": number,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode}

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
            return 0

        # Got to check t osee if we already have this member (number) in our system
        for m in memberlist:
            if m["number"] == number:
                return v.memberalreadyfound

        fp.close()
        fp = open(v.memberlist, 'w+b')
        memberlist.append(listitem)
        dump(memberlist, fp)
        fp.close()
        return True

    def display(self):
        """display all members of the choc-an members list."""
        if not path.exists(v.memberlist):
            return v.memberfileerror
        else:
            fp = open(v.memberlist, 'rb')

            try:
                displaylist = load(fp)
            except ValueError:
                return v.displayerror
            else:
                print ""
                for m in displaylist:
                    print m["name"]
                    print "    " + m["number"]
                    print "    " + m["address"]
                    print "    " + m["city"]
                    print "    " + m["state"]
                    print "    " + m["zipcode"]
                    print ""
        return True

    def deleteall(self):
        """ Delete the file and start with an empty one. """
        if path.exists(v.memberlist):
            remove(v.memberlist)

        fp = open(v.memberlist, 'w+b')
        fp.close()
        return True
