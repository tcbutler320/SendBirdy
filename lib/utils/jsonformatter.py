import json
import datetime

from pyjavaproperties import Properties

import lib.utils.constants as c


def format(file):

    p = Properties()
    p.load(open('res/proj.properties'))

    dt = datetime.datetime.now().strftime("%Y%m%d%H%M")

    try:
        for line in open(file, 'r'):
            parsed = json.loads(line)
            formatted_outfile = str(p.getProperty('FORMATTEDOUTFILE')) + "sendbirdy-" + dt + ".json"
            try:
                f = open(formatted_outfile, "a")
                f.write(json.dumps(parsed, indent=4, sort_keys=True))
                f.close()
            except IOError as io:
                print("{!}----- I/O error({0}): {1}"+ format(io.errno))
    except Exception as e:
        print(c.indent_msg + c.indent_err + e)

    print(c.indent_msg + c.indent_info + " Output Located : [" + formatted_outfile)


    return



