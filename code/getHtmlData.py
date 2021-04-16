#!/usr/bin/env python
# coding: utf-8

# 리스트 컴프리헨션을 사용하여 HTML Element의 텍스트를 반환하는 사용자 정의 함수를 생성합니다.
def getText(x, css):
    return [i.select(selector = css)[0].text for i in x]

# 리스트 컴프리헨션을 사용하여 HTML Element의 속성값을 반환하는 사용자 정의 함수를 생성합니다.
def getAttr(x, css, key):
    return [i.select(selector = css)[0].get(key = key) for i in x]

