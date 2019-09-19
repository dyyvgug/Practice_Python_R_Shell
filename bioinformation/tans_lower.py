#tran_lower.py
def getText():
    fasta = [ATXN1.fa,DDX5.fa,DHX9.fa,EWSR1.fa,FUS.fa,HnRNPA1.fa,TAF15.fa,TDP43.fa,TIA1.fa]
    fasta = "".join.fasta
    for i in fasta:
        txt = open(".fa","r").read()
        txt = txt.lower()
    for ch in '!@#$%^&*[]\{}\|?/><_+-=()~`':
        txt = txt.replace(ch," ")
    return txt
