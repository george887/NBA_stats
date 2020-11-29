![maxresdefault](https://user-images.githubusercontent.com/62911364/100548752-211a6c00-3234-11eb-949c-38d71486c989.jpg)
# NBA Classification Project

## Goal of Project
The goal of this project is to see what features help predict a team win using of NBA games played in 2014 through 2018. I will utilize the nba [games.stats.csv](https://www.kaggle.com/ionaskel/nba-games-stats-from-2014-to-2018) found on Kaggle. A jupyter notebook will document all phases of the project including data acquisition, data preparation, exploration and modeling. A README.md will be made to describe and reproduce project. 

# Project Planning
<details>
  <summary> Click to Expand 
  
## Data Acquisition
- Download [games.stats.csv](https://www.kaggle.com/ionaskel/nba-games-stats-from-2014-to-2018) on Kaggle.

## Data Preparation
Some data preparation was performed prior to exploring the data 
- Dummy variables were created for categorical variables of ```home``` team and ```winorloss``` to have binary values (0 & 1).   
- Some variable names were changed for easier interpretation (refer to the data dictionary).
- Split dataset into train, validate and test sets
- Equations found in prepare.py

## Explore
- Created an explore.py file
- File contains functions to help create plots
- Functions for KMeans, centroids, adding clusters/centroids to data frames and RFE ranker

</summary>

## Initial Thoughts
1. Is there a relationship between price_per_sqft and logerror?
2. Is there a relationship between bed_bath_ratio and logerror?
3. Is there a relationship between lot size per sqft and logerror?
4. Is there a relationship between lot size per sqft and price per sqft?

## Hypothesis Testing
> H<sub>0</sub>: Means of price_per_sqft_ratio small, medium, large are equal

> H<sub>a</sub>: Means of price_per_sqft_ratio small, medium, large are not equal

> H<sub>0</sub>: Means of bed_bath_ratio small, medium, large are equal

> H<sub>a</sub>: Means of bed_bath_ratio small, medium, large are not equal

## Data Dictionary
| Column | Description | Data Type |
| --- | ---| --- |
| bathroomcnt | Number of bathrooms including fractional bathrooms | float64 |
| bedroomcnt | Number of bedrooms | float64 |
| buildingqualitytypeid | Assessment of condition of home from best (lowest) to worst (highest) | float64 |
| sqft | Total squarefeet of home | float64 |
| fips | Federal Information Processing System codes - unique geographical areas | float64 |
| fullbathcnt | Number of full bathrooms | float64 |
| latitude | Latitude of the property | float64 |
| longitude | Longitude of the property | float64
| lotsizesquarefeet| Size of the lot in square feet | float64 |
| propertycountylandusecode | County land use code AKA zoning at the county level | object |
| roomcnt | Number of rooms in the property | float64 |
| unitcnt | Number of property units on the property | float 64 |
| yearbuilt | The year the property was built | float 64 |
| structuretaxvaluedollarcnt | The tax assessed value of the property structure | float64 |
| home_value | The tax accessed value of the property | float64 |
| taxamount | Property tax assessed for that year | float 64 |
| logerror | Zillow's Zestimate model. Difference in sale price and estimated price | float64 |
| transactiondate | Date of property purchase | object |
| heatingorsystemdesc | Type of heating system in home | object |
| county | Fips value converted to actual county | | object |
| age | Age of property | float64 | 

## Conclusions
- ANNOVA tests were ran on price per square feet and logerror & bed bath ratio and logerror
- Means were differnent in both test so the Ho was rejected
- Clusters were created comparing building quality type id & bed bath ratio, price per sqft & age, and price per sqft and lot size per sqft
- Dummy variables were created with clusters of price per sqft and lot size per sqft
- Modeling was performed with scaled data along with the cluster dummies
- The best model (Lassolars) did out perform the baseline RMSE 0.17374 on train and validate but did not on test 0.18188
- Further testing needs to be done to see how different features can help reduce the RMSE of logerror
- Look further into the relationship of binned bed bath ratio and logerror
- Create dummy variables with price per sqft and age to model

## How to reproduce

- Have access to the Codeup SQL data base
- Have credential in env.py file to establish a connection with the server
- Use wrangle.py file for data acquisition and data preperation
- Use explore.py file to explore
- Look at MVP_walkthru.ipynb to see analysis done

