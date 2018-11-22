#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : fromstring函数.py
# Date              : 20.11.2018
# Last Modified Date: 20.11.2018
"""
分析html，return a single element/document
"""
from lxml import html
tree = html.fromstring("<p>Hello, World!</p>")
print(html.tostring(tree))
