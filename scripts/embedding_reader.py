import numpy as np

def read_glove_file():
    embedding_vector = {}
    fileGlove = open('../../../../embeddings/glove_s300.txt')
    
    for line in fileGlove:
        value = line.split(' ')
        word = value[0]
        coef = np.asarray(value[1:], dtype='float32')
        embedding_vector[word] = coef

    fileGlove.close()

    return embedding_vector