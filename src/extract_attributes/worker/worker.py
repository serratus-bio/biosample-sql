import io
import pandas as pd
from lxml import etree
from biosample import BioSample
from download import get_contents
from upload import upload


def handler(event, context):
    process(event['start_byte'], event['end_byte'])


def process(start_byte, end_byte):
    """read [start_byte, end_byte)"""
    contents = get_contents(start_byte, end_byte - 1).read()
    contents = f'<xml>{contents}</xml>'.encode()
    f = io.BytesIO(contents)

    items = etree.iterparse(f, events=("end", ))
    items = filter(lambda x: x[1].tag in {"BioSample", "Attribute", "Id"}, items)
    df = get_df_from_items(items)
    upload(df)
    return df


def get_df_from_items(items):
    elements = []
    dicts = []
    for _, element in items:
        if element.tag == 'BioSample':
            biosample = BioSample(elements)
            elements = []
            biosample_columns = biosample.get_columns()
            if 'biosample_id' not in biosample_columns:
                print(f'empty BioSample entry: {biosample}')
                continue
            dicts.append(biosample_columns)
        elements.append(element)
    df = pd.DataFrame(dicts)
    return df
