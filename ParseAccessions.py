###Module to pull out accession numbers for each contig from blast XML
###and write them to a new file

import xml.etree.ElementTree as ET

def parse(xmlFile, outFile):
    tree = ET.parse(xmlFile)
    finalL = open(outFile, "w")

    ##list of contigs, accession numbers
    accessionList = []

    #iterate through the xml and add all contigs and accessions to a list
    for node in tree.iter():
        if node.tag == "Iteration_query-def":
            contig = node.text
            accessionList.append(contig)

        if node.tag == "Hit_accession":
            accession = node.text
            accessionList.append(accession)


    #onyl take contigs that have accessions and their first accession hit and add to file
    newL = []
    for line in accessionList:
        if line[0] == "c":
            contig = line
            nextIX = accessionList.index(line) + 1
            if accessionList[nextIX][0] != "c":
                topAcc = accessionList[nextIX]
                newL.append((contig, topAcc))
                finalL.write(contig + "\t" + topAcc + "\n")

