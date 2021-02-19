from pathlib import Path
from biosample_parse_functions import (
    include_coord_key,
    include_text_key
)


key_list_dir = Path('tests', 'attribute_key_lists')
geo_coord_include = Path(key_list_dir, 'geo_coord_include.txt')
geo_coord_exclude = Path(key_list_dir, 'geo_coord_exclude.txt')
geo_coord_exclude_todo = Path(key_list_dir, 'geo_coord_exclude_todo.txt')
geo_text_include = Path(key_list_dir, 'geo_text_include.txt')
geo_text_exclude = Path(key_list_dir, 'geo_text_exclude.txt')
geo_text_exclude_todo = Path(key_list_dir, 'geo_text_exclude_todo.txt')


def test_include_coord_key():
    with open(geo_coord_include) as f:
        for line in f:
            line = line.rstrip()
            print(line)
            assert include_coord_key(line) == True
    with open(geo_coord_exclude) as f:
        for line in f:
            line = line.rstrip()
            print(line)
            assert include_coord_key(line) == False
    with open(geo_coord_exclude_todo) as f:
        for line in f:
            line = line.rstrip()
            print(line)
            assert include_coord_key(line) == True


def test_include_text_key():
    with open(geo_text_include) as f:
        for line in f:
            line = line.rstrip()
            print(line)
            assert include_text_key(line) == True
    with open(geo_text_exclude) as f:
        for line in f:
            line = line.rstrip()
            print(line)
            assert include_text_key(line) == False
    with open(geo_text_exclude_todo) as f:
        for line in f:
            line = line.rstrip()
            print(line)
            assert include_text_key(line) == True
