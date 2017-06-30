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

    #print(len(oList))
    oDict = {}

    #split each element in the list with "['
    for i in oList:
        geneL = [i] ##need to make list of each line to split
        for j in geneL:
            parts = j.split("[")
            uneditedOr = parts[1]
            gene = parts[0]
            organism = uneditedOr[:-1]

            ##add genes and their organism hits to a dictionary
            ###FIIIXX
            oDict[organism] = []
            if gene not in oDict[organism]:
                oDict[organism].append(gene)



###make dictionary of organism: genes, so can count the number of values associated with organism