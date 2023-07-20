#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jsonlines
from keywords import keywords
str1 = ""
str2 = ""

def get(o):
    ss = []
    with open("datas/{}.txt".format(o), 'r') as f:
        for line in f: ss.append(line)
    for i in range(0, len(ss)):
        if o in ss[i]:
            str1 = ""
            i += 1
            while i < len(ss):
                if "zsq" in ss[i]: break
                if o in ss[i]: break
                str1 += ss[i]
                i += 1
        if i >= len(ss): break
        if "zsq" in ss[i]:
            str2 = ""
            i += 1
            while i < len(ss):
                if o in ss[i]: break
                if "zsq" in ss[i]: break
                str2 += ss[i]
                i += 1
            for key in keywords:
                if key in str2 and len(str2) <= len(key) + 2:
                    with jsonlines.open("text.jsonl", 'a') as f:
                        f.write({"question": str1, "answer": str2})
                    str1 = str2 = ""
                    break
    

names = ["xccz", "lpr", "whr", "lzf", "hsb", "zzx", "lrc"]
for o in names: get(o)