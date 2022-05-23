# sample function

df <- data.frame(a1 = 1:10,
                 a2 = letters[1:10],
                 a3 = letters[1:10],
                 a4 = letters[1:10],
                 a5 = letters[1:10],
                 a6 = letters[1:10],
                 a7 = letters[1:10],
                 a8 = letters[1:10],
                 a9 = letters[1:10],
                 a10 = letters[1:10])

df_len <- length(df)

df_sample <- df[sample(seq_len(df_len), size = 5,replace = T), ]

df_sample
