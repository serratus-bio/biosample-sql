class BioSample():

    def __init__(self, elements):
        """elements : from etree.iterparse"""
        self.elements = elements
        self.ids = dict()
        self.attrs = dict()
        self.parse_elements()
        self.extracted_attrs = dict()
        self.parse_location()

    def parse_elements(self):
        for element in self.elements:
            if element.tag == 'Id' and 'db' in element.attrib:
                self.ids[element.attrib['db']] = normalize_text(element.text)
            elif element.tag == 'Attribute' and 'harmonized_name' in element.attrib:
                self.attrs[element.attrib['harmonized_name']] = normalize_text(element.text)

    def parse_location(self):
        self.extracted_attrs['location'] = None
        if 'lat_lon' in self.attrs and self.attrs['lat_lon']:
            self.extracted_attrs['location'] = self.attrs['lat_lon']
        elif 'geo_loc_name' in self.attrs and self.attrs['geo_loc_name']:
            self.extracted_attrs['location'] = self.attrs['geo_loc_name']
            # TODO: convert to coordinates

    def as_dict(self):
        return {**self.ids, **self.attrs, **self.extracted_attrs}

    def get_columns(self, columns):
        d = self.as_dict()
        return {x: d[x] for x in columns if x in d}

    def __repr__(self):
        return f'BioSample({self.ids})'


nan_values = {'not determined', 'Missing', 'missing'}

def normalize_text(element_text):
    if element_text in nan_values:
        return None
    return element_text
