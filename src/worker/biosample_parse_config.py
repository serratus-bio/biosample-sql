biosample_id_colname_map = {'BioSample': 'biosample_id', 'SRA': 'sra_id'}

# XML: <Attribute harmonized_name="geo_loc_name"
biosample_attribute_keys = ['harmonized_name', 'attribute_name']

potential_geo_coord_keywords = {'latitude', 'longitude', '_lat', '_lon', 'lat_', 'lon_'}
potential_geo_text_keywords = {'location', 'geogra', 'geoloc', 'geo_loc'}
collection_date_attr = "collection_date"

geo_coord_exclusion_keywords = {
    'colon',
    'latino',
    'later',
    'how_long',
}

geo_text_exclusion_keywords = {
    'anatomical',
    'aneurysm',
    'barcode',
    'biopsy',
    'body',
    'colon',
    'disease',
    'gi',
    'plate',
    'stake',
    'tissue',
    'tonotopic',
    'transect',
    'translocation',
    'tumor',
    'tumour',
    'well',
}

# in order of removal
null_text_values = [
    'null',
    'missing geographic information',
    'missing',
    'lab culture', # "usa: lab culture with samples originating from freiburg, germany"
    'lab strain',
    'n/a',
    'n.a.',
    'none',
    'not available',
    'not applicable',
    'not collected',
    'not determined',
    'not provided',
    'not stated',
    'restricted access',
    'unknown',
]

# these should be exact match (don't remove substring)
exact_null_text_values = [
    'na',
    'lab',
]

# lat_lon_pattern = '^(-?\d+(\.\d+)?)\s*(\w)*\s*(-?\d+(\.\d+)?)\s*(\w)*$'
