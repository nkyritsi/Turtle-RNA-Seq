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

    return oList



###make dictionary of organism: genes, so can count the number of values associated with organism
