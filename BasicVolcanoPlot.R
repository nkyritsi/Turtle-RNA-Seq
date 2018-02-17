#Reference:
#http://www.gettinggeneticsdone.com/2014/05/r-volcano-plots-to-visualize-rnaseq-microarray.html

inputFile <- "GonadVol.csv"

##read file into data frame
gonadDF <- read.delim(file = inputFile, sep = ",")

###A Basic volcano plot
###PostFC and FDR are column labels
with(gonadDF, plot(log2(PostFC), -log10(FDR), pch=20, main="Volcano plot", xlim = c(-2.5, 2)))

##Add colored points; red if p<0.05, orange if log2FC>0.5849625 (FC > 1.5), green if both
with(subset(gonadDF, FDR<.05), points(log2(PostFC), -log10(FDR), pch=20, col="red"))
with(subset(gonadDF, abs(log2(PostFC))>0.5849625), points(log2(PostFC), -log10(FDR), pch=20, col="orange"))
with(subset(gonadDF, FDR<0.05 & abs(log2(PostFC))>0.5849625), points(log2(PostFC), -log10(FDR), pch=20, col="green"))
