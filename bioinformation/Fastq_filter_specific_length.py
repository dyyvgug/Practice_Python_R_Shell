#!/usr/bin/python
from optparse import OptionParser

parser = OptionParser()
parser.add_option("--infile", dest="infile", help="give a fasta file to me", metavar="FILE")
parser.add_option("--outfile",  dest="outfile", help="the name of oufput file [fasta]", metavar="FILE")
(options, args) = parser.parse_args()

fafile=file(options.infile,'r')
fafilter=file(options.outfile,'w')

i=0
for line in fqfile:
        #print i,i%4,line
        if i%2==0:
                seqID=line.strip("\n")
        elif i%2==1:
                sequence=line.strip("\n")                
                if len(sequence)>=300 :
                        fafilter.write(seqID+"\n"+sequence+"\n")
        i+=1

fafile.close()
fafilter.close()
