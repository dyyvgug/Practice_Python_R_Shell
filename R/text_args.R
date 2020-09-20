library(getopt)
spec = matrix(c(
  'verbose', 'v', 2, "integer",
  'help'   , 'h', 0, "logical",
  'count'  , 'c', 1, "integer"), byrow=TRUE, ncol=4)
opt = getopt(spec)
print(opt$count)
print(opt$verbose)

if(F){
  command=matrix(c("bam","b",1,"character",
                   "bed","d",1,"character",
                   "png","p",1,"character",
                   "help","h",0,"logical"),byrow=T,ncol=4)
  args=getopt(command)
  if (!is.null(args$help) || is.null(args$bam) || is.null(args$png) || is.null(args$bed)) {
    cat(paste(getopt(command, usage = T), "\n"))
    q()
  }
  
}

