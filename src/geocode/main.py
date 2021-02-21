from aurora import download, upload
from convert import get_coords

table_name = 'biosample5'
query = f'''
    select distinct geo_text_extracted
    from {table_name}
    where geo_text_extracted is not null
'''

df = download(query)
df['coordinate_x'], df['coordinate_y'] = zip(*df['geo_text_extracted'].map(get_coords))
upload(df)


# pickle

# df.to_pickle('geo_text_extracted_geocoded.pickle')
# import pickle
# import pandas as pd
# df = pd.read_pickle('geo_text_extracted_geocoded.pickle')
