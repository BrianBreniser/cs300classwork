"""the business logic for Choc-An system."""

from json import load, dump
from os import path, remove
import decimal as decimal
import datetime as dt
# from pprint import pprint


class v(object):

    """standard (v)ariables and error messages and used in this program."""

    # data files
    memberlist = "memberlist.json"
    providerlist = "providerlist.json"
    servicelist = "servicelist.json"
    weekservicelist = "weekservicelist.json"

    # report files
    memberreportlist = "memberreportlist.json"
    providerreportlist = "memberreportlist.json"
    summaryreportlist = "summaryreportlist.json"

    # error codes
    fileerror = "There was an unknown file error"
    displayerror = "display error: no file found"
    alreadyfound = "that object is already found"
    missingdata = "You entered missing data"
    toolongdata = "Some of your data is too long"
    nonefound = "none was found"
    typeerror = "you entered the wrong type of data"
    pmcnotfound = "provider, member, or code numbers not found"


class h(object):

    """ some (h)elper functions we can use mostly universally."""

    def checkfileandreturnlist(self, filename=None):
        """find and/or create the file being used."""
        if filename is None:
            return False

        # Check to see if file exists, if not, create it and close it
        if not path.exists(filename):
            fp = open(filename, 'w+b')
            fp.close()

        # Open file (which will exist because the last secion made it exists no matter what)
        fp = open(filename, 'rb')

        # try to load the file from JSON format, if it fails, initiate an empty list
        try:
            data = load(fp)
        except ValueError:
            data = list()
        except:
            data = list()
            print "unhandled exception occured"

        # Done with reading the file
        fp.close()

        # return either the populated list, or an empty list
        return data

    def writedatatofile(self, filename=None, data=None):
        """Will write 'data' to 'filename', in json format."""
        # fail if parameters are not entered
        if filename is None or data is None:
            return False

        # open file (while destroying current data) for writing, write the new data
        fp = open(filename, 'w+b')
        dump(data, fp)
        fp.close()
        return True  # return a success if we get to this point


class member(object):

    """a member of the choc-an system."""

    def addone(self, name=None, number=None, address=None, city=None, state=None, zipcode=None):
        """add a member to the members file, creates the file if it does not exist."""
        # Check for non-entered data
        if name is None or number is None or address is None or city is None or state is None or zipcode is None:
            return v.missingdata

        # Check for correct data types
        if type(name) is not str:
            return v.typeerror
        if type(number) is not int:
            return v.typeerror
        if type(address) is not str:
            return v.typeerror
        if type(city) is not str:
            return v.typeerror
        if type(state) is not str:
            return v.typeerror
        if type(zipcode) is not int:
            return v.typeerror

        # Check for length attributes
        if len(name) > 25 or len(str(number)) > 9 or len(address) > 25 or len(city) > 14 or len(state) > 2 or len(str(zipcode)) > 5:
            return v.toolongdata

        # Prep our list item to be added to file
        listitem = {"name": name,
                    "number": number,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode}

        fulllist = h().checkfileandreturnlist(filename=v.memberlist)
        if fulllist is False:
            return False

        # Got to check to see if we already have this member (number) in our system
        for m in fulllist:
            if m["number"] == number:
                return v.alreadyfound

        # If it all checks out, we can add our new listitem
        fulllist.append(listitem)

        return h().writedatatofile(filename=v.memberlist, data=fulllist)

    def display(self):
        """display all members of the choc-an members list."""
        if not path.exists(v.memberlist):
            return v.fileerror
        else:
            fp = open(v.memberlist, 'rb')

            try:
                displaylist = load(fp)
            except ValueError:
                return v.displayerror
            else:
                print ""
                for m in displaylist:
                    print str(m["name"])
                    print "    " + str(m["number"])
                    print "    " + str(m["address"])
                    print "    " + str(m["city"])
                    print "    " + str(m["state"])
                    print "    " + str(m["zipcode"])
                    print ""
        return True

    def deleteall(self):
        """ Delete the file and start with an empty one. """
        if path.exists(v.memberlist):
            remove(v.memberlist)

        fp = open(v.memberlist, 'w+b')
        fp.close()
        return True

    def deleteone(self, number=None):
        """Delete only a single member by member number."""
        # If no data was passed in, don't do anything
        if number is None:
            return v.missingdata

        fulllist = h().checkfileandreturnlist(filename=v.memberlist)
        if fulllist is False:
            return False

        # Check to see if member number is in the list
        for m in fulllist:
            if m["number"] == number:
                # we found it! Remove it from the list!
                fulllist.remove(m)

                # return true if writing was good, false if writing failed
                return h().writedatatofile(filename=v.memberlist, data=fulllist)

        # If we made it here, we didn't find the item
        return v.nonefound

    def modifyone(self, name=None, number=None, address=None, city=None, state=None, zipcode=None):
        """modify a member by searching for member number and overwriting other fields entered."""
        # If we didn't give a member number, we don't know what to change
        if number is None:
            return v.missingdata

        fulllist = h().checkfileandreturnlist(filename=v.memberlist)
        if fulllist is False:
            return False

        # Check to see if member number is in the list
        for m in fulllist:
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

                # return true if writing was good, false if writing failed
                return h().writedatatofile(filename=v.memberlist, data=fulllist)

        # If we made it here, we didn't find the item
        return v.nonefound


