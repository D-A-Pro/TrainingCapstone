import pandas as pd
from sqlalchemy import create_engine
import pymysql
from decouple import config


host = config('HOST')
user = config('USER')
password = config('PASSWORD')
database = config('DATABASE')

connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=database
)

conn_string = f'mysql+pymysql://{user}:{password}@{host}/{database}'
engine = create_engine(conn_string)

file_path = """C:/Users/safmuk01/OneDrive - Robert Half/Desktop/Work/Clients/Arden/Prep/AutoML technical/data/online_shoppers_intention_historical.csv"""

df = pd.read_csv(file_path)

df.to_sql('onlineshoppersintention', engine, if_exists='replace', index=False)
