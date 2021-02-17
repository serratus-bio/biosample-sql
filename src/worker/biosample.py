from biosample_parse_config import (
    biosample_attribute_keys,
    potential_geo_coord_keywords,
    potential_geo_text_keywords,
    collection_date_attr
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

    def as_dict(self):
        return {**self.ids, **self.attrs}

    def get_columns(self):
        d = self.get_ids()
        d.update(self.get_attrs())
        return d

    def get_ids(self, id_columns=('BioSample', 'SRA')):
        d = self.ids
        return {x: d[x] for x in id_columns if x in d}

    def get_attrs(self):
        d = {
            'geo_coord': dict(),
            'geo_text': dict()
        }
        for k, v in self.attrs.items():
            if k == collection_date_attr:
                d['collection_date'] = v
            elif any(keyword in k for keyword in potential_geo_coord_keywords):
                d['geo_coord'][k] = v
            elif any(keyword in k for keyword in potential_geo_text_keywords):
                d['geo_text'][k] = v
        return d

    def __repr__(self):
        return f'BioSample({self.ids})'


def normalize_text(element_text):
    if element_text in nan_values:
        return None
    return element_text
