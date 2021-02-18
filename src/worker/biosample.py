from biosample_parse_config import (
    biosample_id_colname_map,
    biosample_attribute_keys,
    potential_geo_coord_keywords,
    potential_geo_text_keywords,
    collection_date_attr
)
from biosample_parse_functions import get_extracted_cols

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
            'geo_coord': dict(),
            'geo_text': dict()
        }
        for k, v in self.attrs.items():
            if k == collection_date_attr:
                d['collection_date'] = v
            elif any(keyword in k.lower() for keyword in potential_geo_coord_keywords):
                d['geo_coord'][k] = v
            elif any(keyword in k.lower() for keyword in potential_geo_text_keywords):
                d['geo_text'][k] = v
        return d

    def __repr__(self):
        return f'BioSample({self.ids})'
