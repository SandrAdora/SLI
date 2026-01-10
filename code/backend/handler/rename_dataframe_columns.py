# This program renames the names of the headers of a pandas dataframe 

# convert int digits to string 
def convert_intDigits_to_string(digit: int) -> str:
    """This method convers an integer to a sting of that integer
    Args:
        digit (int): A digit
    Return: 
        digit_str (str): A string of the digit number"""
    return str(digit)
        

# rename header of a dataframe 
def rename_header(df, header_name:str = "pixel"):
    """This Method renames the header names of a specific dataframe.
    Default header name is *pixel* the names will be a combination of the 
    header_name + digit nr.
    
    Args:
        df (pandas): Data of type pandas 
        header_name (str): Header name for columns. 
    Return:
        df (pandas): Data with renamed header"""
    
    # make sure the df is not empty
    if df.columns is None:
        print("Error: Dataframe is empty")
        exit
    # change header name to lower case 
    header_name=header_name.lower()
    # get the amount of the columns 
    columns_digit=len(df.columns) # df.shape[1]
    if columns_digit :
        print(f"Success: The numbers of available columns were  passed {columns_digit}")
    
    # rename the first column to label 
    df=df.rename(columns={df.columns[0]: "label"})
    
    # iterate and rename subsequent columns
    for i in range(1,columns_digit):
        df=df.rename(columns={df.columns[i]: f"{header_name}_{convert_intDigits_to_string(i)}"})
    
    # return df
    return df
        
    
    
    
        