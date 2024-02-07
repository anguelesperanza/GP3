import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 500)


file = 'troop_movements.csv'

starwars = pd.read_csv(file)

eor = starwars.groupby(['empire_or_resistance']).size().reset_index(name='count')
print(eor)

print("========================")

homeworld = starwars.groupby(['homeworld']).size().reset_index(name='count')
print(homeworld)

print("========================")

unit_type = starwars.groupby(['unit_type']).size().reset_index(name='count')
print(unit_type)

print("========================")

starwars_copy = starwars.copy()



def is_resistance(value):
    if value == 'resistance':
        return 'True'
    else:
        return 'False'

    
starwars_copy['is_resistance'] = starwars_copy['empire_or_resistance'].map(is_resistance)


print(starwars_copy)

