setwd("C:/Users/Joe/Desktop/R/671 breast cancer")
library(ggplot2)
library(plyr)
data=read.table("breast-cancer-wisconsin.data.txt", sep=',', header=FALSE)
#average = 0.955+ 0.980+ 0.955+ 0.94+ 0.975+ 0.965+ 0.95+ 0.955+ 0.96+ 0.95

# ADD TEXTUAL DESCRIPTORS FOR EACH MASS CHARACTERISTIC FOR THE DOCUMENT-TERM MATRIX
thick <- as.vector(apply(as.matrix(data[1], mode="character"),1,paste,"clump",sep="",collapse=""))
size <- as.vector(apply(as.matrix(data[2], mode="character"),1,paste,"size",sep="",collapse=""))
shape <- as.vector(apply(as.matrix(data[3], mode="character"),1,paste,"shape",sep="",collapse=""))
adhesion <- as.vector(apply(as.matrix(data[4], mode="character"),1,paste,"adhesion",sep="",collapse=""))
single <- as.vector(apply(as.matrix(data[5], mode="character"),1,paste,"single",sep="",collapse=""))
nuclei <- as.vector(apply(as.matrix(data[6], mode="character"),1,paste,"nuclei",sep="",collapse=""))
chromatin <- as.vector(apply(as.matrix(data[7], mode="character"),1,paste,"chromatin",sep="",collapse=""))
nucleoli <- as.vector(apply(as.matrix(data[8], mode="character"),1,paste,"nucleoli",sep="",collapse=""))
mitoses <- as.vector(apply(as.matrix(data[9], mode="character"),1,paste,"mitoses",sep="",collapse=""))

training_data <- cbind(data[10],thick,size,shape,adhesion,single,nuclei,chromatin,nucleoli,mitoses)


# [OPTIONAL] SUBSET YOUR DATA TO GET A RANDOM SAMPLE
training_data <- training_data[sample(1:699,size=600,replace=FALSE,),]
training_codes <- training_data[1]
training_data <- training_data[-1]
library(tm)
# CREATE A TERM-DOCUMENT MATRIX THAT REPRESENTS WORD FREQUENCIES IN EACH DOCUMENT
# WE WILL TRAIN ON THE Title and Subject COLUMNS
matrix <- create_matrix(training_data, language="english", removeNumbers=FALSE, stemWords=FALSE, removePunctuation=FALSE, weighting=weightTfIdf)

# ARTICLE TRAINING SET AND A 400 ARTICLE TESTING SET.
container <- create_container(matrix,t(training_codes),trainSize=1:200, testSize=201:600,virgin=FALSE)


# THERE ARE TWO METHODS OF TRAINING AND CLASSIFYING DATA.
# ONE WAY IS TO DO THEM AS A BATCH (SEVERAL ALGORITHMS AT ONCE)
models <- train_models(container, algorithms=c("SVM"))

#models <- train_models(container, algorithms=c("MAXENT","SVM","GLMNET","SLDA","TREE","BAGGING","BOOSTING","RF"))
results <- classify_models(container, models)


# VIEW THE RESULTS BY CREATING ANALYTICS
analytics <- create_analytics(container, results)

#didn't use#from online to build sample data/training
#require(caTools)
#sample = sample.split(bc671, SplitRatio = .80)
#train = subset(bc671, sample == TRUE)
#test = subset(bc671, sample == FALSE)


