# Practice PCA.From http://www.sthda.com/english/articles/31-principal-component-methods-in-r-practical-guide/112-pca-principal-component-analysis-essentials.
library("factoextra")
library("FactoMineR")
library("corrplot")

data("decathlon2")
head(decathlon2)
decathlon2.active = decathlon2[1:23, 1:10]
head(decathlon2.active)
head(decathlon2.active[, 1:6], 4)
# PCA(X, scale.unit = TRUE, ncp = 5, graph = TRUE)
res.pca = PCA(decathlon2.active,graph = FALSE)         
print(res.pca)
eig.val = get_eigenvalue(res.pca)
eig.val
fviz_eig(res.pca, addlabels = TRUE, ylim = c(0, 50))   # fviz_eig() or fviz_screeplot()
var = get_pca_var(res.pca)
var
head(var$coord)
head(var$cor)
head(var$cos2)
head(var$contrib)
fviz_pca_var(res.pca, col.var = "black")
head(var$cos2, 4)
corrplot(var$cos2, is.corr=FALSE)
# Total cos2 of variables on Dim.1 and Dim.2
fviz_cos2(res.pca, choice = "var", axes = 1:2)
# Color by cos2 values: quality on the factor map
fviz_pca_var(res.pca, col.var = "cos2",
             gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"), 
             repel = TRUE                             # Avoid text overlapping
)
# Change the transparency by cos2 values
fviz_pca_var(res.pca, alpha.var = "cos2")

fviz_pca_ind(res.pca)
fviz_pca_ind(res.pca, col.ind = "cos2", 
             gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"),
             repel = TRUE # Avoid text overlapping (slow if many points)
)
fviz_pca_ind(res.pca, pointsize = "cos2", 
             pointshape = 21, fill = "#E7B800",
             repel = TRUE # Avoid text overlapping (slow if many points)
)
#=======================================================================================
# Color by groups
#=======================================================================================
head(iris, 3)
# The variable Species (index = 5) is removed
# before PCA analysis
iris.pca <- PCA(iris[,-5], graph = FALSE)
fviz_pca_ind(iris.pca,
             geom.ind = "point", # show points only (nbut not "text")
             col.ind = iris$Species, # color by groups
             palette = c("#00AFBB", "#E7B800", "#FC4E07"),
             addEllipses = TRUE, # Concentration ellipses
             legend.title = "Groups"
)
