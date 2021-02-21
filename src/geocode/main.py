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

# pickled

# df.to_pickle('geo_text_extracted_distinct.pickle')
# import pickle
# import pandas as pd
# df = pd.read_pickle('geo_text_extracted_distinct.pickle')
# df_head = df[:100].copy()
# for geo_text in df_head.geo_text_extracted:
#     print(get_coords(geo_text))
