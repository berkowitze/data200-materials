import pandas as pd
import requests

resp = requests.get('https://en.wikipedia.org/wiki/Gun_violence_in_the_United_States_by_state')

# decode because we need to convert what the web sends (0s and 1s) to text (abcs)
pd.read_html(resp.content.decode())
tables = pd.read_html(resp.content.decode())

# https://stackoverflow.com/questions/31328861
table = tables[1]
table.columns = table.iloc[0]
table = table[1:]

print(table.head())
