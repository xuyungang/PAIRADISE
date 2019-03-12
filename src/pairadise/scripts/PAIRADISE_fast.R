args<-commandArgs(TRUE)
library('PAIRADISE')
args
my.data=read.table(args[1],header = TRUE,colClasses = c(rep("character", 5), rep("numeric", 2)))
results <- pairadise(my.data, numCluster = 8, equal.variance = F)
write.table(cbind(results$exonID,results$raw.pvalues),file=args[2])

