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
  
     <img width="1807" height="716" alt="Screenshot 2025-11-21 162444" src="https://github.com/user-attachments/assets/6acb2104-9fdf-4b88-888a-18627971fd63" />

<img width="1732" height="613" alt="Screenshot 2025-11-21 162453" src="https://github.com/user-attachments/assets/c686acda-ae6b-4c8e-9f75-97a7bb7cbc12" />

<img width="765" height="544" alt="Screenshot 2025-11-21 162500" src="https://github.com/user-attachments/assets/465b3605-75b2-4848-b935-edac582f9fdd" />

<img width="1725" height="406" alt="Screenshot 2025-11-21 162509" src="https://github.com/user-attachments/assets/f825d5d1-c52b-40f5-bc05-5c7bb371b9fa" />

<img width="842" height="547" alt="Screenshot 2025-11-21 162514" src="https://github.com/user-attachments/assets/4591f607-e5b7-468b-96bb-cf1b3eaf1935" />

