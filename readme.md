# Transparency

### Requirements

- Python 3.6 and above
- Scrapy 2.0.0

### Steps to run on local

- clone the repository
- install scrapy
- cd into the clone folder
- to get data for all companies
   - run `python3 -m scrapy crawl AllSignatories -o all_signatories.csv`
- to get data for selected companies
   - first enter company names in companies.txt file
   - make sure each company name is on its own line
   - make sure company names exactly matches with the company name provided on the website
   - run `python3 -m scrapy crawl signatories -o selected_signatories.csv`
- check the corresponding csv file for data
- to fetch data again, either delete the csv file or delete all data in it, else it appends the fresh data to current data
