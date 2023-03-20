#merge two table by two column
X <- data.frame(A = c("a", "b", "c"), B = c(1, 2, 3))
Y <- data.frame(A = c("a", "b", "c", "d", "e", "f", "g", "h", "i", "j"),
                B = c(1, 2, 11, 4, 5, 6, 7, 8, 9, 10),
                C = c(11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
merged <- merge(X, Y, by = c("A", "B"))
merged2 <- merge(X, Y, by = c("A", "B"), all.x = TRUE)
