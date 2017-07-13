###Module to filter out contigs with a log FC of less than 1.5
###Takes 2 files as parameter; csv file to be read, and a file to write to
import csv


##Function to filter out contigs with an FC <=1.5
def FC(file1, file2):
    unFiltered = open(file1, "rt")
    Filtered = open(file2, "w")

    reader = csv.reader(unFiltered, delimiter = ",")
    writer = csv.writer(Filtered)

    for row in reader:
        print(row[2])
        if float(row[2]) >= 1.5:
            writer.writerow(row)

##Make a new file of contgis w/FC >=1.5 and their accessions
def FCaccessions(file1, file2, file3):
    accessions = open(file1, "rt")
    FCcontigs = open(file2,"rt")
    FCaccs = open(file3, "w")

    Areader = csv.reader(accessions , delimiter = ",")
    FCreader = csv.reader(FCcontigs)

    #make dictionary of contigs and their accessions
    accDict = {}
    for row in Areader:
        #print(row[0])
        contig = row[0]
        accession = row[1]
        accDict[contig] = accession

    # list of all contigs
    FCcontigs = []
    for row in FCreader:
        FCcontigs.append(row[0])
        #print(row[0])


    for i in FCcontigs:
        if i in accDict:
            iAcc = accDict.get(i)
            FCaccs.write(i + "\t" + iAcc + "\n")


###function to filter out super low FC contigs and create new file of contigs and accessions
#contig	description	log(ABSFC)	PPEE	PPDE	PostFC	RealFC	FC (+/-)	ABS(FC)	E-value	sim		GO IDs	GO names
def lowFCs(file1, file2, file3):
    gContigAcc = open(file1, "rt")
    FCvals = open(file2, "rt")
    filteredFCaccs = open(file3, "w")

    CAreader = csv.reader(gContigAcc)#, delimiter = "\t")
    FCvalreader = csv.reader(FCvals)#, delimiter = ",")

    CAlist = []
    for row in FCvalreader:
        contig = row[0]
        FC = row[2]
        #print(contig, FC)
        #print(row[2])
        if float(FC) >= 0.5:
            CAlist.append(contig)

    ###build dict of contigs and accessions
    ContigAccDict = {}
    for row in CAreader:
        contig = row[0]
        acc = row[1]
        #print(contig, acc)
        ContigAccDict[contig] = acc

    ###iterate through filtered contigs and write them to a new file with their accessions
    for i in CAlist:
        if i in ContigAccDict:
            contig = i
            acc = ContigAccDict.get(i)
            #print(contig, acc)
            filteredFCaccs.write(contig + "\t" + acc + "\n")




