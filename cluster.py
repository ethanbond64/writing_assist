import numpy as np
import math

def paragraphsToClusters(paragraphs,stop_words=None):
    # n_paragraphs = len(paragraphs)
    flatParagraphs = [flattenParagraph(paragraph) for paragraph in paragraphs]
    similarity_matrix = build_similarity_matrix(flatParagraphs,stop_words)
    clusters = similarityMatrixToClusters(similarity_matrix)
    return clusters

def similarityMatrixToClusters(similarity_matrix):
    clusters = []
    currentCluster = []
    for idx, value in enumerate(similarity_matrix):
        # print(value,idx)
        if idx < len(value)-1:
            if value[idx+1] > 0:
                currentCluster.append(idx)
            else:
                clusters = appendIfNotEmpty(clusters,currentCluster)
                currentCluster = [idx]
        else:
            clusters = appendIfNotEmpty(clusters,currentCluster)
    return clusters

def appendIfNotEmpty(outerList,innerList):
    if len(innerList) != 0:
        outerList.append(innerList)
        return outerList
    else:
        return outerList

def flattenParagraph(paragraph):
    flatParagraph = []
    for sentence in paragraph:
        flatParagraph += sentence
    return flatParagraph

def build_similarity_matrix(parapgraphs, stop_words=None):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(parapgraphs), len(parapgraphs)))

    for idx1 in range(len(parapgraphs)):
        for idx2 in range(idx1+1,len(parapgraphs)):
            if idx1 == idx2: #ignore if both are same parapgraphs
                similarity_matrix[idx1][idx2] = -1
                continue
            similarity_matrix[idx1][idx2] = parapgraph_similarity(parapgraphs[idx1], parapgraphs[idx2], stop_words)

    return similarity_matrix

def parapgraph_similarity(paragraph1, paragraph2, stopwords=None):
    if stopwords is None:
        stopwords = []

    all_words = [word for word in set(paragraph1 + paragraph2) if word not in stopwords]

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    # build the vector for the first sentence
    for w in paragraph1:
        if w not in stopwords:
            vector1[all_words.index(w)] += 1

    # build the vector for the second sentence
    for w in paragraph2:
        if w not in stopwords:
            vector2[all_words.index(w)] += 1

    return cosine_similarity(vector1, vector2)

def cosine_similarity(v1,v2):
    return (np.dot(v1,v2) / (math.sqrt(np.dot(v1,v1)) * math.sqrt(np.dot(v2,v2))))