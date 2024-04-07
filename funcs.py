### Categorizing time of day function
# Source: https://stackoverflow.com/questions/63071619/how-to-categorize-timestamp-into-evening-in-pandas-dataframe

def ftod(x):
    if (x>=0) & (x<6):
        tod = 'night'
    elif (x>=6) & (x<12):
        tod = 'morning'
    elif (x>=12) & (x<18):
        tod = 'afternoon'
    else:
        tod = 'evening'
    return tod

