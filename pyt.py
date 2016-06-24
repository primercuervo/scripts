import re
import os
import glob

patt_v = re.escape('RFNOC_SRCS = $(abspath $(addprefix $(BASE_DIR)/../lib/rfnoc/, \\\n')

def append_item_into_file(filename, linepattern, newline):
    """ Detects the re 'linepattern' in the file. After its last occurrence,
    pastes each item of the input list line per line. If pattern doesn't exist
    notifies and leaves the file unchanged
    """
    oldfile = open(filename, 'r').read()
    lines = re.findall(linepattern, oldfile, flags=re.MULTILINE)
    if len(lines) == 0:
        print "Pattern {} not found. Could not write {} file".format(linepattern,oldfile)
        exit(1)
    else:
        last_line = lines[-1]
        newfile = oldfile.replace(last_line, last_line +newline)
    print newfile
    open(filename, 'w').write(newfile)

def copy_sources(args):
    """
    takes the contents of the sources file (which should be only a list) and adds it to the RFNOC_OOT_SRCS variable
    of the oot_Makefile.srcs, to be included into the build process
    """
    oot_dir = args.include_dir
    oot_srcs_dir = os.path.join(oot_dir,'rfnoc','fpga-src')
    dest_srcs_dir = os.path.join(os.getcwd(),'..','..','lib','rfnoc')
    srcs = compare (os.path.join(oot_srcs_dir,'Makefile.srcs'),os.path.join(dest_srcs_dir,'Makefile.scrs'))


def compare(file1,file2):
    """
    compares two files line by line, and returns a list of the lines of the first file that were not found on the second
    """
    notinside = []
    lists = []
    strings = ''
    with open(file1,'r') as arg1:
        with open(file2,'r') as arg2:
            text1 = arg1.readlines()
            text2 = arg2.readlines()
            for item in text1:
                if item not in text2:
                    notinside.append(item)
    lists = notinside
    strings = ''.join(notinside)
    return lists,strings

def zero_padd(noc_id):
    """
    checks if the number given for NoC ID is 16 digits long. If it is shorter, pads the until 16 with zeros. If it is longer,
    throws error, as it is not allowed
    """
    digits = len(noc_id)
    if (digits > 16):
        print "Invalid NoC ID - Please provide an ID shorter than 16 Hex Digits"
        #raise ModToolException('Invalid NoC ID - Only Hexadecimal Values accepted.')
        return
    else:
        while digits < 16:
            noc_id +='0'
            digits += 1
    return noc_id

def device_dict(args):
    """
    helps selecting the device building folder based on the targeted device
    """
    build_dir = {'x300':'x300','x310':'x300','e300':'e300'}
    return build_dir[args]

def     getScriptPath():
        return os.path.dirname(os.path.realpath(argv[0]))


def checkdir_v(include_dir):
    """
    Checks the existance of verilog files in the given include dir
    """
    nfiles = glob.glob(include_dir+'*.v')
    if (len(nfiles) == 0):
        print 'No verilog files found in the given directory'
        exit(0)
    else:
        print 'Verilog sources found!'
    return
