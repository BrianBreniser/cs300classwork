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
    nonefound = "nonefound"


class member(object):

    """a member of the choc-an system."""

    def addmember(self, name=None, number=None, address=None, city=None, state=None, zipcode=None):
        """add a member to the members file, creates the file if it does not exist."""

        # Check for non-entered data
        if name is None or number is None or address is None or city is None or state is None or zipcode is None:
            return v.missingdata

        # Check for length attributes
        if len(name) > 25 or len(number) > 9 or len(address) > 25 or len(city) > 14 or len(state) > 2 or len(zipcode) > 5:
            return v.toolongdata

        # Prep our list item to be added to file
        listitem = {"name": name,
                    "number": number,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode}

        # Check to see if member file exists, if not, create it and close it
        if not path.exists(v.memberlist):
            fp = open(v.memberlist, 'w+b')
            fp.close()

        # Open file (which will exist because the last secion made it exists no matter what)
        fp = open(v.memberlist, 'rb')

        # try to load the file from JSON format, if it fails, initiate an empty list
        try:
            memberlist = load(fp)
        except ValueError:
            memberlist = list()
        except:
            print "unhandled exception occured"
            return 0

        # Done with reading the file
        fp.close()

        # Got to check to see if we already have this member (number) in our system
        for m in memberlist:
            if m["number"] == number:
                return v.memberalreadyfound

        # If it all checks out, we can add our new listitem
        memberlist.append(listitem)

        # open file (while destroying current data) for writing, write the new data
        fp = open(v.memberlist, 'w+b')
        dump(memberlist, fp)
        fp.close()
        return True  # return a success if we get to this point

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

    def deletemember(self, number=None):
        """Delete only a single member by member number."""
        # If no data was passed in, don't do anything
        if number is None:
            return v.missingdata

        # Check to see if member file exists, if not, create it and close it
        if not path.exists(v.memberlist):
            fp = open(v.memberlist, 'w+b')
            fp.close()

        # Open file (which will exist because the last secion made it exists no matter what)
        fp = open(v.memberlist, 'rb')

        # try to load the file from JSON format, if it fails, initiate an empty list
        try:
            memberlist = load(fp)
        except ValueError:
            memberlist = list()
        except:
            print "unhandled exception occured"
            return 0

        # Done with reading the file
        fp.close()

        # Check to see if member number is in the list
        for m in memberlist:
            if m["number"] == number:
                # we found it! Remove it from the list!
                memberlist.remove(m)

                # open file (while destroying current data) for writing, write the new data
                fp = open(v.memberlist, 'w+b')
                dump(memberlist, fp)
                fp.close()
                return True  # return a success if we get to this point

        # If we made it here, we didn't find the item
        return v.nonefound

    def modifymember(self, name=None, number=None, address=None, city=None, state=None, zipcode=None):
        """modify a member by searching for member number and overwriting other fields entered."""
        # If we didn't give a member number, we don't know what to change
        if number is None:
            return v.missingdata

        # Check to see if member file exists, if not, create it and close it
        if not path.exists(v.memberlist):
            fp = open(v.memberlist, 'w+b')
            fp.close()

        # Open file (which will exist because the last secion made it exists no matter what)
        fp = open(v.memberlist, 'rb')

        # try to load the file from JSON format, if it fails, initiate an empty list
        try:
            memberlist = load(fp)
        except ValueError:
            memberlist = list()
        except:
            print "unhandled exception occured"
            return 0

        # Done with reading the file
        fp.close()

        # Check to see if member number is in the list
        for m in memberlist:
            if m["number"] == number:
                # we found it! Start changin data
                # For each item, if we passed in data, update the list
                if name is not None:
                    m["name"] = name
                if address is not None:
                    m["address"] = address
                if city is not None:
                    m["city"] = city
                if state is not None:
                    m["state"] = state
                if zipcode is not None:
                    m["zipcode"] = zipcode

                # open file (while destroying current data) for writing, write the new data
                fp = open(v.memberlist, 'w+b')
                dump(memberlist, fp)
                fp.close()
                return True  # return a success if we get to this point

        # If we made it here, we didn't find the item
        return v.nonefound
