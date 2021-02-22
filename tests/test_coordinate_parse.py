from coordinate_parse import (
    get_lat_lon,
    try_get_coords,
    is_single_column,
)

def test_is_single_column():
    assert True == is_single_column('20.237556 N 84.270018 E')
    assert True == is_single_column('22.768333 N 157.89 W')

def test_get_lat_lon():
    assert ('84.270018', '20.237556') == get_lat_lon('20.237556 N 84.270018 E')
    assert ('-157.89', '22.768333') == get_lat_lon('22.768333 N 157.89 W')
    assert ('-179.983333', '-0.033333') == get_lat_lon('0.033333 S 179.983333 W')
    assert ('18.2225', '-0.0067') == get_lat_lon('0.0067 S 18.2225 E')

def test_try_get_coords():
    assert ('84.270018', '20.237556') == try_get_coords({
        'lat_lon': '20.237556 N 84.270018 E'})
    assert ('84.270018', '20.237556') == try_get_coords({
        'latitude': '20.237556 N',
        'longitude': ' 84.270018 E'})
    assert ('84.270018', '20.237556') == try_get_coords({
        'geographic location (latitude)': '20.237556 N',
        'geographic location (longitude)': ' 84.270018 E'})
