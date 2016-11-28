#Workshop in R

#Easy math
1 + 3
5 - 3
5 * 10
1 / 103

#Sligthly less easy math
exp(130)
sqrt(130)
log(10)
log(10,10)

#Assigning variables
x
x <- 10
x
y <- 12
y
z <- 'JEST'
z

#Math with variables
x + y
x * y
x / y
sqrt(exp(y))
x * z

class(x)
class(z)

#Types of data
###Logical
###Numeric
###Complex
###Character

#Vectors
v1 <- c(10,301,3,4)
v1
v2 <- c('13',3,13,TRUE)
v2
v3 <- c('J','E','S','T')
v3
v4 <- c(FALSE,10,20)
v4

#Lists
l1 <- list('1',3,c(103,13,13))
l1

#Arrays
myarray <- array(c('J','E','S','T'),dim = c(4,2,2))
myarray

#Matrices
mymatrix <- matrix(v1,nrow = 10, ncol = 3,byrow = TRUE)
mymatrix
v1

#Picking Elements, Columns, Lines
print(mymatrix[,2])

print(mymatrix[2,])

print(mymatrix[2])

print(mymatrix[1,2])

subSetIris <- iris[iris$Sepal.Length < 5,]
subSetIris <- subset(iris, Sepal.Length < 5)
#Dataframes
mydataframe <- data.frame(myvalues = v2, JEST = v3)

print(mydataframe)

print(mydataframe[1])

ncol(mydataframe)

nrow(mydataframe)

dim(mydataframe)

#Getting your packages ready
install.packages('readr')
library('readr')
?read_csv
myfile <- read_csv('output_mon.csv')

#Boolean logic
#logical statements
k <- 6
j <- 'six'
k == 6
k < 6
k <= 6
j == 6
length(j) == 6
length(j) != 6
length(j) == 1

#logical operators
k|j == 6
k & j == 6

#logical statements

if (k > 0){
  print('k is positive')
}else{
  print('k is not positive')
}


#Looping - when NOT do loop
mysum <- 0
for (i in c(1:6)) {
  mysum <- mysum + i
}
mysum

#Find a function to do it for you!
mysum <- sum(c(1:6))
mymean <- mean(c(1:6))
individuals <- seq(6)

#Getting some stats from your data
mynewvector <- c(1,4,3,1,3,2,3)
myvar <- var(mynewvector)
mysd <- sqrt(myvar)
mysd <- sd(mynewvector)

###Tdyr,dplyr, Cleaning, processing and manipulating data

library(dplyr)
library(tidyr)

###tidyr

###complement with separate
compac_iris <- unite(iris, Area, c(Sepal.Width,Sepal.Length), sep= '*' ,remove = TRUE)

###dplyr
###Pick specific instances
filtered_iris <- filter(iris, Species=='setosa')

###Compact information
sum_iris <- summarize(iris, mean(Sepal.Width))

###Rearranje data
rear_iris <- arrange(iris, desc(Sepal.Width))

###Mutate Datasets
mut_iris <- mutate(iris, Area = Sepal.Width*Sepal.Length)

#Visualizing your data [IMPORTANT!]
anotherNameIris <- iris
colnames(iris)
rownames(iris)

###Scatterplot
plot(iris$Sepal.Length ~ iris$Petal.Length)
plot.new()

###Boxplots
?boxplot
boxplot(iris$Petal.Width ~ iris$Species)

###Histograms
hist(iris$Sepal.Length, main = '', xlab = 'Sepal Length',col = "grey40",
     border = "white", breaks = seq(from = 4, to = 8, by = 0.25))

plot.new()

###Visualizing a wide number of variables - checking for
###possible correlation
pairs(~Sepal.Width + Sepal.Length + Petal.Width + Petal.Length,
  data = iris,
  pch = 20)

library("psych")
pairs.panels(x = iris[,c(1,2,3,4)],
             smooth = 0.1,
             jiggle = TRUE,
             hist.col = "gray40",
             cex.cor = 0.5)

###ggplot2
library(ggplot2)
library(grid)
library(gridExtra)
?ggplot
plot.new()

p1 <- ggplot(iris, aes(x = Sepal.Length,color = Species)) +
  geom_histogram(bins = 20) +
  labs(x = "Sepal Length", y = 'Count') +
  ggtitle("Sepal Length Histogram") +
  theme(text = element_text(size=8),plot.title = element_text(lineheight=.8, size = 10, face="italic"))

