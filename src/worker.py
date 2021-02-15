import pandas as pd
from lxml import etree


MAX_ITEMS_PER_WORKER = 1000
xml_file = 'data/head.xml'

def handler(event, context):
    start_byte = event['start_byte']
    end_byte = event['end_byte']
    with open(xml_file, 'rb') as f:
        f.seek(start_byte, 0)
        items = etree.iterparse(f, events=("end", "start"))
        items = filter(lambda x: x[0] == "start", items)
        items = filter(lambda x: x[1].tag in {"BioSample", "Attribute", "Id"}, items)
        # items = itertools.islice(items, 10000)
        df = get_df_from_items(items)
    # df.dropna(subset=['lat_lon', 'geo_loc_name'], thresh=1).to_csv('test.tsv', sep='\t', index=False)
    return df


def get_df_from_items(items):
    collect = False
    elements = []
    dicts = []
    for _, element in items:
        if element.tag == 'BioSample':
            biosample = BioSample(elements)
            dicts.append(biosample.get_columns(['BioSample', 'SRA', 'lat_lon', 'geo_loc_name']))
            if len(dicts) == MAX_ITEMS_PER_WORKER:
                break
            elements = []
        elements.append(element)
    return pd.DataFrame(dicts)
