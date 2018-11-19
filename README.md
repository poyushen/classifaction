# Classifaction

## This is a repository for finding the difference between `real rule` and `the rule that classifier finds`.

### The dataset is designed to predict whether a person will break the contract or not.
### Features: Gender, Age, Married, Payment_Method, Has_Kids, Income, Contract_Length
The dataset I designed is in `data.csv`.  
The rules I used are :  
* Age < 30 && Has_Kids = 1 && Income < 35000 & Contract_Length < 20 --> Label = 1    

* Two classifiers are used in this project:
	* `DecisionTreeClassifier`: you can see the result in `decision_tree.png`  
	* `XGBClassifier`: you can see the result in `./xgb_tree`  

In `./decision_tree.png`, you can see that the rules of the tree are:  
* Age <= 30.5 && Has_Kids <= 0.5 && Income <= 35500.0 && Contract_Length <= 25.0 --> Label = 1  
The rules matches the rules I designed approximately.  

In `xgb_tree`, you can see the rules of the tree are:  
* Age < 30.5 && Has_Kids < 0.5 && Income < 34500 --> Label = 1  
The rules miss some samples in the dataset.  
