# nba-game-analysis
This project analyzes NBA game data from the 2010 and 2014 seasons using Python. It compares scoring between teams, examines scoring patterns between teams, home vs away win tendencies and explores the relationship between win forecasts and point differentials. Visualizations include histograms, boxplots, contingency tables and scatter plots. 
The project demnostrates data cleaning, visualizations, contingency tables and interpretation of results.

Technologies and librarys used:
- pandas for data loading
- numpy for numerical analysis
- matplotlib for plotting
- seaborn for statistical visualizations
- scipy.stats for correlation and chi-square test

The project analysis answers the following questions:

1. Do teams score differently? (Knicks vs Nets)
   - 2010 season: mean scorring difference ~ 9.7 points. Histograms show different spreads and centers.Teams score differently so the variables fran_id and pts are associated.
   - 2014 season: mean scoring difference ~ 0.45 points. Histograms show nearly identical scoring distributions.

2. Do all franchises score the same?
   - The boxplot used for all teams in 2010 shows highest medians for Thunder and Spurs, Knicks and Celtics in the middle, and Nets with lowest scoring. Different teams have different scoring distributions.

3. Do teams win more at home or away?
   - Using a contigency table we see more wins at home. Game_location and game_result are associated.

4. Are forecast win probabilities related to point differential?
   - Covariance = +1.37, as forecast rise, point differential tends to rise. 



