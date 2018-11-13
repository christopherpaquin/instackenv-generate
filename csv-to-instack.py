import csv
import json
import sys
import getopt
from collections import defaultdict

def main(argv):
    inputfile = None

    try:
        opts, args = getopt.getopt(argv,"c",["csv="])
    except :
        print >> sys.stderr, "csv-to-instack.py --csv=<inputfile>"
        sys.exit(2)

    for opt, arg in opts:
       if opt == '-h':
           print >> sys.stderr ,'csv-to-instack.py --csv=<inputfile>'
           sys.exit()
       elif opt in ("-c", "--csv"):
           inputfile = arg
    if inputfile == None : 
        print >> sys.stderr, "Error : No input file passed"
        print >> sys.stderr, "Usage:"
        print >> sys.stderr, "csv-to-instack.py --csv=<inputfile>"
        sys.exit(2)

    print >> sys.stderr, "Opening %s" % inputfile
    csvFile =  open(inputfile)
    data = list(csv.reader(csvFile))
    
    firstrow = True 
    jdata = defaultdict(list) 
    for value in data:
        if firstrow :
            firstrow = False
            continue
        jdata['nodes'].append({'pm_password' : value[3], 
        'pm_type' : value[5], 
        'mac' : [value[1]], 
        'name' : value[0],
        'cpu' : "4", 
        'memory' : "6144", 
        'disk' : "40", 
        'arch' : "x86_64", 
        'pm_user' : value[3], 
        'pm_addr' : value[4],
        'pm_port' : value[6]})

    print json.dumps(jdata,indent=4, sort_keys=True) 

if __name__ == "__main__":
    main(sys.argv[1:])
