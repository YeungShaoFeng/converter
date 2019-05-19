from sys import exit, argv
from getopt import getopt, GetoptError
from time import perf_counter
from test.encryption.myway import Tre


def workWithFile(fi, fo):
    with open(fi, 'r') as f1:
        with open(fo, 'w') as f2:
            for i in range(10000):
                line = f1.readline().strip()
                if (line):
                    num = Tre(line, 10)
                    num.GO()
                    f2.write("%d" %num.treNum)
                    f2.write('\n')
        

def main(argv):
    #start time benchmark
    t1 = perf_counter()

    #get options from the user and deal with them
    num = ''
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt(argv,"hn:i:o:",["num=","ifile=","ofile="])
    except GetoptError:
        print('treimal.py -n <number> -if <inputfile> -of <outputfile>')
        exit(2)
    for opt, arg in opts:
        if (opt == '-h'):
            print('treimal.py -n <number> -if <inputfile> -of <outputfile>')
            exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-n", "--number"):
            num = arg

    #transform decimal to treimal
    if (inputfile):
        workWithFile(inputfile, outputfile)
    elif (num):
        dec = Tre(num, 10)
        dec.GO()

    #endtimebenchmark
    t2 = perf_counter()
    print(f' GO time is: {t2-t1} s. ')


if __name__ == "__main__":
   main(argv[1:])
