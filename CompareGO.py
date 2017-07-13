###Function to create new file of shared GO terms between tissues

import csv

def GO(fileB, fileG, fileS):
    brainFile = open(fileB, "rt")
    gonadFile = open(fileG, "rt")
    sharedFile = open(fileS, "w")

    bReader = csv.reader(brainFile, delimiter=',')
    gReader = csv.reader(gonadFile, delimiter=',')

    bGO = []
    gGO = []
    sGO = []

    for row in bReader:
        GOterm = row[1]
        #print(GOterm, GOname, GOcat)
        bGO.append(GOterm)

    GOdict = {}
    for row in gReader:
        GOterm = row[1]
        GOname = row[2]
        GOcat = row[3]
        #print(GOterm, GOname, GOcat)
        gGO.append(GOterm)
        GOdict[GOterm] = [GOname, GOcat]

    for i in bGO:
        if i in gGO:
            sGO.append(i)
            items = GOdict.get(i)
            sharedFile.write(str(i) + "\t" + str(items[0]) + "\t" + str(items[1]) + "\n")
