import pandas as pd
import numpy as np
import sys

for line in sys.stdin:
    # add index (fl_date, airline_id, fl_num)
    data['edgeID'] = np.nan
    for index, row in data.iterrows():
            thisDate = str(row[0]).strip().replace('-','')
            thisAirlineID = str(row[1])
            thisFlightNum = str(row[2])

            thisIndex =  int(thisDate + thisAirlineID + thisFlightNum)
            row['edgeID'] = thisIndex
            print row
