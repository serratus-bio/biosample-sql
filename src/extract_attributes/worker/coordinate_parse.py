import re


def try_get_coords(geo_coord_dict):
    if len(geo_coord_dict) == 0:
        return (None, None)

    # order of precedence

    if 'lat_lon' in geo_coord_dict:
        return get_lat_lon(geo_coord_dict['lat_lon'])

    lat_key, lon_key = '', ''
    for key in geo_coord_dict:
        if 'lat' in key:
            lat_key = key
        elif 'lon' in key:
            lon_key = key

    if lat_key and lon_key:
        return get_lat_lon(f'{geo_coord_dict[lat_key]} {geo_coord_dict[lon_key]}')

    return (None, None)


def get_lat_lon(text):
    if not has_digit(text):
        return (None, None)
    lat_lon_pattern = r'(-?[\d\.]+)\s*(\w)*\s*(-?[\d\.]+)\s*(\w)*$'
    result = re.search(lat_lon_pattern, text)
    if not result:
        return (None, None)
    y_num, y_dir, x_num, x_dir = result.groups()
    if y_dir == 'S':
        y_num = f'-{y_num}'
    if x_dir == 'W':
        x_num = f'-{x_num}'
    return x_num, y_num


def has_digit(s):
    return bool(re.search(r'\d+', s))


# unused generic stuff

directions = {'N', 'E', 'S', 'W'}

def is_single_column(text):
    multiple_directions = sum(c in text for c in directions) == 2
    multiple_decimals = text.count('.') == 2
    return multiple_directions | multiple_decimals

# longitude, E/W
def get_x(text):
    if 'E' in text:
        return text
    if 'W' in text:
        return f'-{text}'