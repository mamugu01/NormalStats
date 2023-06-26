NBA Stat Normal Distribution Test

This code runs two sets of tests, for a given NBA stat in order to see if the stat is 
Normally distributed for the 2023 NBA season. Both a Goodness of Fit Test and the Shapiro-Wilk
tests are run to see if the results are consistent and they are also ran against a data sampled from a 
Normal distribution to make sure they are correct. 

To run, run the main.py file and you will be prompted to enter your wanted Stat. Note, that all the 
data is scraped from Basketball Reference stats per game and therefore the name must be consistent with the stat 
names in the table, otherwise an error will occur.

The main inspiration behind this project was that I wondered if there was a better way to quantify good and bad 
field goal percentage for players in the NBA since current standards are somewhat vague(below 40% is bad and around 
45% is excellent). I thought maybe good and bad could be quantified in terms of being 1 standard deviation above
and below the mean, but then I realized I was just assuming the data was normally distributed. The code is meant 
to show that the initial assumption was incorrect and that more work needs to be done on my end to come up with 
a better metric.

Partially adapted from https://analyticsindiamag.com/goodness-of-fit-python-guide/
