# soccer_relative_age
This is a project where I intended to analyze whether the Relative Age Effect, a bias that exists in the selection process for youth athletes, exists also in Uruguayan soccer. To do that, I scraped data from the Uruguayan Football Association (auf.org.uy) to get a dataset of all the players that participated in Youth teams and Professional teams in the period 2013-2022 for both Men and Women's teams. Youth teams go from Under 14 to Under 19.
* analysis.ipynb performs the main analysis. I estimate a logit model and hazard models to assess whether the birth month affects the probability of dropping out.
* scrap_auf.ipynb gets data from the AUF's website using Python. I use Beautiful Soup and Selenium's libraries.
* scrap_transfermakt.ipynb gets data from transfermarkt.es website using Python. I use Beautiful Soup and Selenium's libraries. This dataset gives a good benchmark since it contains all male players born in a specific year (it does not matter where are they playing).
* process_nac.ipynb process births data. This data comes from the Health Authority in Uruguay (MSP) (https://uins.msp.gub.uy/). I process it to show how the distribution looks like for all men and women born at the same time that soccer players.
* extra_cleaning.py is a Python script that cleans each of the datasets to be processed in analysis.ipynb.

For any question you can contact me at guillelezama [at] pitt [dot] edu
