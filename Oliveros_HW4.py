import pandas as pd
import matplotlib as mpl
from pylab import *
import pickle

# 3) Import your data set to pandas. Re-create any reshaping operations you did in R for homework 
#2. If your dataset is new, provide a short data manual as a separate pdf.

# No reshaping needed
data = pd.read_csv('cfb2013stats.csv')

# 4) Get numerical summaries for all your variables. 

data.TeamName.describe() # Offensive team's name
data.Site.describe() # Game played at home, away, or neutral
data.Date.describe() # Date of game
data.Opponent.describe() # Opposing team
data.Line.describe() # Vegas line
data.ScoreOff.describe() # Total score offensive team
data.ScoreDef.describe() # Total score defensive team
data.RushYdsOff.describe() # Offensive team's rush yards
data.RushYdsDef.describe() # Defensive team's rush yards
data.RushAttOff.describe() # Offensive team's rush attempts
data.RushAttDef.describe() # Defensive team's rush attempts
data.PassYdsOff.describe() # Total passing yards for offensive team
data.PassYdsDef.describe() # Total passing yards for defensive team
data.PassIntOff.describe() # Offensive team's interceptions
data.PassIntDef.describe() # Defensive team's interceptions
data.PassCompOff.describe() # Offensive team's passing completions
data.PassCompDef.describe() # Defensive team's passing completions
data.PassAttOff.describe() # Offensive team's passing attempts
data.PassAttDef.describe() # Defensive team's passing attempts
data.FumblesOff.describe() # Fumbles by opposing team
data.FumblesDef.describe() # Fumbles by the defensive team

# 5
# Replace missing lines with 0's
data.Line.replace(' ', '0', inplace=True)

# 6
# No transformations needed

#7) Get three visualizations that you consider meaningful.
plot(data.PassAttOff, data.PassCompOff, hold = False)
xlabel('Pass Attemps')
ylabel('Pass Completions')
savefig("fig1.png")

plot(data.RushAttOff, data.RushYdsOff, hold = False)
xlabel('Rush Attempts')
ylabel('Rushing Yards')
savefig("fig2.png")

hist(data.ScoreOff, hold = False)
title("Score Offense")
savefig("fig3.png")

pickle.dump(data, open( "data_fr_pickle.p", "wb" ))