class provider(object):

    """a provider of the choc-an system."""

    def addone(self, name=None, number=None, address=None, city=None, state=None, zipcode=None):
        """add a provider to the providers file, creates the file if it does not exist."""
        # Check for non-entered data
        if name is None or number is None or address is None or city is None or state is None or zipcode is None:
            return v.missingdata

        # Check for correct data types
        if type(name) is not str:
            return v.typeerror
        if type(number) is not int:
            return v.typeerror
        if type(address) is not str:
            return v.typeerror
        if type(city) is not str:
            return v.typeerror
        if type(state) is not str:
            return v.typeerror
        if type(zipcode) is not int:
            return v.typeerror

        # Check for length attributes
        if len(name) > 25 or len(str(number)) > 9 or len(address) > 25 or len(city) > 14 or len(state) > 2 or len(str(zipcode)) > 5:
            return v.toolongdata

        # Prep our list item to be added to file
        listitem = {"name": name,
                    "number": number,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode}

        fulllist = h().checkfileandreturnlist(filename=v.providerlist)
        if fulllist is False:
            return False

        # Got to check to see if we already have this provider (number) in our system
        for m in fulllist:
            if m["number"] == number:
                return v.alreadyfound

        # If it all checks out, we can add our new listitem
        fulllist.append(listitem)

        return h().writedatatofile(filename=v.providerlist, data=fulllist)

    def display(self):
        """display all providers of the choc-an providers list."""
        if not path.exists(v.providerlist):
            return v.fileerror
        else:
            fp = open(v.providerlist, 'rb')

            try:
                displaylist = load(fp)
            except ValueError:
                return v.displayerror
            else:
                print ""
                for m in displaylist:
                    print str(m["name"])
                    print "    " + str(m["number"])
                    print "    " + str(m["address"])
                    print "    " + str(m["city"])
                    print "    " + str(m["state"])
                    print "    " + str(m["zipcode"])
                    print ""
        return True

    def deleteall(self):
        """ Delete the file and start with an empty one. """
        if path.exists(v.providerlist):
            remove(v.providerlist)

        fp = open(v.providerlist, 'w+b')
        fp.close()
        return True

    def deleteone(self, number=None):
        """Delete only a single provider by provider number."""
        # If no data was passed in, don't do anything
        if number is None:
            return v.missingdata

        fulllist = h().checkfileandreturnlist(filename=v.providerlist)
        if fulllist is False:
            return False

        # Check to see if provider number is in the list
        for m in fulllist:
            if m["number"] == number:
                # we found it! Remove it from the list!
                fulllist.remove(m)

                # return true if writing was good, false if writing failed
                return h().writedatatofile(filename=v.providerlist, data=fulllist)

        # If we made it here, we didn't find the item
        return v.nonefound

    def modifyone(self, name=None, number=None, address=None, city=None, state=None, zipcode=None):
        """modify a provider by searching for provider number and overwriting other fields entered."""
        # If we didn't give a provider number, we don't know what to change
        if number is None:
            return v.missingdata

        fulllist = h().checkfileandreturnlist(filename=v.providerlist)
        if fulllist is False:
            return False

        # Check to see if provider number is in the list
        for m in fulllist:
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

                # return true if writing was good, false if writing failed
                return h().writedatatofile(filename=v.providerlist, data=fulllist)

        # If we made it here, we didn't find the item
        return v.nonefound


