#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from keywords import keywords
import random

while(True):
    s = input("> ")
    print(keywords[random.randint(0, len(keywords) - 1)])