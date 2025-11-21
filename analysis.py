import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

knicks_pts_10 = nba_2010.pts[nba_2010.fran_id=='Knicks']
nets_pts_10 = nba_2010.pts[nba_2010.fran_id=='Nets']

#calculate the average points scored by Knicks and Nets in 2010 and their difference
knicks_mean_score = np.mean(knicks_pts_10)
nets_mean_score = np.mean(nets_pts_10)
diff_means_2010 = knicks_mean_score - nets_mean_score
print('Difference between the two teams average points scored:')
print(diff_means_2010)
print('\n')
#since the means are not the same, the team appears to influence how many points are scored in a game, this suggests that frand_id and pts are asssociated 

#compare the points by knicks and nets using overlapping histograms
plt.hist(knicks_pts_10, alpha = 0.8, normed=True, label='knicks')
#im using normed instead of density because of the older version of matplotlib used on codecademy
plt.hist(nets_pts_10, alpha=0.8, normed=True, label='nets')
plt.title('2010 season')
plt.show()
plt.close()
#by the histograms i can tell that the distributions don't appear to be the same, the blue one is shifted more to the left which means that team scores more points, the orange one is shifted more to the right , which means that team scores less points. The means, spread and shape are different.The blue team has more values above 100, while the orange team has more values around 85-95.


#calculate the average points scored by Knicks and Nets in 2014 and their difference
knicks_pts_14 = nba_2014.pts[nba_2014.fran_id=='Knicks']
nets_pts_14 = nba_2014.pts[nba_2014.fran_id=='Nets']

knicks_mean_score = np.mean(knicks_pts_14)
nets_mean_score = np.mean(nets_pts_14)
diff_means_2014 = knicks_mean_score - nets_mean_score
print('Difference between the two teams average points scored in 2014 is :')
print(diff_means_2014)
print('\n')

plt.hist(knicks_pts_14, alpha = 0.8, normed=True, label='knicks')
plt.hist(nets_pts_14, alpha=0.8, normed=True, label='nets')
plt.title('2014 season')
plt.show()
plt.close()
#the two distributions overlap, especially at the center,the teams had nearly identical scorring paterns in 2014, the mean difference is very small (~0.45)


#the relationship between points scored per game between all teams
sns.boxplot(data=nba_2010, x='fran_id', y='pts')
plt.title('Points per game in 2010')
plt.show()
plt.close()
#different teams have different scoring distribution,thunder and spurs tend to score more on average, while the nets consistenly score less points, since the scoring patterns change, fran_id and pts are associated variables

#check if teams tend to win more games at home compared to away in 210
location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)
print("This table shows if teams tend to win more games at home compared to away.")
print(location_result_freq)
print('\n')
#the table shows that teams win more often when playing at home,the variables are associated because the probability of winning depends on whether the game is played at home or away.

#convert the table of frequencies to a table of proportions
location_result_proportions = location_result_freq/len(nba_2010)
print("Table of proportions:")
print(location_result_proportions)
print('\n')

# Calculate expected contingency table and Chi-Square statistic
chi2, p, dof, contingency = chi2_contingency(location_result_freq)
print('Expected contingency table:')
print(contingency)
print('\n')
print('Chi-Square statistic:', chi2)
print('\n')


#calculate the covariance between forecast and point_diff
point_diff_forecast_cov = np.cov(nba_2010['forecast'], nba_2010['point_diff'])
print("The covariance between forecast and point_diff is:")
print(point_diff_forecast_cov)
print('\n')
#the covariance is positive (+1.37)

plt.close()
plt.scatter('forecast', 'point_diff', data=nba_2010)
plt.title('Forecast vs. Point Differential Scatter Plot')
plt.xlabel('Forecasted win probabilities')
plt.ylabel('Point Differential')
plt.show()
# the correlation value makes sense,the scatter plot shows positive trend, games with higher win probabilities tend to result in larger point margins. The upwars pattern in the plot matches the positive correlation value (1.37)

#OUTPUT:
  #         game_id  year_id  fran_id  ... game_result  forecast  point_diff
#21717  200910270CLE     2010  Celtics  ...           W  0.277472           6
#21718  200910280BOS     2010  Celtics  ...           W  0.814619          33
#21719  200910280MIA     2010   Knicks  ...           L  0.258755         -22
#21720  200910280MIN     2010     Nets  ...           L  0.475155          -2
#21721  200910280OKC     2010  Thunder  ...           W  0.716764          13

#[5 rows x 11 columns]
 #           game_id  year_id  fran_id  ... game_result  forecast  point_diff
#23468  201310300CLE     2014     Nets  ...           L  0.611981          -4
#23469  201310300NYK     2014   Knicks  ...           W  0.793150           7
#23470  201310300SAS     2014    Spurs  ...           W  0.692980           7
#23471  201310300TOR     2014  Celtics  ...           L  0.361233          -6
#23472  201310300UTA     2014  Thunder  ...           W  0.526056           3

#[5 rows x 11 columns]
#Difference between the two teams average points scored:
#9.731707317073173


#Difference between the two teams average points scored in 2014 is :
#0.44706798131809933


#This table shows if teams tend to win more games at home compared to away.
#game_location    A    H
#game_result            
#L              133  105
#W               92  120


#Table of proportions:
#game_location         A         H
#game_result                      
#L              0.295556  0.233333
#W              0.204444  0.266667


#Expected contingency table:
#[[119. 119.]
# [106. 106.]]


#Chi-Square statistic: 6.501704455367053


#The covariance between forecast and point_diff is:
#[[  0.05   1.37]
# [  1.37 186.56]]








