#!/usr/bin/env python3
# coding: utf-8

import numpy as np
import pandas as pd


flight_df = pd.read_csv(r"2007.csv")

first3sfo = flight_df[flight_df["Origin"]=="SFO"].loc[:,('ArrDelay', 'Origin')].head(3)


first3sfo.to_csv(r'first3sfo.csv', index=False)







