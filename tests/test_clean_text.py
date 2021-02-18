from biosample_parse_functions import (
    clean_text,
    remove_null_values
)

def test_remove_null_values():
    assert remove_null_values('not available: not collected') == ': '

def test_clean_text():
    assert clean_text('not available: not collected') == ':'
    assert clean_text('"foo"') == 'foo'
    assert clean_text('naples') == 'naples'
    assert clean_text('na') == None
