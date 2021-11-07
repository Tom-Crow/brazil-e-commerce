import pandas as pd

from brazil_e_commerce.db_functions import create_sql_alchemy_db_engine

engine = create_sql_alchemy_db_engine()

data_sources = [
    'customers', 'geolocation', 'order_items', 'order_payments',
    'orders', 'products', 'sellers'
]

if __name__ == "__main__":
    for source in data_sources:
        df = pd.read_csv(f"./data/olist_{source}_dataset.csv")
        df.to_sql(source, engine, if_exists='replace', index=False)
