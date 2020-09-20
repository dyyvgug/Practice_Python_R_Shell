
df = read.table("codon_frequency.txt", sep = "\t", header = F )

a = aggregate(V3~V2, df, max)

df = merge(df, a , by.x = "V2", by.y = "V2")

df$CAI = round(df$V3.x/df$V3.y, 3)

category = function(x)   {
                if (x > 0.8)  {
                  y = 3
                }
                else if (x > 0.3 & x <= 0.8)  {
                  y = 2
                }
                else {
                  y = 1
                }
                return(y)
              }

df$cat = sapply(1:64, function(x) category(df[x,"CAI"]))
df = df[,c(-3, -4)]
names(df) = c("AA", "codon", "CAI", "rand")

write.table(df, "CBI_ref.txt", sep = "\t", row.names = F, quote = F)

## --------------------------------
## this part for calculation of CBI
## --------------------------------

df = read.table("ref/NC10_CBI_CAIavg.txt", sep = "\t", header = T)

df1 = read.table("ref/CBI.txt", sep = " ", header = F, skip = 1)

df1 = df1[ , apply(df1, 2, function(x) !any(is.na(x)))] # remove columns have NA

df = merge(df,df1, by.x = "transcription_id", by.y = "V1" )

df = df[,-5]

names(df)[5] = "CBI"

write.table(df, "ref/NC10_CBI_CAIavg.txt", sep = "\t",row.names = F)












