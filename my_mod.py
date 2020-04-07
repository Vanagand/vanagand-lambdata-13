import pandas as pd

def enlarge(n):

# Param n is a number
# Function will enlarge the number
    return n * 100

# Function to split a date column into multiple columns
def datesplit(df, column):
    
    df = df.copy()

    # Convert input column to datetime format
    df[column] = pd.to_datetime(df[column], infer_datetime_format=True)

    # Split input column into day, month, and year columns
    df['day'] = df[column].dt.day
    df['month'] = df[column].dt.month
    df['year'] = df[column].dt.year

    return(df)

# Function to split a dataframe into a train, validation, and training set
def modeltrisplit(df, target, trainsize=0.4, validationsize=0.4, testsize=0.2):
    
    df = df.copy()
    train = []
    val = []
    test = []
    
    return(train, val, test)
    
# Only invoked if used from command line
# if __name__ == '__main__':