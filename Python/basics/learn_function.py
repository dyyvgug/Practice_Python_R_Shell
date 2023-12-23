#!/usr/bin/python
import sys

def readin(filename,sep=','):
    fh = open(filename)
    filenames = fh.readline().rstrip().split(sep)
    db = []
    for line in fh:
        lst = line.rstrip().rstrip().split(sep)
        d = dict(zip(filenames,lst))
        db.append(d)
    fh.close()
    #print(filenames)
    #print(db[0])
    return (filenames,db)

# getcol
def getcol(res,key):
    col = []
    for row in res[1]: col.append(row[key])
    print(col)
    col_f = []
    for i in col: col_f.append(float(i))
    print(col_f)
    print("median", sum(col_f) / len(col_f))

# search --------------------------------------------------------
def search(res,key,value):
    sres=[]
    for row in res[1]:
        if row[key] == value:
            sres.append(row)
    print(sres)
    # method2
    check=lambda row:row[key]==value
    #check=lambda row:float(row["height"])>1.80 and float(row['weight'])>80
    for row in db:
        if check(row):
            sres.append(row)
    print(sres)
    return (filename,sres)

# output ---------------------------------------------------------
def output(res,out,sep=','):
    filename=out
    fh=open(filename,'w')
    print(sep.join(res[0]),file=fh)
    #fh.write(sep.join(filenames))

    for row in db:
        #fh.write(sep.join(row.values()))
        print(sep.join(row.values()),file=fh)
    fh.close()

# -----------------------------------------------------------
# main
# -----------------------------------------------------------
if __name__=="__main__":
    print("Main program is executed!")
    params=sys.argv[1:]
    filename=params.pop(0) if params else "adr.csv"
    sep=params.pop(0) if params else ","

    res=readin(filename=filename,sep=sep)
    (fieldnames,db)=res
    #print(res[0])
    #print(res[1])

    column=getcol(res,key="height")

    sres=search(res,key="ort",value="muenchen")
    (fieldname,sdb)=sres

    output(res,out="out.csv",sep=";")
    output(sres,out="sout.csv")

