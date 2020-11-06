from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

######################### Train Logistic Regression #################################

def logistic_regression(X_train, y_train):
    '''
    This function takes in X_train (features using for model) and y_train (target 'win') and performs logistic
    regression giving us accuracy of the model and the classification report
    '''
    # Calling out funtion
    logit = LogisticRegression()

    # Fit the training data set
    logit = logit.fit(X_train, y_train)

    # Make predictions
    y_pred = logit.predict(X_train)

    #Accuracy of model
    score = logit.score(X_train, y_train)

    print(f'The logistic regression models accuracy is {round(score * 100,2)}%\n')     
    print(f'Confusion Matrix\n {confusion_matrix(y_train, y_pred)}\n') 
    
    # Coefficients for each feature  
    coef_df = pd.DataFrame(logit.coef_)

    print(f'Classification Report\n {classification_report(y_train, y_pred)}')