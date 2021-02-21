from biosample_parse_config import (
    biosample_id_colname_map,
    biosample_attribute_keys,
    collection_date_attr
)
from biosample_parse_functions import (
    get_extracted_cols,
    clean_text,
    include_coord_key,
    include_text_key
)

class BioSample():

    def __init__(self, elements):
        """elements : from etree.iterparse"""
        self.elements = elements
        self.ids = dict()
        self.attrs = dict()
        self.parse_elements()

    def parse_elements(self):
        for element in self.elements:
            if element.tag == 'Id' and 'db' in element.attrib:
                self.ids[element.attrib['db']] = element.text
            elif element.tag == 'Attribute':
                for key in biosample_attribute_keys:
                    if key in element.attrib:
                        self.attrs[element.attrib[key]] = element.text
                        break

    def get_columns(self):
        d = self.get_id_columns()
        raw_attrs = self.get_raw_attrs()
        d.update(raw_attrs)
        d.update(get_extracted_cols(raw_attrs))
        return d

    def get_id_columns(self):
        return {colname: self.ids[id_key]
                for id_key, colname in biosample_id_colname_map.items()
                if id_key in self.ids}

    def get_raw_attrs(self):
        d = {
            'attributes': self.attrs,
            'geo_coord_all': dict(),
            'geo_text_all': dict()
        }
        for k, v in self.attrs.items():
            if k == collection_date_attr:
                d['collection_date'] = clean_text(v)
            elif include_coord_key(k):
                d['geo_coord_all'][k] = v
            elif include_text_key(k):
                d['geo_text_all'][k] = v
        return d

    def __repr__(self):
        return f'BioSample({self.ids})'
