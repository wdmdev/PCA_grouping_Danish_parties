import os
import re
from enum import Enum
import numpy as np

class SplitType(Enum):
    Single = 1
    Files = 2
    Lines = 3

def __clean(data, stop_symbols):
    for s in stop_symbols:
        data = data.replace(s,'')

    data = re.sub(r'[^\w\s]|[0-9]','',data)
    return data


def loadFiles(folder, split_type, num_of_lines):
    '''
    Loads all .txt files from the given folder (with subfolders)
    returns them as a list of strings.
    '''
    enc = 'utf8'

    #Parties to exclude
    with open('exclude.txt', 'r', encoding='utf8') as ex:
        exclude = [e.replace('\n', '') for e in ex.readlines()]

    #variables
    party_docs = np.array([])
    labels = np.array([])
    symbols = [r'\ufeff']

    #Iterating through subfolders
    if len(exclude) > 0:
        print('Excluded: {0}'.format(exclude))

    for party in os.listdir(folder):
        if party not in exclude:
            p = os.path.join(folder, party)
            labels = np.append(labels,party)
            documents = np.array([])
            for f in os.listdir(p):
                #Reading files
                with open(os.path.join(p, f), "r", encoding=enc) as file:
                    doc = file.read().lower()
                    doc = __clean(doc,symbols)
                    if split_type != SplitType.Lines:
                        doc = doc.replace('\n','')
                    if split_type == SplitType.Lines:
                        doc = np.asarray(doc.splitlines())
                    documents = np.append(documents,doc)

            if split_type == SplitType.Single:
                documents = ' '.join(documents)
            if split_type == SplitType.Lines:
                documents = documents[:num_of_lines]
 
            party_docs = np.append(party_docs,documents)

    return (party_docs, labels)

