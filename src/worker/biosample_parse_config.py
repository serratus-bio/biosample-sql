biosample_id_colname_map = {'BioSample': 'biosample_id', 'SRA': 'sra_id'}

# XML: <Attribute harmonized_name="geo_loc_name"
biosample_attribute_keys = ['harmonized_name', 'attribute_name']

collection_date_attr = "collection_date"

geo_coord_inclusion_keywords = {
    'latitude',
    'longit',
    '_lat',
    '_lon',
    'lat_',
    'lon_',
    'coordinates',
}
geo_coord_exclusion_keywords = {
    'colon',
    'latino',
    'later',
    'how_long',
}

geo_text_inclusion_keywords = {
    'country',
    'county',
    'geo_',
    'geo:',
    'geogra',
    'geoloc',
    'localization',
    'location',
    'region',
    'province',
    'sample_area',
}
geo_text_exclusion_keywords = {
    'anatomical',
    'aneurysm',
    'barcode',
    'biopsy',
    'body',
    'colon',
    'disease',
    'plate',
    'stake',
    'tissue',
    'tonotopic',
    'transect',
    'translocation',
    'tumor',
    'tumour',
    'ulcer',
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
