import re


LAT_LON_PATTERN = r'(-?[\d\.]+)\s*([NS])*\s*(-?[\d\.]+)\s*([EW])*$'


def try_get_coords(geo_coord_dict):
    """Return (x,y) from dictionary of biosample attributes.
    Return (None,None) if extraction not possible.
    """
    if len(geo_coord_dict) == 0:
        return (None, None)

    # 1: extract from lat_lon
    if 'lat_lon' in geo_coord_dict:
        return get_lat_lon(geo_coord_dict['lat_lon'])

    # 2: extract from pair of keys for lat/lon
    # TODO: get unit keys
    lat_key, lon_key = '', ''
    for key in geo_coord_dict:
        if 'lat' in key.lower():
            lat_key = key
        elif 'lon' in key.lower():
            lon_key = key
    if lat_key and lon_key:
        return get_lat_lon(f'{geo_coord_dict[lat_key]} {geo_coord_dict[lon_key]}')

    # 3: no extraction possible
    return (None, None)


def get_lat_lon(text):
    """Return (x,y) from coordinate text.
    Return (None,None) if regex pattern not matched.
    """
    result = re.search(LAT_LON_PATTERN, text)
    if not result:
        return (None, None)
    y_num, y_dir, x_num, x_dir = result.groups()

    if y_dir == 'S' and y_num[0] != '-':
        y_num = f'-{y_num}'
    if x_dir == 'W' and x_num[0] != '-':
        x_num = f'-{x_num}'

    try:
        x_num, y_num = float(x_num), float(y_num)
    except ValueError:
        return (None, None)

    if (-180 <= x_num <= 180) and (-90 <= y_num <= 90):
        return (x_num, y_num)
    return (None, None)
