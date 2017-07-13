inputFile <- "GonadVol.csv"

##read file into data frame
gonadDF <- read.delim(file = inputFile, sep = ",")

###A Basic volcano plot
###PostFC and FDR are column labels
with(gonadDF, plot(log2(PostFC), -log10(FDR), pch=20, main="Volcano plot", xlim = c(-2.5, 2)))
