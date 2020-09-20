df = read.table("c_elegans_CBI_CAIavg.txt", sep = "\t", header = T)
df2 = read.table("c_elegans_CBI_CAIavg.txt", sep = "\t", header = T)

df = merge(df, df2, by.x = "transcription_id", by.y = "transcription_id")
df = df[df$CBI > -1,]
plot(df$avg_CAI, df$CBI, pch = 15, col = "red")
l = lm(CBI~avg_CAI
       , data = df)
abline(l)

cor.test(df$avg_CAI, df$CBI)
