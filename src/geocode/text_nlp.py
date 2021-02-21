# This module is unused by the geocoding step.
# NLP should be used at the extraction step so we can get clean data for geocoding

from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import Tree
import truecase


node_types = {'NN', 'NNS', 'NNP', 'CD', ':', '.', ','}
geo_labels = {'GPE', 'PERSON', 'ORGANIZATION'}

# derived from https://stackoverflow.com/a/48676189/4410590
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    continuous_chunk = []

    for item in chunked:
        if type(item) == Tree:
            subtree = item
            if subtree.label() in geo_labels:
                named_entity = " ".join([token for token, pos in subtree.leaves()])
                continuous_chunk.append(named_entity)
        elif item[1] in node_types:
            continuous_chunk.append(item[0])

    return continuous_chunk


def clean_geo_text(text):
    text_cased = truecase.get_true_case(text)
    geo_text = get_continuous_chunks(text_cased)
    return ' '.join(geo_text)
