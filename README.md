![maxresdefault](https://user-images.githubusercontent.com/62911364/100548752-211a6c00-3234-11eb-949c-38d71486c989.jpg)
# Drivers of Winning in the NBA

## Goal of Project
The goal of this project is to see what features help predict a team win using of NBA games played in 2014 through 2018. I will utilize the nba [games.stats.csv](https://www.kaggle.com/ionaskel/nba-games-stats-from-2014-to-2018) found on Kaggle. A jupyter notebook will document all phases of the project including data acquisition, data preparation, exploration and modeling. A README.md will be made to describe and reproduce project.

# Project Planning
  
## Data Acquisition
- Download [games.stats.csv](https://www.kaggle.com/ionaskel/nba-games-stats-from-2014-to-2018) on Kaggle.

## Data Preparation
Some data preparation was performed prior to exploring the data 
- Dummy variables were created for categorical variables of ```home``` team and ```winorloss``` to have binary values (0 & 1).   
- Some variable names were changed for easier interpretation (refer to the data dictionary).
- Split dataset into train, validate and test sets
- Equations found in prepare.py

## Explore
- Created an explore.py file containing the recursive Feature Elimination function, Select K-Best function and scaled data frames to aid in modeling.

## Model
- Classification models performed using model.py
- Logistic Regression, Decision Tree, Random Forest and K-Nearest Neighbor algorithms performed

## Initial Thoughts
1. Team points and opponent points will tell me if a team wins or loses. I will not be using this in my analysis
2. Field goal pct or field goals attempted will help in predicting a win.
3. 3 pt pct, assists, and total rebounds will help predict a win.
4. Home team will win more games than road team.

## Hypothesis Testing
> H<sub>0</sub>: Does field goal percentage influence a win? Alpha < .05 so we reject the null hypothesis H<sub>0</sub> 

> H<sub>a</sub>: Does field goals attempted influence a win? Alpha > .05 so we fail to reject the null hypothesis H<sub>0</sub> 

> H<sub>0</sub>: Does 3 point shot percentage influence a win? Alpha < .05 so we reject the null hypothesis H<sub>0</sub> 

> H<sub>a</sub>: Does assists influence a win? Alpha < .05 so we reject the null hypothesis H<sub>0</sub> 

> H<sub>a</sub>: Does total rebounds influence a win? Alpha < .05 so we reject the null hypothesis H<sub>0</sub> 

> H<sub>a</sub>: Does having home court influence a win? Alpha < .05 so we reject the null hypothesis H<sub>0</sub> 


## Data Dictionary
  
| **Column** | **Definition** |
| :------- | :-------|
| team | Name of the home team  |
| game | Game number in season |
| date | Date game played |
| opponent | Opponent team name |
| teampoints | Home team score |
| opponentpoints | Opponent score|
| fieldgoals | Number of field goals made by home team|
| fieldgoalsattempted | Number of field goals attempted by home team|
| fieldgoal_pct | Field goal percentage for home team |
| x3pointshots | 3 point shots made by the home team |
| freethrows | Free throws made by the home team |
| freethrowsattempted | Free throws attempted by home team |
| freethrows_pct | Free throw percentage of home team|
| offrebounds | Number of offensive rebounds by the home team |
| totalrebounds | Total number of rebounds by the home team |
| assists | Number of assist by the home team |
| steals | Number of steals by the home team |
| blocks | Number of blocks by the home team |
| turnovers | Number of turnovers by the home team |
| totalfouls | Number of fouls by the home team |
| opp.fieldgoals| Opponents field goal percentage |
| opp.fieldgoalsattempted| Opponents field goals attempted |
| opp_fieldgoal_pct | Opponents field goal percentage |
| opp.3pointshots | Opponents 3 point shots made |
| opp.3pointshotsattempted | Opponents 3 point field goal percentage attempted |
| opp_3pointshots_pct | Opponents 3 point field goal percentage |
| opp.freethrows | Opponents free throws made |
| opp.freethrowsattempted | Opponents free throws attempted |
| opp_freethrows_pct | Opponents free throw percentage |
| opp.offrebounds | Opponents offensive rebounds |
| opp.totalrebounds | Opponents total rebounds |
| opp.assists | Opponents total number of assists |
| opp.steals | Opponents total number of steals |
| opp.blocks | Opponents total number of blocks |
| opp.turnovers | Opponents total number of turnovers |
| opp.totalfouls | Opponents total fouls |
| is_home | Away team = 0 Home team = 1 |

| **Target** | **Definition** |
| :------- | :-------|
| win | Loss = 0 win = 1 |
  
## Conclusions
- There are many features that can influence a win
- Picked a variety of the top features found in RFE and SelectKBest
- Feature in modeling include:
    - fieldgoals_pct, opp.fieldgoals_pct, opp.3pointshots, 3pointshots, opp.totalfouls, totalfouls, assist, and opp.assist
- Baseline accuracy of a win = 50%
- Scaled trained data fit with Logistic Regression, Decision Tree, Random Forest, and K-NearestNeighbor
- All models moved to validation phase
- Logistic Regression accuracy performed the best with 87% on test
    | **Model** | **Train** | **Validate** | **Test** |
    | :------- | :-------| :-------| :-------|
    | Logistic Regression | 86% | 86% | 87% |
    | Decision Tree | 82% | 79% | NA |
    | Random Forest | 85% | 83% | NA |
    | KNN | 88% | 82% | NA |
- Logistic Regression model accuracy was consistent through all phases of testing 
- Going foward, further testing can be done to optimize the best features to predict a win.
- Injuries play a big factor in the success of a team. I did not account for this in my models and information was not in data set. It would be interesting to see how models will perform with this data

## How to reproduce

- Download [games.stats.csv](https://www.kaggle.com/ionaskel/nba-games-stats-from-2014-to-2018) on Kaggle
- Download prepare.py and model.py files to use in exploring and modeling data
- Read through MVP_walkthru.ipynb to see analysis done