p2 <- ggplot(iris, aes(x = Sepal.Length, y = Sepal.Width)) +
  geom_point(size = 0.1) +
  labs(x = "Sepal Length",y = 'Sepal Width') +
  ggtitle("Sepal length by sepal width") +
  theme(text = element_text(size=8),plot.title = element_text(lineheight=.8, size = 10, face="italic"))

p3 <- ggplot(iris, aes(x = Petal.Length, y = Petal.Width,color = Species)) +
  geom_smooth(data = iris, inherit.aes = FALSE,aes(y = Petal.Width, x =Petal.Length),method = "lm",size = 0.3) +
  geom_point(alpha = 1/5) +
  labs(x = "Petal Length",y = "Petal Width") +
  ggtitle("Petal length by petal width") +
  theme(text = element_text(size=8),plot.title = element_text(lineheight=.8, size = 10, face="italic"))

p4 <- ggplot(iris, aes(x = Petal.Length, y = Petal.Width)) +
  geom_density2d(alpha = 1/3) +
  labs(x = "Petal Length",y = "Sepal Length") +
  ggtitle("Petal Length by Petal Width - Density") +
  theme(text = element_text(size=8),plot.title = element_text(lineheight=.8, size = 10, face="italic"))

myLM <- lm(data = iris, Petal.Length ~ Petal.Width)
summary(myLM)
fullGrob <- arrangeGrob(p1,p2,p3,p4,top = "Several graphs about the iris dataset\n")
grid.arrange(fullGrob)
ggsave("myplot.pdf",fullGrob,width = 8.27,height = 11.69/2,units = "in")

p5 <- ggplot(iris, aes(x = Petal.Length, fill = Species)) +
  geom_density(alpha = 0.7,size = 0.3) + 
  ggtitle("Petal Length Density") + 
  labs(x = "Petal Length", y = "Density") +
  theme(text = element_text(size=8),
        plot.title = element_text(lineheight=.8, size = 10, face="italic"))

p6 <- ggplot(iris, aes(factor(Species),Sepal.Width)) + 
  geom_boxplot(outlier.color = NA, fill = NA, width = 0.5, lwd = 0) + 
  geom_point(position = position_jitter(width = 0.1),alpha = 0.3,size = 0.1) + 
  labs(x = "\nSpecies", y = "Sepal Width\n") +
  ggtitle("Sepal width by species") + 
  theme(text = element_text(size=8),
    plot.title = element_text(lineheight=.8, size = 10, face="italic"),
    axis.text.x = element_text(size = 6, color = "black", face = "bold"))

fullGrob <- arrangeGrob(p1,p2,p3,p4,p5,p6,top = "\nSeveral graphs about the iris dataset\n",heights = list(1,1,1),widths = list(1.1,0.9))
grid.arrange(fullGrob)
ggsave("myotherplot.pdf",fullGrob, width = 8.27,height = 11.69,units = "in")
?arrangeGrob

###caret
library(caret)

###Visualization
featurePlot(x = iris[, 1:4], 
            y = iris$Species,
            plot = "density", 
            ## Pass in options to xyplot() to 
            ## make it prettier
            scales = list(x = list(relation="free"), 
                          y = list(relation="free")), 
            adjust = 1.5, 
            pch = "|", 
            layout = c(4, 1), 
            auto.key = list(columns = 3))

###Preprocessing
train_iris <- iris[1:75,]
test_iris <- iris[76:150,]

preProcValues <- preProcess(train_iris, method = c("center", "scale"))

output <- predict(preProcValues,test_iris)
preProcValues

###Data Splitting

trainIndex <- createDataPartition(iris$Species, p = .8, 
                                  list = FALSE, 
                                  times = 1)

irisTest  <- iris[-trainIndex,]
irisTrain <- iris[ trainIndex,]

###Data training
library(caret)
knnFit1 <- train(Species ~ ., data = irisTrain, method = "knn")
knnFit1

knnTest <- predict(knnFit1,irisTest)
knnTest

###Model Scoring
scores <- confusionMatrix(data = irisTest$Species, reference = knnTest)
scores

###Another training model

nnFit1 <- train(Species ~ ., data = irisTrain, 
                method = "nnet")
nnFit1

nnTest <- predict(nnFit1,irisTest)
nnTest

nnscores <- confusionMatrix(data = irisTest$Species, reference = nnTest)
nnscores