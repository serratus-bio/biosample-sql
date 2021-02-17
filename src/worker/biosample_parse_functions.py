import re

def get_extracted_cols(raw_attrs):
    d = {
        'geo_coord_extracted': None, # TODO: split into x/y
        'geo_text_extracted': None
    }
    if len(raw_attrs['geo_coord']) != 0:
        d['geo_coord_extracted'] = try_get_coords(raw_attrs['geo_coord'])
    if not d['geo_coord_extracted'] and len(raw_attrs['geo_text']) != 0:
        d['geo_text_extracted'] = try_get_text(raw_attrs['geo_text'])
    return d


def try_get_coords(geo_coord_dict):
    # get arbitrary first value with digit
    for k, v in geo_coord_dict.items():
        if has_digit(v):
            return v


def try_get_text(geo_text_dict):
    return list(geo_text_dict.values())[0] # naive, get arbitrary first value


def has_digit(s):
    return bool(re.search(r'\d+', s))
