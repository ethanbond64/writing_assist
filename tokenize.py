import re

def textToParagraphs(text):
    paragraphs =  text.lower().split('\n')
    paragraphs = [paragraphToSentences(paragraph) for paragraph in paragraphs if len(paragraph) > 0]
    return paragraphs

def paragraphToSentences(paragraph):
    sentences = paragraph.replace('?','.').replace('!','.').split('.')
    sentences = [tokenizeSentence(sentence) for sentence in sentences if len(sentence) > 0]
    return sentences

def tokenizeSentence(sentence):
    sentence = sentence.replace('"','')
    sentence = sentence.replace("'",'')
    sentence = sentence.replace(',','')
    sentence = sentence.replace('*','')
    sentence = sentence.replace('+','')
    # sentence = sentence.replace('-',' ')
    sentence = sentence.replace(')',' ')
    sentence = sentence.replace('(',' ')
    sentence = sentence.replace('{',' ')
    sentence = sentence.replace('}',' ')
    sentence = sentence.replace('[',' ')
    sentence = sentence.replace(']',' ')

    tokens = sentence.split()
    return tokens

