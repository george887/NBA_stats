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
    print(f'Confusion Matrix\n\n {confusion_matrix(y_train, y_pred)}\n') 
    
    # Coefficients for each feature  
    coef_df = pd.DataFrame(logit.coef_)

    print(f'Classification Report\n {classification_report(y_train, y_pred)}')

    ######################## Decesion Tree ############################
def decesion_tree(X_train, y_train, k):
    '''
    This function requires X_train, y_train and k (max_depth). A confusion matrix, models accuracy and 
    classification report are outputed
    '''
    # Creating the decision tree object
    clf = DecisionTreeClassifier(max_depth=k, random_state=123)

    # Fitting the data to the trained data
    clf.fit(X_train, y_train)

    # Array of the win/loss
    y_pred = clf.predict(X_train)

    # Estimate the probaility of win
    y_pred_proba = clf.predict_proba(X_train)

    # Confusion matrix
    print(f'Confusion Matrix: \n\n {confusion_matrix(y_train, y_pred)}\n' )

    print('The decision tree classifier accuracy : {:.2f}\n'
         .format(clf.score(X_train, y_train)))
    print("Decesion Tree Model Classification Report:\n", classification_report(y_train, y_pred))

    ####################### Random Forest ###################################
def random_forest(X_train, y_train, k):
    # Random forest object
    rf = RandomForestClassifier(n_estimators=100, max_depth=k, random_state=123)

    # Fitting the model
    rf.fit(X_train, y_train)

    # Make predictions
    y_pred = rf.predict(X_train)

    # Estimate the probability of a passenger surviving, using the training data
    y_pred_proba = rf.predict_proba(X_train)

    # Accuracy
    rf.score(X_train, y_train)

    # Confusion matrix
    print(f'Confusion Matrix: \n\n {confusion_matrix(y_train, y_pred)}\n' )

    print('The random forest accuracy : {:.2f}\n'
             .format(rf.score(X_train, y_train)))
    print("Random Forest Model Classification Report:\n", classification_report(y_train, y_pred))

    ########################## KNN ###################################
def knn(X_train, y_train, k):
    # KNN object
    knn = KNeighborsClassifier(n_neighbors=k, weights='uniform')

    # Fit the model
    knn.fit(X_train, y_train)

    # Make predictions
    y_pred = knn.predict(X_train)

    # Estimate the probability
    y_pred_proba = knn.predict_proba(X_train)

    # Confusion matrix
    print(f'Confusion Matrix: \n\n {confusion_matrix(y_train, y_pred)}\n' )

    print('The k-neareast neighbor accuracy : {:.2f}\n'
                 .format(knn.score(X_train, y_train)))
    print("K-Nearest Neighbor Classification Report:\n", classification_report(y_train, y_pred))