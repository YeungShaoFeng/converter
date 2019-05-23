from sys import exit, argv
from getopt import getopt, GetoptError
from time import perf_counter
from myway import Tre


def workWithFile(inputfile, outputfile, aimtype):
    with open(inputfile, 'rb') as fi:
        with open(outputfile, 'w') as fo:
            for i in range(10000):
                line = fi.readline().strip()
                if (line):
                    num = Tre(line, aimtype)
                    num.GO()
                    fo.write("%d" %num.treNum)
                    fo.write('\n')
        
def workWithNum(num, aimtype):
    dec = Tre(num, aimtype)
    dec.GO()

def main(argv):
    #start time benchmark
    t1 = perf_counter()
    #get options from the user and deal with them
    aimtype = ''
    num = ''
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt(argv,"hn:i:o:a:",["num=","ifile=","ofile=", "atype="])
    except GetoptError:
        print('treimal.py -n <number> -i <inputfile> -o <outputfile>, -a <aimtype>')
        exit(2)
    for opt, arg in opts:
        if (opt == '-h'):
            print('treimal.py -n <number> -i <inputfile> -o <outputfile>')
            exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--number"):
            num = arg
        elif opt in ("-a", "--aimtype"):
            aimtype = arg
        elif opt not in ("-a", "--aimtype"):
            aimtype = [2, 3, 8]     #[2, 3, 8, 16]
    # start converting
    if (inputfile):
        workWithFile(inputfile, outputfile, aimtype)
    elif (num):
        workWithNum(num, aimtype)
    #endtimebenchmark
    t2 = perf_counter()
    print(f' GO time is: {t2-t1} s. ')

if __name__ == "__main__":
   main(argv[1:])
