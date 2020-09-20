library(pheatmap)
test = matrix(rnorm(200), 20, 10)
test[1:10, seq(1, 10, 2)] = test[1:10, seq(1, 10, 2)] + 3
test[11:20, seq(2, 10, 2)] = test[11:20, seq(2, 10, 2)] + 2
test[15:20, seq(2, 10, 2)] = test[15:20, seq(2, 10, 2)] + 4
colnames(test) = paste("Test", 1:10, sep = "")
rownames(test) = paste("Gene", 1:20, sep = "")
head(test)
pheatmap(test)
pheatmap(test, scale = "row") # row normalization
pheatmap(test,scale = "row", clustering_method = "average") #default"complete",optional 'ward', 'ward.D', 'ward.D2', 'single', 'complete', 'average', 'mcquitty', 'median' or 'centroid'.
pheatmap(test, scale = "row", clustering_distance_rows = "correlation")# optional Pearson corralation，default distance "euclidean"
pheatmap(test, color = colorRampPalette(c("navy", "white", "firebrick3"))(50))
pheatmap(test, legend_breaks = c(1:5), legend_labels = c("1.0","2.0","3.0","4.0","5.0"))# range and label
pheatmap(test, legend = FALSE) # remove legend
pheatmap(test, border=FALSE) # remove border line
pheatmap(test, display_numbers = TRUE,number_color = "blue") # display the corresponding value
pheatmap(test, display_numbers = TRUE, number_format = "%.1e")
pheatmap(test, cellwidth = 15, cellheight = 12, main = "Example heatmap")