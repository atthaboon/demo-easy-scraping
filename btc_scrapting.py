from cryptocmd import CmcScraper
import pandas

# initialise scraper with time interval
scraper = CmcScraper("BTC", "01-01-2021", "01-06-2021")

# get raw data as list of list
headers, data = scraper.get_data()

# get data in a json format
json_data = scraper.get_data("json")

# export the data to csv
scraper.export("csv")

# get dataframe for the data
df = scraper.get_dataframe()

with pandas.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)