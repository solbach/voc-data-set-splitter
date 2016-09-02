import os
import sys
import glob
import random

######################
# Generates four files
#
# trainval.txt
# test.txt
# train.txt
# val.txt
#
# location: ImageSets/
######################


def checkPath(path):
    if not os.path.isdir(path):
        print ">> " + path + " <<" + " does not exist."
        print "exit"
        sys.exit()
    return

def init(inputParam):
    print "\n##############"
    print "Pascal VOC style DATA-SET SPLITTER"
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

# Shuffle elements in anFiles
random.shuffle(anFiles)

# Get first set
anSet1 = anFiles[0:set1]
# Get second set
anSet2 = anFiles[set1+1:set1+1+set2]
# Get third set
anSet3 = anFiles[set2+1:set2+1+set3]

print len(anSet1)
print len(anSet2)
print len(anSet3)

print anSet1[0]

# Create directories
if not os.path.exists(path + "ImageSets/"):
    os.makedirs(path + "ImageSets/")

# Generating train.txt and trainval.txt
for ele in anSet1:
    start = ele.find('/n') + 1
    end = ele.find('.xml', start)
    eleClean = ele[start:end]
    print eleClean
    break

# Generating val.txt and trainval.txt
for ele in anSet2:
    start = ele.find('/n') + 1
    end = ele.find('.xml', start)
    eleClean = ele[start:end]
    print eleClean
    break

# Generating test.txt
for ele in anSet3:
    start = ele.find('/n') + 1
    end = ele.find('.xml', start)
    eleClean = ele[start:end]
    print eleClean
    break
