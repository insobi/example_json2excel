import sys, getopt, json
import pandas as pd
   
def main(argv):
    in_filename = ""
    out_filename = ""

    opts, args = getopt.getopt(argv, "i:o:")

    for opt, arg in opts:
        if opt in ('-i', '--input'):
            in_filename = arg
        if opt in ('-o', '--out'):
            out_filename = arg            

    with open(in_filename) as readed:
        loaded = json.load(readed)
    
    pd.DataFrame(loaded).to_excel(out_filename)

if __name__ == "__main__":
    main(sys.argv[1:])