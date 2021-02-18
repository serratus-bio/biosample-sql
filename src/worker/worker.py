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
            dicts.append(biosample.get_columns())
            elements = []
        elements.append(element)
    df = pd.DataFrame(dicts)
    return df
