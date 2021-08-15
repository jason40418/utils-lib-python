MILESTONE_LIST = {
    "develope"            : "dev",
    "pre-alpha"           : "pa",
    "alpha"               : "a",
    "beta"                : "b",
    "preview"             : "p",
    "release-candidate"   : "rc",
    "general-availability": "ga",
    "release"             : ""
}

MILESTONE    = "develope"
MAJOR        = "0"
MINOR        = "1"
REVISION     = "0"
YEAR         = "2021"
MONTH        = "08"
DAY          = "15"
BUILD        = "00"

"""
Version naming rule:
{major}.{minor}.{revision}({milestone}{build})

build naming rule: YYYYMMDDBB
YYYY : Year
MM   : Month
DD   : Day
BB   : Build time
"""
def get_version ():
    semantic  = ".".join([MAJOR, MINOR, REVISION])
    milestone = MILESTONE_LIST[MILESTONE]

    if MILESTONE == 'develope':
        build = "".join([YEAR, MONTH, DAY, BUILD])
    elif MILESTONE == 'release':
        build = ""
    else:
        build = BUILD

    version   = "".join([
        semantic,
        "_" if MILESTONE != "release" else "",
        milestone,
        build,
        "" if MILESTONE == "develope" else ""
    ])
    return version
