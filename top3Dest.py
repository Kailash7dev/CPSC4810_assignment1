#!/usr/bin/env python3




import numpy as np
import pandas as pd


flight_df = pd.read_csv(r"2007.csv")

top3dest = flight_df.groupby('Dest').count().reset_index().sort_values(by="Year", ascending=False).loc[:,('Dest','Year')].head(3)

top3dest.columns=['Dest','Count']

top3dest.to_csv('top3dest.csv', index=False)
print('kailash')





