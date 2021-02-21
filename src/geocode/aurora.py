import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy_aurora_data_api import register_dialects

register_dialects()

cluster_arn = 'arn:aws:rds:us-east-1:797308887321:cluster:serratus-aurora'
secret_arn = 'arn:aws:secretsmanager:us-east-1:797308887321:secret:rds-db-credentials/cluster-KOFPN4Q2TKDBO5FHY6QO5M3S7Q/serratus-agdBn9'
geocode_table = 'biosample_geocode'
engine = create_engine('postgresql+auroradataapi://:@/summary',
            connect_args=dict(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn))

dtype = {
    'attributes': sqlalchemy.dialects.postgresql.JSONB,
    'geo_coord_all': sqlalchemy.dialects.postgresql.JSONB,
    'geo_text_all': sqlalchemy.dialects.postgresql.JSONB
}

def download(query):
    with engine.connect() as con:
        df = pd.read_sql(query, con)
    return df

def upload(df):
    with engine.connect() as con:
        df.to_sql(geocode_table, con,
            if_exists='append',
            index=False,
            chunksize=1000)
