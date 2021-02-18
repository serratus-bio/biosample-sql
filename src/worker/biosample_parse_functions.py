import re
from biosample_parse_config import (
    null_text_values,
    exact_null_text_values
)

def get_extracted_cols(raw_attrs):
    d = {
        'geo_coord_extracted': None, # TODO: split into x/y
        'geo_text_extracted': None
    }
    d['geo_coord_extracted'] = try_get_coords(raw_attrs['geo_coord_all'])
    if not d['geo_coord_extracted']:
        d['geo_text_extracted'] = try_get_text(raw_attrs['geo_text_all'])
    return d


def try_get_coords(geo_coord_dict):
    if len(geo_coord_dict) == 0:
        return None
    # get arbitrary first value with digit
    for k, v in geo_coord_dict.items():
        if has_digit(v):
            return v


def try_get_text(geo_text_dict):
    if len(geo_text_dict) == 0:
        return None
    # naive, get arbitrary first value
    for k, v in geo_text_dict.items():
        text = clean_text(v)
        if text:
            return text


def clean_text(text):
    text = text.lower()
    text = text.replace('"', '')
    text = remove_null_values(text)
    text = text.strip()
    if text == '':
        return None
    return text


def remove_null_values(text):
    for useless_value in null_text_values:
        text = text.replace(useless_value, '')
    for useless_value in exact_null_text_values:
        if text == useless_value:
            text = ''
    return text


def has_digit(s):
    return bool(re.search(r'\d+', s))
