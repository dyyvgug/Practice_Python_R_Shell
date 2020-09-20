setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
con <- file("out.txt", "r")
line=readLines(con,n=1)
while( length(line) != 0 ) {
  print(line)
  line=readLines(con,n=1)
}
close(con)
