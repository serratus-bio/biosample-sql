import io
import pandas as pd
from lxml import etree
from biosample import BioSample
from download import get_contents


MAX_ITEMS_PER_WORKER = 1000


def handler(event, context):
    process(event['start_byte'], event['end_byte'])


def process(start_byte, end_byte):
    contents = get_contents(start_byte, end_byte).read()
    contents = f'<xml>{contents}</xml>'.encode()
    f = io.BytesIO(contents)

    items = etree.iterparse(f, events=("end", ))
    items = filter(lambda x: x[1].tag in {"BioSample", "Attribute", "Id"}, items)
    df = get_df_from_items(items)
    return df


def get_df_from_items(items):
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

# process(54, 1692820)
# process(1692820, 3558646)
