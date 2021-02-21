from nltk import word_tokenize, pos_tag, ne_chunk
from nltk import Tree
import truecase


# from https://stackoverflow.com/a/48676189/4410590
def get_continuous_chunks(text, label):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    prev = None
    continuous_chunk = []
    current_chunk = []

    for subtree in chunked:
        if type(subtree) == Tree and subtree.label() == label:
            current_chunk.append(" ".join([token for token, pos in subtree.leaves()]))
        if current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
        else:
            continue

    return continuous_chunk


def clean_geo_text(text):
    text_cased = truecase.get_true_case(text)
    geo_text = get_continuous_chunks(text_cased, 'GPE')
    return ' '.join(geo_text)
