# The Problem: Classify Wikipedia Disease Articles

We provide a sample of articles taken from Wikipedia. There are lots of different kinds of articles, and one flavor is those that describe a disease. The data are html dumps of wikipedia articles. We give you a labelled set of disease articles (positives), and non-diseases articles (negatives).

*   **Part 1:** Use this data set to create a classifier that can accurately predict whether an article describes a disease.
*   **Part 2:** Extract the name of the disease. Optionally, include as much information as you can about the disease. E.g. information to consider are symptoms, causes, prognosis, prevention, treatment, relevant drugs, human/non-human susceptibility.

**The data:** The directory contains wikipedia article html dumps. There are direct wgets of the articles, e.g. [malaria](https://en.wikipedia.org/wiki/Malaria), [autism](https://en.wikipedia.org/wiki/Autism), [Parkinson's disease](https://en.wikipedia.org/wiki/Parkinson%27s_disease). They are organized into two directories: <tt>positive/</tt> and <tt>negative/</tt>. The positive dataset is 3,693 articles about diseases, and the negative dataset is 10,000 articles.

Here is the data set: [wikipedia_diseases.zip](http://challenge.20n.com/machine-learning/training.tar.gz)

**Edge cases:**

1.  Your classifier might misclassify drug articles as disease articles, e.g. [Penicillin](https://en.wikipedia.org/wiki/Penicillin), [Paracetamol](https://en.wikipedia.org/wiki/Paracetamol), [L-DOPA](https://en.wikipedia.org/wiki/L-DOPA), [Erythromycin](https://en.wikipedia.org/wiki/Erythromycin). Check if that is the case, and optionally try to fix that mis-classification.
2.  Exclude broad articles that talk about generic classes of diseases, e.g. [genetic disorders](https://en.wikipedia.org/wiki/Genetic_disorder), [infection](https://en.wikipedia.org/wiki/Infection), [bacteria](https://en.wikipedia.org/wiki/Bacteria), [virus](https://en.wikipedia.org/wiki/Virus), [mutation](https://en.wikipedia.org/wiki/Mutation). Fun: when you exclude these, what does your classifier do for [cancer](https://en.wikipedia.org/wiki/Cancer)?


## FAQs

**How long will this take?**  
That is yours to commit. Just get back within 7 days from the time this repository is shared with you.

**What language should I use?**  
Whatever you want. 

**Can I use X?**  
Unless the tool directly answers the question "are these disease articles?". You can use whatever you want. 

**How should I solve it?**
There are many solutions to non-convex problems. We are seeking a deep learning engineer, so deep learning models are preferrable. 

Through this we want to understand the core skills and methods you are developing as a problem solver.

**What should I deliver?**  
Your code, results, and brief instructions on how to build and run your solution. 

**What is this again?**
This is a simulation of a project that you might execute. Our goal is that by collaborating on this repo we will both learn from experience. 

**Is there an example solution?**

1. Naive Bayes Classifier - https://github.com/shkr/wikiclassifier/blob/master/wikiclassifier.pdf

## Overview of Beautiful Soup
Beautiful Soup is a Python library for pulling data out of HTML and XML files. It creates a parse tree that allows scrapping specific documents from the HTML or XML file.

**SETUP**
```
$ pip install beautifulsoup4
```
The ```find_all()``` method takes an HTML tag as a string argument and returns the list of elements that match with the provided tag. Here, we will extract all the ```<p>``` tags from the provided HTML files and store the extracted information in a CSV file.

The code for the same can be found in the repository.

## BERT for Text Classification
On a range of natural language processing tasks, the BERT(Bidirectional Encoder Representations from Transformers) deep learning model has produced state-of-the-art results. It is a powerful and game-changing NLP framework from Google. BERT models are usually pre-trained on a large corpus of text, then fine-tuned for specific tasks.
![bert-architecture width-1280](https://user-images.githubusercontent.com/91879854/179442183-ec854dc1-84ba-4e8c-a8a8-ba4b3446dd24.png)
For given text input, BERT creates a language representation model using the Transformer encoder architecture. The input to the BERT encoder is a  series of tokens that are first transformed into vectors and then processed by the neural network. By just adding a few layers to the basic BERT model, it can be applied to solve a wide range of language tasks.

**SETUP**

A dependency of the preprocessing for BERT inputs
```
$ pip install -U tensorflow-text==2.6.0
```
Link to BERT trained classification model
https://drive.google.com/file/d/1vI-HWRGEfehq2XjZBx_7CeWbBCmmZA1E/view?usp=sharing

The code for the same can be found in the repository.

## Custom NER model

SpaCy is an open-source Python library that does advanced natural language processing. It aids in the development of applications that process and "understand" massive amounts of text.  It can be used to create systems for information extraction, NLU, or text pre-processing for deep learning. Tokenization, Parts-of-Speech 
(PoS) Tagging, Text Classification, and Named Entity Recognition(NER) are a few of the functionalities offered by spaCy.

**SETUP**

SpaCy can be installed using a simple pip install.
```
$ pip install -U spacy
```
SpaCy NER already supports the entity types like - (PERSON)People, including fictional. (NORP)Nationalities or religious or political groups. (FAC)Buildings, airports, highways, bridges, etc. (ORG)Companies, agencies, institutions, etc. (GPE)Countries, cities, states, etc.

Our aim is to further train this model to incorporate for our own custom 
entities present in our dataset. 

Link to custom NER model
https://drive.google.com/drive/folders/12IxF6HKzgThH1TlpW8TlJ9nDBF4YEloK?usp=sharing

The code for the same can be found in the repository.

**TESTING THE MODELS**

To test the trained models, execute runner.ipynb script. Make sure tensorflow-text, beautifulsoup4 is installed first.








