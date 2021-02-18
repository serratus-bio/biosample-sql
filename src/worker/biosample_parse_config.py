biosample_id_colname_map = {'BioSample': 'biosample_id', 'SRA': 'sra_id'}

# XML: <Attribute harmonized_name="geo_loc_name"
biosample_attribute_keys = ['harmonized_name', 'attribute_name']

potential_geo_coord_keywords = {'latitude', 'longitude', '_lat', '_lon', 'lat_', 'lon_'}
potential_geo_text_keywords = {'location', 'geogra', 'geoloc', 'geo_loc'}
collection_date_attr = "collection_date"

# lat_lon_pattern = '^(-?\d+(\.\d+)?)\s*(\w)*\s*(-?\d+(\.\d+)?)\s*(\w)*$'
