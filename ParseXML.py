import xml.etree.ElementTree as ET

def xml(xmlFile):
    tree = ET.parse(xmlFile)

    #list of gene names with [organism] at the end
    oList = []

    #parse through xml assembly, pull out all hits with gene name and organism and add to
    #an empty list
    for node in tree.iter('Hit_def'):
        if node.tag == "Hit_def":
            geneOrg = node.text
            if geneOrg not in oList:
               oList.append([geneOrg])

    #print(oList)
    
    newL = []

    #split each element in the list with "[' to separate organism name from rest of gene
    for i in oList:
        #geneL = [i] ##need to make list of each line to split
        for j in i:
            parts = j.split("[")
            #some genes do not have associated organism, so those will not be added to the list
            if len(parts) > 1:
                uneditedOr = parts[1]
                gene = parts[0]
                organism = uneditedOr[:-1]
                newL.append([organism, gene])

    #final, clean list of (orgnism, gene) pairs
    finalL= []
    for i in newL:
        gene = i[1]
        if len(i[0]) > 30:
            stringOr = str(i[0])
            organism = stringOr.split("]")[0]
            finalL.append([organism, gene])
        else:
            organism = i[0]
            finalL.append([organism, gene])

    #print(finalL)
    
    #build dictionary of organism and all its associated genes
    oDict = {}
    for i in finalL:
        organism = i[0]
        gene = i[1]

        #if the organism is not in the dictionary, add it with a list to be able to add multiple genes
        if oDict.get(organism) == None:
            oDict[organism] = []
            oDict[organism].append(gene)
        else:
            oDict[organism].append(gene)

    return oDict


###make dictionary of organism: genes, so can count the number of values associated with organism
