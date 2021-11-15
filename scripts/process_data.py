import pandas as pd

from src.db_functions import create_sql_alchemy_db_engine
from src.helpers import remove_accents

PROCESSED_FOLDER = "./data/processed"


def process_orders_and_sellers(conn):
    orders = pd.read_sql("SELECT * FROM orders", conn)
    customers = (
        pd.read_sql("SELECT * FROM customers", conn)
        .rename({
            'customer_zip_code_prefix': 'zip_code_prefix',
            'customer_city': 'city',
            'customer_state': 'state'
        }, axis=1)
        .assign(city=lambda df: df.city.apply(remove_accents))
    )
    sellers = (
        pd.read_sql("SELECT * FROM sellers", conn)
        .rename({
            'seller_zip_code_prefix': 'zip_code_prefix',
            'seller_city': 'city',
            'seller_state': 'state'
        }, axis=1)
        .assign(city=lambda df: df.city.apply(remove_accents))
    )
    geoloc = (
        pd.read_sql("SELECT * FROM geolocation", conn)
        .rename({
            'geolocation_zip_code_prefix': 'zip_code_prefix',
            'geolocation_city': 'city',
            'geolocation_state': 'state',
            'geolocation_lat': 'lat',
            'geolocation_lng': 'lon'
        }, axis=1)
        .assign(city=lambda df: df.city.apply(remove_accents))
    )

    # Take the average lat-lon by zipcode, city and state
    zipcode_average_latlon = (
        geoloc
            .groupby(['zip_code_prefix', 'city', 'state'])
        [['lat', 'lon']]
            .mean()
            .reset_index()
    )

    customers_with_location = customers.merge(zipcode_average_latlon)
    sellers_with_location = sellers.merge(zipcode_average_latlon)
    orders_with_customer_info = orders.merge(customers_with_location)

    sellers_with_location.to_parquet(f"{PROCESSED_FOLDER}/sellers_with_location.parquet")
    orders_with_customer_info.to_parquet(f"{PROCESSED_FOLDER}/orders_with_cust_info.parquet")


if __name__ == "__main__":
    connection = create_sql_alchemy_db_engine()
    process_orders_and_sellers(connection)