class service(object):

    """a service of the choc-an system."""

    def addone(self, name=None, code=None, fee=None):
        """add a service to the services file, creates the file if it does not exist."""
        # Check for non-entered data
        if name is None or code is None or fee is None:
            return v.missingdata

        # Ensure our fee is a decimal, and not str or int
        fee = decimal.Decimal(fee)

        # Check for correct data types
        if type(name) is not str:
            return v.typeerror
        if type(code) is not int:
            return v.typeerror
        if type(fee) is not decimal.Decimal:
            return v.typeerror

        # Check for length attributes
        if len(name) > 25 or len(str(code)) > 9 or (0 > decimal.Decimal(fee) or decimal.Decimal(fee) > 999.99):
            return v.toolongdata

        # Prep our list item to be added to file
        listitem = {"name": name,
                    "code": code,
                    "fee": str(fee)}

        fulllist = h().checkfileandreturnlist(filename=v.servicelist)
        if fulllist is False:
            return False

        # Got to check to see if we already have this service (number) in our system
        for m in fulllist:
            if m["code"] == code:
                return v.alreadyfound

        # If it all checks out, we can add our new listitem
        fulllist.append(listitem)

        return h().writedatatofile(filename=v.servicelist, data=fulllist)

    def display(self):
        """display all services of the choc-an services list."""
        if not path.exists(v.servicelist):
            return v.fileerror
        else:
            fp = open(v.servicelist, 'rb')

            try:
                displaylist = load(fp)
            except ValueError:
                return v.displayerror
            else:
                print ""
                for m in displaylist:
                    print str(m["name"])
                    print "    " + str(m["code"])
                    print "    $" + str(m["fee"])
                    print ""
        return True

    def deleteall(self):
        """ Delete the file and start with an empty one. """
        if path.exists(v.servicelist):
            remove(v.servicelist)

        fp = open(v.servicelist, 'w+b')
        fp.close()
        return True

    def deleteone(self, code=None):
        """Delete only a single service by service number."""
        # If no data was passed in, don't do anything
        if code is None:
            return v.missingdata

        fulllist = h().checkfileandreturnlist(filename=v.servicelist)
        if fulllist is False:
            return False

        # Check to see if service number is in the list
        for m in fulllist:
            if m["code"] == code:
                # we found it! Remove it from the list!
                fulllist.remove(m)

                # return true if writing was good, false if writing failed
                return h().writedatatofile(filename=v.servicelist, data=fulllist)

        # If we made it here, we didn't find the item
        return v.nonefound

    def modifyone(self, name=None, code=None, fee=None):
        """modify a service by searching for service number and overwriting other fields entered."""
        # If we didn't give a service number, we don't know what to change
        if code is None:
            return v.missingdata

        # make fee forced to Decimal if it exists
        if fee is not None:
            fee = decimal.Decimal(fee)

        fulllist = h().checkfileandreturnlist(filename=v.servicelist)
        if fulllist is False:
            return False

        # Check to see if service number is in the list
        for m in fulllist:
            if m["code"] == code:
                # we found it! Start changin data
                # For each item, if we passed in data, update the list
                if name is not None and type(name) is str and len(name) <= 25:
                    m["name"] = name
                if fee is not None and type(fee) is decimal.Decimal and 0 <= decimal.Decimal(fee) and decimal.Decimal(fee) <= 999.99:
                    m["fee"] = str(fee)

                # return true if writing was good, false if writing failed
                return h().writedatatofile(filename=v.servicelist, data=fulllist)

        # If we made it here, we didn't find the item
        return v.nonefound


