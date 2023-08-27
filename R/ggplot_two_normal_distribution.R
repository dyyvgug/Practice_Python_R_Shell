# Generate data for two normal distributions
mean1 <- 0
sd1 <- 1
x1 <- seq(-3, 3, by = 0.01)
y1 <- dnorm(x1, mean = mean1, sd = sd1)

mean2 <- 2
sd2 <- 1.5
x2 <- seq(-3, 6, by = 0.01)
y2 <- dnorm(x2, mean = mean2, sd = sd2)

# Create a blank plot
plot(x1, y1, type = "l", col = "blue", lty = 1, lwd = 2, ylim = c(0, 0.4), 
     xlab = "X-axis", ylab = "Density")

# Add the second normal distribution to the plot
lines(x2, y2, col = "red", lty = 2, lwd = 2)

# Add a legend
#legend("topright", legend = c("N(mean1, sd1)", "N(mean2, sd2)"), 
#       col = c("blue", "red"), lty = c(1, 2), lwd = 2)
df <- data.frame(
  x = c(x1, x2),
  y = c(y1, y2),
  group = factor(rep(c("N(mean1, sd1)", "N(mean2, sd2)"), each = length(x1)))
)

# Create the plot using ggplot2
ggplot(data = df, aes(x = x, y = y, color = group)) +
  geom_line(size = 1) +
  labs(x = "X-axis", y = "Density") +
  scale_color_manual(values = c("blue", "red")) +
  theme_minimal()

