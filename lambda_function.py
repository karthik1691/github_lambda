import pandas as pd

def lambda_handler(event, context):
    d = {'col1' : [1,2], 'col2' : [3,4], 'col3' : [5,6], 'col4' : [7,8]}
    df = pd.DataFrame{data=d}
    print(df)
    print('done xl')
   

