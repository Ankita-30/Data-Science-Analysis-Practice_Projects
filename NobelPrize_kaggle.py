## Analyzing 


# ..... Load libraries .... #
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
# ..... Load libraries .... #

# Reading in the Nobel Prize data from Kaggle
nobel=pd.read_csv(r'/Users/ankita/Desktop/Kaggle/nobel_prize.csv')

# Taking a look at the first several winners
nobel.head(n=6)

# Display the number of (possibly shared) Nobel Prizes handed
# out between 1901 and 2016
print(len(nobel))

# Display the number of prizes won by male and female recipients.
print(nobel['gender'].value_counts())

# Display the number of prizes won by the top 10 nationalities.
nobel['birth_country'].value_counts().head(10)

# Calculating the proportion of USA born winners per decade
nobel['usa_born_winner'] = nobel['birth_country']=='USA'
nobel['decade'] = (np.floor(nobel['awardYear'] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()


# Display the proportions of USA born winners per decade
print(prop_usa_winners)

# Setting the plotting theme
sns.set()
# and setting the size of all plots.
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners 
ax = sns.lineplot(x='decade', y='usa_born_winner', data=prop_usa_winners)

# Adding %-formatting to the y-axis
ax.yaxis.set_major_formatter(PercentFormatter(1.0))

# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel['gender']=='female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()

# Plotting USA born winners with % winners on the y-axis
ax = sns.lineplot(x='decade', y='female_winner', hue='category', data=prop_female_winners)
ax.yaxis.set_major_formatter(PercentFormatter(1.0))

# Picking out the first woman to win a Nobel Prize
female=nobel[nobel.gender=='female']
print(female.nsmallest(1,'awardYear'))

# Selecting the laureates that have received 2 or more prizes.
name=nobel.groupby('fullName').filter(lambda group: len(group) >= 2)
print(name)

















