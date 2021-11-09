import pandas as pd

from src.db_functions import create_sql_alchemy_db_engine

engine = create_sql_alchemy_db_engine()

DATA_SOURCES = [
    'customers', 'geolocation', 'order_items', 'order_payments',
    'orders', 'products', 'sellers'
]

PARSE_DATES_COLS = {
    'order_items': ['shipping_limit_date'],
    'orders': [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_estimated_delivery_date'
    ]
}

if __name__ == "__main__":
    for source in DATA_SOURCES:
        df = pd.read_csv(
            f"./data/raw/olist_{source}_dataset.csv",
            parse_dates=PARSE_DATES_COLS.get(source)
        )
        df.to_sql(source, engine, if_exists='replace', index=False)
