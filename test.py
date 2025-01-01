import pandas as pd

player_name = []

more_details = 'john,0,0'
ef = pd.read_csv('player_detail.csv')
ef = pd.to_numeric(ef, errors='coerce')

print(ef)