class weeklyservices(object):

    """a service of the choc-an system."""

    def addone(self, dmonth=None, dday=None, dyear=None, pnumber=None, mnumber=None, code=None, comments=None):
        """add a service to the services file, creates the file if it does not exist."""
        # Check for non-entered data
        if dmonth is None or dday is None or dyear is None or pnumber is None or mnumber is None or code is None or comments is None:
            return v.missingdata

        # Check for correct data types
        if type(dmonth) is not int:
            return v.typeerror
        if type(dday) is not int:
            return v.typeerror
        if type(dyear) is not int:
            return v.typeerror
        if type(pnumber) is not int:
            return v.typeerror
        if type(mnumber) is not int:
            return v.typeerror
        if type(code) is not int:
            return v.typeerror
        if type(comments) is not str:
            return v.typeerror

        # Check for length and size attributes
        if (dmonth > 12 or
                len(str(dmonth)) < 2 or
                dday > 31 or
                len(str(dday)) < 2 or
                dyear > int(str(dt.datetime.now())[0:10].split('-')[0]) or  # if the year enteres is later (future) than the current year
                len(str(dyear)) < 4 or
                len(str(pnumber)) > 9 or
                len(str(mnumber)) > 9 or
                len(str(code)) > 6 or
                len(str(comments)) > 100):
            return v.toolongdata

        # Open the other databases since we have to check if our data exists in there
        providerlist = h().checkfileandreturnlist(filename=v.providerlist)
        if providerlist is False:
            return False
        memberlist = h().checkfileandreturnlist(filename=v.memberlist)
        if memberlist is False:
            return False
        servicelist = h().checkfileandreturnlist(filename=v.servicelist)
        if servicelist is False:
            return False

        # Check for existance of provider, member, and services in respective lists
        pexists, mexists, cexists = 0, 0, 0  # initiate some "exists" variables to 0, change to 1 if we find them
        for i in providerlist:
            if pnumber == i["number"]:
                pexists = 1

        for i in memberlist:
            if mnumber == i["number"]:
                mexists = 1

        for i in servicelist:
            if code == i["code"]:
                cexists = 1

        # return error if we didn't find 1 or more distinguishing numbers in our files
        if pexists == 0 or mexists == 0 or cexists == 0:
            return v.pmcnotfound

        # set todays date with correct syntax
        dateofservice = "{0}-{1}-{2}".format(dmonth, dday, dyear)

        # set date of service with correct syntax
        # split up date of now
        datelist = str(dt.datetime.now()).split()[0].split('-')
        # assign date to vars
        cyear, cmonth, cday = datelist[0], datelist[1], datelist[2]
        # split up the time var by colon ":"
        timelist = str(dt.datetime.now()).split()[1].split(':')
        # Assign time vars
        chour, cmin, csec = timelist[0], timelist[1], timelist[2][0:2]
        # put in format I want
        currentdate = "{0}-{1}-{2} {3}:{4}:{5}".format(cmonth, cday, cyear, chour, cmin, csec)

        # Prep our list item to be added to file
        listitem = {"currentdate": currentdate,
                    "dateofservice": dateofservice,
                    "pnumber": pnumber,
                    "mnumber": mnumber,
                    "code": code,
                    "comments": comments}

        fulllist = h().checkfileandreturnlist(filename=v.weekservicelist)
        if fulllist is False:
            return False

        # Nothing else to check, append to list
        fulllist.append(listitem)

        # write to file
        return h().writedatatofile(filename=v.weekservicelist, data=fulllist)

    def display(self):
        """display all services of the choc-an services list."""
        if not path.exists(v.weekservicelist):
            return v.fileerror
        else:
            fp = open(v.weekservicelist, 'rb')

            try:
                displaylist = load(fp)
            except ValueError:
                return v.displayerror
            else:
                print ""
                for m in displaylist:
                    print str(m["currentdate"])
                    print str(m["dateofservice"])
                    print str(m["pnumber"])
                    print str(m["mnumber"])
                    print str(m["code"])
                    print str(m["comments"])
                    print ""
        return True

    def deleteall(self):
        """ Delete the file and start with an empty one. """
        if path.exists(v.weekservicelist):
            remove(v.weekservicelist)

        fp = open(v.weekservicelist, 'w+b')
        fp.close()
        return True

    # def deleteone(self, code=None):
    #     """Delete only a single service by service number."""
    # If no data was passed in, don't do anything
    #     if code is None:
    #         return v.missingdata

    #     fulllist = h().checkfileandreturnlist(filename=v.weekservicelist)
    #     if fulllist is False:
    #         return False

    # Check to see if service number is in the list
    #     for m in fulllist:
    #         if m["code"] == code:
    # we found it! Remove it from the list!
    #             fulllist.remove(m)

    # return true if writing was good, false if writing failed
    #             return h().writedatatofile(filename=v.weekservicelist, data=fulllist)

    # If we made it here, we didn't find the item
    #     return v.nonefound

    # def modifyone(self, name=None, code=None, fee=None):
    #     """modify a service by searching for service number and overwriting other fields entered."""
    # If we didn't give a service number, we don't know what to change
    #     if code is None:
    #         return v.missingdata

    # make fee forced to Decimal if it exists
    #     if fee is not None:
    #         fee = decimal.Decimal(fee)

    #     fulllist = h().checkfileandreturnlist(filename=v.weekservicelist)
    #     if fulllist is False:
    #         return False

    # Check to see if service number is in the list
    #     for m in fulllist:
    #         if m["code"] == code:
    # we found it! Start changin data
    # For each item, if we passed in data, update the list
    #             if name is not None and type(name) is str and len(name) <= 25:
    #                 m["name"] = name
    #             if fee is not None and type(fee) is decimal.Decimal and 0 <= decimal.Decimal(fee) and decimal.Decimal(fee) <= 999.99:
    #                 m["fee"] = str(fee)

    # return true if writing was good, false if writing failed
    #             return h().writedatatofile(filename=v.weekservicelist, data=fulllist)

    # If we made it here, we didn't find the item
    #     return v.nonefound


