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
    assert include_coord_key('location') == False
    assert include_coord_key('_latino') == False
    assert include_coord_key('how_long_live_LA') == False
    assert include_coord_key('Colon_Cleanout_Relative_Day') == False
    # True
    assert include_coord_key('lat_lon') == True
    assert include_coord_key('latitude') == True
    assert include_coord_key('LATITUDE') == True
    assert include_coord_key('Geographic location (latitude)') == True

def test_include_text_key():
    # False
    assert include_text_key('tumor location') == False
    assert include_text_key('anatomical location') == False
    assert include_text_key('platelocation') == False
    assert include_text_key('Plate location') == False
    assert include_text_key('chromosomal translocation') == False
    assert include_text_key('BodyLocation') == False
    assert include_text_key('DiseaseLocation') == False
    assert include_text_key('transect_location') == False
    assert include_text_key('Ulcer_location') == False
    # True
    assert include_text_key('geo_loc_name') == True
    assert include_text_key('location') == True
    assert include_text_key('geographic location (region and locality)') == True
    # TODO: False positives
    assert include_text_key('geographic location (altitude)') == True
    assert include_text_key('geographic location (depth)') == True
    assert include_text_key('geographic location (elevation)') == True
    assert include_text_key('GI_Location') == True
    assert include_text_key('Montreal CD Location Upper GI') == True
