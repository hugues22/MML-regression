library(caret)

data <- read.csv('/home/hugues/Documents/eclipse/workspace/MML-regression/org.xtext.example.mml.tests/programmeMML/Boston.csv') 

param_train <- trainControl(method='none')
trainset <- createDataPartition(data$medv, p=0.03, list = FALSE) 
training <- data[trainset,]
testing <- data[-trainset,]

fit <- train(medv ~  ., data = training, method='rf', trControl=param_train) 


pred <- predict(fit)


postResample(pred = pred, obs = training$medv)[2]
postResample(pred = pred, obs = training$medv)[3]
postResample(pred = pred, obs = training$medv)[1]
