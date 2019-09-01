#! usr/bin/env python


# TODO: Write docstrings
# TODO: 

# -------------------------------------
# Library Imports
# -------------------------------------

import pandas as pd
import datetime


# -------------------------------------
# Function Definitions
# -------------------------------------


def date_fix(x: str, start: int) -> datetime.datetime:
    """
    
    :param x:
    """
    date = int(x.split('/')[0])
    time = x.split('/')[1][0:4]
    if date >= 15:
        date = datetime.datetime(2019, start, date, int(time[0:2]), int(time[2:4]))
    else:
        date = datetime.datetime(2019, start + 1, date, int(time[0:2]), int(time[2:4]))
    return date


def advisory_input(file: str, start: int) -> pd.DataFrame:
    """
    
    """
    widths = [6, 9, 7, 7, 7,7]
    col_names = ['FORECAST',
                 'DATETIME',
                 'LAT',
                 'LON',
                 'SPEED (KTS)',
                 'SPEED (MPH)']

    adv_file = pd.read_fwf(file, widths=widths, header=None, names=col_names)
    
    adv_file['DATETIME'] = adv_file['DATETIME'].apply(lambda x: date_fix(x, start=start))
    adv_file['LAT'] = adv_file['LAT'].apply(lambda x: float(x[0:4]))
    adv_file['LON'] = adv_file['LON'].apply(lambda x: float(x[0:4])*-1)
    adv_file['SPEED (KTS)'] = adv_file['SPEED (KTS)'].apply(lambda x: x.split()[0])
    adv_file['SPEED (MPH)'] = adv_file['SPEED (MPH)'].apply(lambda x: x.split()[0])
    
    return adv_file
    
