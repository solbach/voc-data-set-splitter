import os
import sys
import glob

def checkPath(path):
    if not os.path.isdir(path):
        print ">> " + path + " <<" + " does not exist."
        print "exit"
        sys.exit()
    return

def init(inputParam):
    print "\n##############"
    print "Pascal VOC style data-set splitter"
    print " by Markus Solbach "
    print "    solbach@cse.yorku.ca"
    print "##############\n"

    if len(inputParam) < 2:
        print "\nNot enough arguments (%i)" % len(inputParam)
        print "Usage: synchronize.py <folder>"
        print "<folder> needs subfolders: Annotations with .xml and JPEGImages .JPEG"
        print "exit"
        sys.exit()
    return

################## Main

init(sys.argv)
# Path to folder containing subdir 'Annotations' and 'JPEGImages'
path = str(sys.argv[1])
pathAn = path + "Annotation/*.xml"

# Check for Annotation subfolder
checkPath(path + "Annotation/")

anFiles = glob.glob(pathAn)
total = len(anFiles)
total = 4658
eqSplit = total / 3.0

set1 = total / 3
set2 = set1
set3 = total - (set1 + set2)

if (eqSplit - 3.0) > 0.5:
    set1 = set1 + 1
    set2 = set2 + 1
    set3 = set3 - 2

print "Total files found: %i" % total
print "Split into \n \ttrain-set: \t%i \n\tval-set: \t%i \n\ttest-set: \t%i" % (set1, set2, set3)