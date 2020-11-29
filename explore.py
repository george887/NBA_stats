import pandas as pd
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE, SelectKBest, f_regression

######################### Uses Recursive Feature Elimination (RFE) ############################

def rfe_ranker(train_scaled, y_train, k):
    '''
    Uses Recursive Feature Elimination (RFE) to rank the given features in order of their usefulness in
    predicting a win with a linear regression model.
    '''
    # creating linear regression object
    lm = LinearRegression()

    # fitting linear regression model to features 
    lm.fit(train_scaled, y_train)

    # creating recursive feature elimination object and specifying to rank 5 of the best features
    rfe = RFE(lm, k)

    # using rfe object to transform features 
    x_rfe = rfe.fit_transform(train_scaled, y_train)

    feature_mask = rfe.support_

    # creating train df for rfe object 
    rfe_train = train_scaled

    # creating list of the top features per rfe
    rfe_features = rfe_train.loc[:,feature_mask].columns.tolist()

    # creating ranked list 
    feature_ranks = rfe.ranking_

    # creating list of feature names
    feature_names = rfe_train.columns.tolist()

    # create df that contains all features and their ranks
    rfe_ranks_df = pd.DataFrame({'Feature': feature_names, 'Rank': feature_ranks})

    # return df sorted by rank
    return rfe_ranks_df.sort_values('Rank')

    ###################### Select Kbest #########################

def select_kbest(train_scaled, y_train, k):
    '''
    Takes in the predictors (train_scaled), the target (y_train), the number of features to select (k) 
    and returns the names of the top k selected features
    '''
    f_selector = SelectKBest(f_regression, k)
    f_selector = f_selector.fit(train_scaled, y_train)
    X_train_reduced = f_selector.transform(train_scaled)
    f_support = f_selector.get_support()
    f_feature = train_scaled.iloc[:,f_support].columns.tolist()
    return f_feature

    ################# Adding scaled columns ###########################

def add_scaled_columns(train, validate, test, scaler, columns_to_scale):
    ''' 
    This function takes in the train, validate, test, scaler and columns to scale and returns scaled
    columns
    '''
    new_column_names = [c + '_scaled' for c in columns_to_scale]
    scaler.fit(train[columns_to_scale])
    
    train_scaled = pd.DataFrame(scaler.transform(train[columns_to_scale]), 
                            columns=new_column_names, 
                            index=train.index)
    
    validate_scaled = pd.DataFrame(scaler.transform(validate[columns_to_scale]), 
                            columns=new_column_names, 
                            index=validate.index)
    
    test_scaled = pd.DataFrame(scaler.transform(test[columns_to_scale]), 
                            columns=new_column_names, 
                            index=test.index)
    
    return train_scaled, validate_scaled, test_scaled