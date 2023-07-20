#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB, ComplementNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
from multiprocessing import Pool, Process
import json, jieba, threading, random

from keywords import keywords

datas = []
labels = []

def get_file(file_name):
    global datas, labels
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            record = json.loads(line)
            data_words = ' '.join(jieba.cut(record['question']))
            datas.append(data_words)
            for i in range(0, len(keywords)):
                if keywords[i] in record['answer'] and len(keywords[i]) >= len(record['answer']) - 2:
                    labels.append(i)
                    break

def work(vectorizer, classifier):
    X = vectorizer.fit_transform(datas)
    classifier.fit(X, labels)
    print(classifier.score(X, labels))
    pred = classifier.predict(X)
    cnt = 0
    for i in range(0, len(pred)):
        if pred[i] > 0: 
            cnt += 1
            # print(datas[i])
    print(cnt)
    while(True):
        s = str(input(">"))
        s = ' '.join(jieba.cut(s))
        s_v = vectorizer.transform([s])
        op = classifier.predict(s_v)
        if random.randint(0, 4):
            print(keywords[random.randint(0, len(keywords) - 1)])
        else:
            print(keywords[op[0]])



get_file("text.jsonl")
work(TfidfVectorizer(), RandomForestClassifier(n_estimators=155, random_state=43))