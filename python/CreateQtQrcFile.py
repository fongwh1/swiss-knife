import copy
import sys
import string
import argparse
from os import listdir

imageAbsPath=""
prefix=""
subs=""

def CheckArg ():
    parser = argparse.ArgumentParser(description='Generate qrc items list under dir.')
    parser.add_argument('--path', help='absolute path of images')
    parser.add_argument('--prefix', help='prefix prepended to each images')
    parser.add_argument('--subs', help='subsitution', default="%s")

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    global imageAbsPath
    global prefix
    global subs

    imageAbsPath = parser.parse_args().path
    prefix = parser.parse_args().prefix
    subs = parser.parse_args().subs

def ListFile ():
    global imageAbsPath
    global prefix
    global subs

    filelist = [f for f in listdir(imageAbsPath)]
    filelist.sort()

    i=0
    while i < len(filelist):
        print "        ",str.replace(prefix, "%s", filelist[i])
        i += 1

if __name__ == "__main__":
    CheckArg()
    ListFile()

