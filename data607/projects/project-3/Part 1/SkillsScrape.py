#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:39:18 2024

@author: jonathancruz
"""

import requests
from bs4 import BeautifulSoup
import math
import pandas as pd


#list will hold job id
l=[]
#
o={}

k=[]

target_url='https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=Data%20%28Scientist%20&location=Las%20Vegas%2C%20Nevada%2C%20United%20States&geoId=100293800&currentJobId=3415227738&start={}'
for i in range(0,math.ceil(117/25)):
    res = requests.get(target_url.format(i))
    soup=BeautifulSoup(res.text,'html.parser')
    alljobs_on_this_page=soup.find_all("li")
    for x in range(0,len(alljobs_on_this_page)):
        jobid = alljobs_on_this_page[x].find("div",{"class":"base-card"}).get('data-entity-urn').split(":")[3]
        l.append(jobid)
        
class bcolors:

    WARNING = '\033[93m'
   

print(f"{bcolors.WARNING}Warning: If above list below  has less than ten values or empty consider stopping it and rerunning")

target_url='https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{}'
for j in range(0,len(l)):

    resp = requests.get(target_url.format(l[j]))
    soup=BeautifulSoup(resp.text,'html.parser')

    g = soup.find_all("li")
    rels = soup.find_all("li", {"class": "description__job-criteria-item"})
    designs = soup.find_all("li", {"class": "ellipsis-menu__item"})
    nones = soup.find_all("None")
    for d in  designs:
        d.decompose()   

    for r in rels:
        r.decompose()  
    
    for m in g:
        if len( m.get_text ( strip = True )) == 0: 
  
        # Remove empty tag 
            m.extract() 
        else:
            
            k.append(m.get_text())
                    
#clean list of datatype that might randomly appear
for index in range(len(k)):
    if type(k[index]) != str:
         k[index] = ""
         
while("" in k):
    k.remove("")


l1 = list()
target_url='https://www.coursera.org/browse/data-science'

res = requests.get(target_url)
soup=BeautifulSoup(res.text,'html.parser')
courses = soup.find("section", {"aria-label" : "Most Popular Courses Carousel"})
all_courses=courses.find_all("div",{"class":"slick-slide"})
for i in all_courses:
       l1.append(i.find("a").get('href'))
       
print(l)

skillz = set()
target_url='https://www.coursera.org/{}'
for j in range(0,len(l1)):

    resp = requests.get(target_url.format(l1[j]))
    soup=BeautifulSoup(resp.text,'html.parser')
    skills_contatiners = soup.find_all("li", {"class":"css-0"})
    for i in skills_contatiners:
        if i.find("a") is not None:
            skillz.add(i.find("a").get_text())
            

print(skillz)


from re import sub
from gensim.utils import simple_preprocess
import numpy as np

def preprocess(doc):
    # Tokenize, clean up input document string
    stopwords = ['the', 'and', 'are', 'a']
    doc = sub(r'<img[^<>]+(>|$)', " image_token ", doc)
    doc = sub(r'<[^<>]+(>|$)', " ", doc)
    doc = sub(r'\[img_assist[^]]*?\]', " ", doc)
    doc = sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', " url_token ", doc)
    return [token for token in simple_preprocess(doc, min_len=0, max_len=float("inf")) if token not in stopwords]


query_string = 'Leadership'

ranking_list = list()


import gensim.downloader as api
glove = api.load("glove-wiki-gigaword-50")    

def rank_word(query_string):
    documents = k
    

    
    # From: https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/soft_cosine_tutorial.ipynb
    
    
    # Preprocess the documents, including the query string
    corpus = [preprocess(document) for document in documents]
    query = preprocess(query_string)
    
    
    
    from gensim.corpora import Dictionary
    from gensim.models import TfidfModel
    from gensim.models import WordEmbeddingSimilarityIndex
    from gensim.similarities import SparseTermSimilarityMatrix
    from gensim.similarities import SoftCosineSimilarity
    
    # Load the model: this is a big file, can take a while to download and open
    
    similarity_index = WordEmbeddingSimilarityIndex(glove)
    
    # Build the term dictionary, TF-idf model
    dictionary = Dictionary(corpus+[query])
    tfidf = TfidfModel(dictionary=dictionary)
    
    # Create the term similarity matrix.  
    similarity_matrix = SparseTermSimilarityMatrix(similarity_index, dictionary, tfidf)
    
    query_tf = tfidf[dictionary.doc2bow(query)]
    
    index = SoftCosineSimilarity(
                tfidf[[dictionary.doc2bow(document) for document in corpus]],
                similarity_matrix)
    
    doc_similarity_scores = index[query_tf]
    
    # Output the sorted similarity scores and documents
    sorted_indexes = np.argsort(doc_similarity_scores)[::-1]
    for idx in sorted_indexes:
        print(f'{idx} \t {doc_similarity_scores[idx]:0.3f} \t {documents[idx]}')
    print(np.sum(doc_similarity_scores))
    ranking_list.append([query_string, np.sum(doc_similarity_scores)] )

for skill in skillz:
    rank_word(skill)
print(ranking_list)

file_name = "skills.csv"

df = pd.DataFrame(ranking_list, columns=['Skills', 'Relevancy'])
df.to_csv(file_name, encoding='utf-8', index=False)












