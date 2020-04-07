def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100

# Function to split a date column into multiple columns
def datesplit(df, column):
    
    df = df.copy()

    # convert input column to datetime format
    df[column] = pandas.to_datetime(df[column], infer_datetime_format=True)

    # split input column into day, month, and year columns
    df['day'] = df[column].dt.day
    df['month'] = df[column].dt.month
    df['year'] = df[column].dt.year

    return(df)

# Function to split a dataframe into a train, validation, and training set
def modeltrisplit(df, target):
    
    df = df.copy()
    
# only invoked if used from command line
if __name__ == '__main__':