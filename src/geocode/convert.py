from text_nlp import clean_geo_text
import boto3
client = boto3.client('location')

def get_coords(text):
    text = clean_geo_text(text)
    if len(text) > 200:
        text = text[:200]
    if text.isdigit():
        return (None, None)
    result = client.search_place_index_for_text(
            IndexName="ExamplePlaceIndex",
            MaxResults=1,
            Text=text)
    if len(result['Results']) == 0:
        return (None, None)
    return result['Results'][0]['Place']['Geometry']['Point']
