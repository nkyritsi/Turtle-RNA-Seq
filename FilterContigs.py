###program to filter out the contigs that did not obtain any significant annotations
###so that only a file with significant annotations and their fc, e-values remain
import csv
import sys

def filterNA(inFile, outFile):
    ifile = open(inFile, "rt")
    ofile = open(outFile, "w")

    reader = csv.reader(ifile, delimiter='\t')
    writer = csv.writer(ofile)

    #write each annotated contig to a new file
    for row in reader:
        #print(row[1])
        if row[1] != "---NA---":
            writer.writerow(row)

def filterGO(inFile, outFile):
    ifile = open(inFile, "rt")
    ofile = open(outFile, "w")

    reader = csv.reader(ifile, delimiter='\t')
    writer = csv.writer(ofile)

    # write each annotated contig to a new file
    for row in reader:
        print(row[11])
        if row[11] != "":
            writer.writerow(row)

def filterFC(inFile, outFile):
    ifile = open(inFile, "rt")
    ofile = open(outFile, "w")

    reader = csv.reader(ifile, delimiter = '\t')
    writer = csv.writer(ofile)

    #for ever row that has a logFC greater or equal to 1.5, it is written into a new file
    for row in reader:
        #input the row index that contains the FC value
        if row[1] >= 1.5:
            writer.writerow(row)


#def main():
#    inFile = sys.argv[1]
#    outFile = sys.argv[2]
#    filter(inFile, outFile)




