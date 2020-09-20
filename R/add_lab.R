
library(ggplot2)

p11 <- ggplot(data = iris, aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_smooth(method = "lm", se=FALSE, color="red", formula = y ~ x) +
  geom_point(color = "blue")
p11

model.lm <- lm(Sepal.Length ~ Sepal.Width, data = iris)
summary(model.lm)

l <- list(a = format(coef(model.lm)[1], digits = 4),
          b = format(abs(coef(model.lm)[2]), digits = 4),
          r2 = format(summary(model.lm)$r.squared, digits = 4),
          p = format(summary(model.lm)$coefficients[2,4], digits = 4))

eq <- substitute(italic(Sepal.Length) == a - b %*% italic(Sepal.Width)~","~italic(R)^2~"="~r2~","~italic(P)~"="~p, l)

p12 <- p11 + geom_text(aes(x = 6.5, y = 2, label = as.character(as.expression(eq))), parse = TRUE)
p12
