import os
from bs4 import BeautifulSoup
import pandas as pd

# convert to html document
# folder1 = "training/positive/"
# for filename in os.listdir(folder1):
#     src = folder1 + filename
#     dst = folder1 + filename + ".html"
#     os.rename(src, dst)

path_positives = 'training/positive'
path_negatives = 'training/negative'
positive = []
negative = []
sentence = ''

for filename in os.listdir(path_positives):
     if filename.endswith('.html'):
         fname = os.path.join(path_positives,filename)
         with open(fname, 'r', encoding="utf-8") as f:
             soup = BeautifulSoup(f.read(),'html5lib')
             # to extract all data from p tags for each disease.
             for data in soup.find_all('p'):
                 sentence += data.get_text()
         positive.append(sentence)
         sentence = ''

print("positives done")

dict_pos = {"Sentence": positive}
df = pd.DataFrame(dict_pos)
df.to_csv('positives.csv')

for filename in os.listdir(path_negatives):
     if filename.endswith('.html'):
         fname = os.path.join(path_negatives,filename)
         with open(fname, 'r', encoding="utf-8") as f:
             soup = BeautifulSoup(f.read(),'html5lib')
             # to extract all data from p tags for each non-disease.
             for data in soup.find_all('p'):
                 sentence += data.get_text()
         negative.append(sentence)
         sentence = ''

print("negatives done")

dict_neg = {"Sentence": negative}
df = pd.DataFrame(dict_neg)
df.to_csv('negatives.csv')
