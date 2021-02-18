from biosample_parse_functions import (
    clean_text,
    remove_null_values,
    include_coord_key,
    include_text_key
)

def test_remove_null_values():
    assert remove_null_values('not available: not collected') == ': '

def test_clean_text():
    assert clean_text('not available: not collected') == ':'
    assert clean_text('"foo"') == 'foo'
    assert clean_text('naples') == 'naples'
    assert clean_text('na') == None

def test_include_coord_key():
    # False
    assert False == include_coord_key('location')
    assert False == include_coord_key('_latino')
    assert False == include_coord_key('how_long_live_LA')
    assert False == include_coord_key('Colon_Cleanout_Relative_Day')
    # True
    assert True == include_coord_key('lat_lon')
    assert True == include_coord_key('latitude')
    assert True == include_coord_key('LATITUDE')
    assert True == include_coord_key('Geographic location (latitude)')

def test_include_text_key():
    # False
    assert False == include_text_key('tumor location')
    assert False == include_text_key('anatomical location')
    assert False == include_text_key('platelocation')
    assert False == include_text_key('Plate location')
    assert False == include_text_key('chromosomal translocation')
    assert False == include_text_key('BodyLocation')
    assert False == include_text_key('DiseaseLocation')
    assert False == include_text_key('transect_location')
    assert False == include_text_key('Ulcer_location')
    # True
    assert True == include_text_key('geo_loc_name')
    assert True == include_text_key('location')
    assert True == include_text_key('geographic location (region and locality)')
    # TODO: False positives
    assert True == include_text_key('geographic location (altitude)')
    assert True == include_text_key('geographic location (depth)')
    assert True == include_text_key('geographic location (elevation)')
    assert True == include_text_key('GI_Location')
    assert True == include_text_key('Montreal CD Location Upper GI')
