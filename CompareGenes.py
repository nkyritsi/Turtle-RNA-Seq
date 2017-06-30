##Function to compare genes found in turtle brain tissue with those in turtle gonad tissue
##by creating two lists of genes and checking whether a gene is found in the other
import csv

def compareGenes(file1, file2, sameGenesFile):
    brainFile = open(file1, "rt")
    gonadFile = open(file2, "rt")
    file3 = open(sameGenesFile, 'w')

    bReader = csv.reader(brainFile, delimiter = ',')
    gReader = csv.reader(gonadFile, delimiter = ',')

    #list of brain genes
    bList = []
    #list of gonad genes
    gList = []
    #list of shared genes
    sList = []

    #build list of brain genes
    for row in bReader:
        gene = row[1]
        bList.append(gene)

    #build list of gonad gene
    for row in gReader:
        gene = row[1]
        gList.append(gene)

    file3.write('List of Shared Genes in RNA Brain and Gonad Tissue of Sea Turtles' + "\n" + "\n")
    file3.write('Number of Genes in Brain Tissue with BLAST annotations: ' + str(len(bList)) + '\n')
    file3.write("Number of Genes in Gonad Tissue with BLAST annotations: " + str(len(gList)) + "\n")
    #file3.write("Number of Shared genes between brain and gonad tissue: " + str(len(sList)) + '\n')

    #build list of shared genes
    for i in gList:
        if i in bList:
            sList.append(i)
            file3.write(str(i) + "\n")

    file3.write("Number of Shared genes between brain and gonad tissue: " + str(len(sList)) + '\n')

def compareOrganisms()