class report(object):

    """report functions for member, provider, and summary."""

    def memberreport(self):
        """member report function, creates external json file with report."""
        # Start clean, with an empty file before running each report
        if path.exists(v.memberreportlist):
            remove(v.memberreportlist)

        # load up the files we will use
        providerlist = h().checkfileandreturnlist(filename=v.providerlist)
        if providerlist is False:
            return False

        memberlist = h().checkfileandreturnlist(filename=v.memberlist)
        if memberlist is False:
            return False

        servicelist = h().checkfileandreturnlist(filename=v.servicelist)
        if servicelist is False:
            return False

        weekservicelist = h().checkfileandreturnlist(filename=v.weekservicelist)
        if weekservicelist is False:
            return False

        # create a copy of our memberlist to make modifications
        modifiedmemberlist = memberlist

        # enter a loop to build the services each member got, and add that to our new services list
        for m in modifiedmemberlist:  # loop through our member list
            m["service list"] = []  # always add an initiated empty list to each member
            for w in weekservicelist:  # loop through weekly services list
                if w["mnumber"] == m["number"]:  # if we find one for our member number, that means they got a service this cycle
                    newservice = {}  # create a new service dict to fill info into
                    newservice["date of service"] = w["dateofservice"]  # and fill it with date of service
                    for p in providerlist:  # then find associated provider in providers list (from weekly service)
                        if w["pnumber"] == p["number"]:  # if found
                            newservice["provider name"] = p["name"]  # add their name
                            break  # we can stop looking now
                    for s in servicelist:  # we need the services name now too
                        if w["code"] == s["code"]:  # so find the code
                            newservice["service name"] = s["name"]  # add its name
                            break  # we can stop looking now
                    m["service list"].append(newservice)  # we need to add this service to a running list of services for each member
                    continue  # keep looking, find ALL services for each member
        # ^^ holy shit I think we're done

        # Check to see if we have any members without services for the week
        for m in modifiedmemberlist:
            if m["service list"] == []:
                # we found it! Remove it from the list!
                modifiedmemberlist.remove(m)

        # pprint for minor debug issue
        # pprint(modifiedmemberlist)

        # gotta write it to the file
        return h().writedatatofile(filename=v.memberreportlist, data=modifiedmemberlist)

    def providerreport(self):
        """providerreport function, creates external json file with report."""
        # Start clean, with an empty file before running each report
        if path.exists(v.providerreportlist):
            remove(v.providerreportlist)

        # load up the files we will use
        providerlist = h().checkfileandreturnlist(filename=v.providerlist)
        if providerlist is False:
            return False

        memberlist = h().checkfileandreturnlist(filename=v.memberlist)
        if memberlist is False:
            return False

        servicelist = h().checkfileandreturnlist(filename=v.servicelist)
        if servicelist is False:
            return False

        weekservicelist = h().checkfileandreturnlist(filename=v.weekservicelist)
        if weekservicelist is False:
            return False

        # create a copy of our provider list to make modifications
        modifiedproviderlist = providerlist

        # enter a loop to build the services each member got, and add that to our new services list
        for p in modifiedproviderlist:  # loop through our member list
            p["service list"] = []  # always add an initiated empty list to each member
            p["total number of consultations"] = int(0)
            p["total fee for week"] = decimal.Decimal(0)
            for w in weekservicelist:  # loop through weekly services list
                if w["pnumber"] == p["number"]:  # if we find one for our provider number, that means they provided a service this cycle
                    p["total number of consultations"] += 1
                    newservice = {}  # create a new service dict to fill info into
                    newservice["date of service"] = w["dateofservice"]  # and fill it with date of service
                    newservice["date and time of data recieved"] = w["currentdate"]  # also fill with date service entry was entered
                    for m in memberlist:  # then find associated member in members list (from weekly service)
                        if w["mnumber"] == m["number"]:  # if found
                            newservice["member name"] = m["name"]  # add their name
                            newservice["member number"] = m["number"]  # and their number
                            break  # we can stop looking now
                    for s in servicelist:  # we need the services name now too
                        if w["code"] == s["code"]:  # so find the code
                            newservice["service name"] = s["name"]  # add its name
                            newservice["service fee"] = s["fee"]  # and the fee associated
                            p["total fee for week"] = decimal.Decimal(p["total fee for week"]) + decimal.Decimal(s["fee"])
                            break  # we can stop looking now
                    p["total fee for week"] = str(p["total fee for week"])  # convert decimal to string since JSON doesnt like decimals
                    p["service list"].append(newservice)  # we need to add this service to a running list of services for each provider
                    continue  # keep looking, find ALL services for each provider
        # ^^ holy shit I think we're done

        # Check to see if we have any members without services for the week
        for p in modifiedproviderlist:
            if p["service list"] == []:
                # we found it! Remove it from the list!
                modifiedproviderlist.remove(p)

        # gotta write it to the file
        return h().writedatatofile(filename=v.memberreportlist, data=modifiedproviderlist)

    def summaryreport(self):
        """summary  report function, creates external json file with report."""
        # Start clean, with an empty file before running each report
        if path.exists(v.summaryreportlist):
            remove(v.summaryreportlist)

        # run the other reports first
        report().memberreport()
        report().providerreport()

        # load up the report files
        providerreportlist = h().checkfileandreturnlist(filename=v.providerreportlist)
        if providerreportlist is False:
            return False

        # initate a new empty list we will eventually write to summary report JSON file
        summaryreportlist = []

        # initiate a dict with initial summary data
        summaryreportlist.append({})
        summaryreportlist[0]["total number of providers who provided services"] = 0
        summaryreportlist[0]["total number of consultations"] = 0
        summaryreportlist[0]["total overall week fee"] = decimal.Decimal(0)

        # loop through the providerreportlist
        for p in providerreportlist:
            # add a subset of the provider report to our final report
            additem = {}
            additem["provider name"] = p["name"]
            additem["number of consulations"] = p["total number of consultations"]
            additem["total fee for week for this provider"] = p["total fee for week"]
            summaryreportlist.append(additem)

            # increment some counters of the first list items overall summary dictionary
            summaryreportlist[0]["total number of providers who provided services"] += 1
            summaryreportlist[0]["total number of consultations"] += int(p["total number of consultations"])
            summaryreportlist[0]["total overall week fee"] = decimal.Decimal(summaryreportlist[0]["total overall week fee"]) + decimal.Decimal(p["total fee for week"])

        # welp, JSON no like decimal, so gotta do this too
        summaryreportlist[0]["total overall week fee"] = str(summaryreportlist[0]["total overall week fee"])

        # gotta write it to the file
        return h().writedatatofile(filename=v.summaryreportlist, data=summaryreportlist)
