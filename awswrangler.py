import awswrangler as wr
import pandas as pd
import os
import urllib.parse

# Extracting from environment variables
path = 's3://cleaned-ver-for-yt-dataset/' 
tablename = os.getenv('TABLE_NAME', 'table01')
dbname = os.getenv('DB_NAME', 'db01')
writedataoperation = os.getenv('WRITE_OPERATION', 'append')

def lambda_handler(event, context):
    # Getting bucket name and object key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        # Creating dataframe from the object/content in the bucket
        df = wr.s3.read_json(f's3://{bucket}/{key}')

        # Extract column and normalize
        df = pd.json_normalize(df['items'])

        # Write to S3 in Parquet format
        wr_response = wr.s3.to_parquet(
            df=df,                   # Dataframe to write
            path=path,               # Path for new bucket which will store cleansed data
            dataset=True,            # Whether to create a dataset
            database=dbname,         # Database name for the Wrangler to create tables in
            table=tablename,         # New table name (for catalog or schema) to be created
            mode=writedataoperation  # Append or write over
        )

        return {
            'statusCode': 200,
            'body': wr_response
        }
    except Exception as e:
        print(str(e))
        print(f'Error getting {key} object from {bucket} bucket. Make sure they exist and the bucket is in the same region as this function.')
        raise e
