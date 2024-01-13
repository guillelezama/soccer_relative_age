# Soccer Relative Age Analysis Project
## Overview
This project investigates the existence of the Relative Age Effect, a known bias in the selection process of youth athletes, within Uruguayan soccer. The analysis spans both male and female players in Youth and Professional teams from 2013 to 2022.

## Data Sources
The data was obtained from the following sources:

1) Uruguayan Football Association (AUF): Data for players in Youth (U14 to U19) and Professional teams. Website
2) Health Authority in Uruguay (MSP): Births data for comparative analysis. Website
3) Transfermarkt: Additional dataset for male players born in specific years. Website

## Files Description
* analysis.ipynb: Main analysis notebook. Implements logit and hazard models to evaluate the impact of birth month on player dropout rates.
* scrap_auf.ipynb: Python script to scrape data from the AUF's website using Beautiful Soup and Selenium libraries.
* scrap_transfermarkt.ipynb: Python script to scrape data from Transfermarkt. Focuses on male players born in specific years.
* process_nac.ipynb: Processes birth data from the MSP for distribution analysis.
* extra_cleaning.py: Python script for cleaning datasets for use in analysis.ipynb.

# Contact
For inquiries, please contact: guillelezama [at] pitt [dot] edu
