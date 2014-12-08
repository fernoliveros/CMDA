import pandas as pd
import pickle

import visuals
import regression
import predictwin

# 1
# Import the data and save it as a pickle
cfb = pd.read_csv('data/cfb2013stats.csv')
with open('cfb_pickle.pickle', 'wb') as handle:
  pickle.dump(cfb, handle)

  
# 2
# Provide at least one reshaping technique implementation

# For this, we take the scoring offense of each team for each game
# and break it into bins: low, medium, and high.
cfb.ScoreOffCat = pd.cut(cfb.ScoreOff, [0, 14, 35, 222], labels=["low", "medium", "high"])
cfb.ScoreDefCat = pd.cut(cfb.ScoreDef, [0, 14, 35, 222], labels=["low", "medium", "high"])


# 3
# Provide at least one treatment for missing data

# Our only missing data is the Vegas odds line for some of the games
# which were not bet on. Setting this equal to the average line would make
# no sense
cfb = cfb.applymap(lambda x: None if isinstance(x, basestring) and x.isspace() else x)

  
# 4
# Provide and comment on numerical summaries for at least three variables (at
# least one categorical and at least one numeric). You can use Python code or R
# code with pyper.

cfb.Date.describe() 		# Date of the game
cfb.TeamName.describe() 	# This team's name
cfb.ScoreOff.describe() 	# This team's total score
cfb.RushAttOff.describe() 	# This team's rush attempts
cfb.RushYdsOff.describe() 	# This team's rush yards
cfb.PassAttOff.describe() 	# This team's passing attempts
cfb.PassCompOff.describe()     # This team's passing completions
cfb.PassYdsOff.describe() 	# This team's total passing yards
cfb.PassIntOff.describe() 	# How many interceptions this team has thrown
cfb.FumblesOff.describe() 	# How many fumbles this team has had

cfb.Opponent.describe() 	# Opponent's name
cfb.ScoreDef.describe() 	# Opponent's total score
cfb.RushAttDef.describe() 	# Opponent's rush attempts
cfb.RushYdsDef.describe() 	# Opponent's rush yards
cfb.PassAttDef.describe() 	# Opponent's passing attempts
cfb.PassCompDef.describe()     # Opponent's passing completions
cfb.PassYdsDef.describe() 	# Opponent's total passing yards
cfb.PassIntDef.describe() 	# How many interceptions the opponent has thrown
cfb.FumblesDef.describe() 	# How many fumbles the opponent has had

cfb.Site.describe() 		# Whether the game was home, away, or at a neutral site
cfb.Line.describe() 		# Vegas betting line; Human prediction of score

cfb.ScoreOffCat.describe()     # This teams score broken into categories
cfb.ScoreDefCat.describe()     # Opposing team's score broken into categories


# 5
# Visuals

visuals.run()


# 6
# Machine learning

regression.run()
predictwin.run()