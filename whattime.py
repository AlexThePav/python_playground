
from dateutil import parser
from dateutil.tz import gettz
from sys import argv
from time import tzname

if __name__ == "__main__":
    tzinfos = {
        "BRST": -7200, 
        "CST": gettz("America/Chicago"),
        "PST": gettz("PST8PDT"),
        "PDT": gettz("PST8PDT")
        }
    if len(argv) > 1:
        p = parser.parse(" ".join(argv[1:]), tzinfos = tzinfos)
        sys_tz = gettz(tzname[0]) or gettz(tzname[1])
        print(tzname)
        print(f"Original timezone: {p}; Local timezone: {p.astimezone(sys_tz)}")
