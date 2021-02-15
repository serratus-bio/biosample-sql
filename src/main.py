import itertools
import gzip
import pandas as pd
from lxml import etree
from biosample import BioSample


def get_df_from_items(items):
    collect = False
    elements = []
    biosamples = []
    dicts = []
    for _, element in items:
        if element.tag == 'BioSample':
            if not elements:
                collect = True
            else:
                biosample = BioSample(elements)
                dicts.append(biosample.get_columns(['BioSample', 'SRA', 'lat_lon', 'geo_loc_name']))
                elements = []
        if collect:
            elements.append(element)
    return pd.DataFrame(dicts)


if __name__ == '__main__':
    handle = gzip.open("../data/biosample_set.xml.gz", "r")
    items = etree.iterparse(handle, events=("end", "start"))
    items = filter(lambda x: x[0] == "start", items)
    items = filter(lambda x: x[1].tag in {"BioSample", "Attribute", "Id"}, items)
    items = itertools.islice(items, 10000)
    df = get_df_from_items(items)
    df.dropna(subset=['lat_lon', 'geo_loc_name'], thresh=1).to_csv('test.tsv', sep='\t', index=False)
