# Calculate combination and permutation.Yingying Dong.

# =================================================
# METHOD 1 
# Combinat package
# =================================================
library(combinat)

# generating combinations of alphabets taking 2 at per time
print("Combination of letters 2 at a time")
print(letters)

# -------------------------------------------------
# Combination 
# -------------------------------------------------
combn(letters[1:4], 2)
combn(letters[1:4], 2, simplify = F)
print ("Combination where x=m")
# selecting 8 items out of 8 
combn(8,8)
# selecting 7 items out of 8
combn(8,7)
# getting counts of the combination
res <- combn(letters[1:4], 2)
print(paste0("Numbers of combination: ",ncol(res)))
# --------------------------------------------------
# Permutation
# --------------------------------------------------
# generating permutations of the number 3
permn(3)
# permutations of colors
x <- c("red","blue","white","green","black","violet")
print ("Permutations of colors")
permn(x)
res <- permn(x)
print(paste0("Number of possible permutations : ",length(res)))
# ==================================================
# METHOD 2
# gtools package
# it can calculate permutation with or without replacement
# ==================================================
library(gtools)
# --------------------------------------------------
# combination
# --------------------------------------------------
# generating combinations of 5 numbers taking 2 at per time
combinations(n = 5,r = 2) # or combinations(5，2)
# specify numbers
y <- c(5:9)
res1 <- combinations(n = 5, r = 2, v = y) # or combinations(5,2,y)
print(res1)
print(paste0("Number of combinations without replacement: ",nrow(res1)))
res1_r <- combinations(5,2,y,repeats.allowed = T)
print(res1_r)
print(paste0("Number of combinations with replacement: ",nrow(res1_r)))
# --------------------------------------------------
# permutation
# --------------------------------------------------
vec<- LETTERS[1:4]
# getting permutation on choose 2 letters from 4 letters without replacement 
res <- permutations(n = 4, r = 2, v = vec)
print(res)
print(paste0("Number of permutations without replacement: ",nrow(res)))
# with replacement
res2 <- permutations(n = 4, r = 2,  v = vec, repeats.allowed = T)
print(res2)
print(paste0("Number of permutations with replacement: ",nrow(res2)))
