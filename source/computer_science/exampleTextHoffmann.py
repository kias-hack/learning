import math
import numpy as np
import time

text = 'aaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbcccccddddef'

def twosmallvalfromdict(arr):
    for i in range(2):
        small = None
        for key in arr.keys():
            if small == None:
                small = key
            if arr[key] < arr[small]:
                small = key
        yield small, arr.pop(small)

def mergenode(nodes):
    newkey = ''
    newvalue = 0
    for key in nodes.keys():
        newkey = key + newkey
        newvalue = newvalue + nodes[key]
    return dict({newkey: newvalue})

def treehoffman(arrfreqchars):
    arr = arrfreqchars.copy()
    while len(arr) > 2:
        smalledvalue = dict(twosmallvalfromdict(arr))
        arr.update(mergenode(smalledvalue))
    return arr
    
def codecompute(arr):
    mapcode = dict()
    nodes = list(arr.keys())
    mapcode[nodes[0]] = 0
    code = 0
    counter = 1
    for char in reversed(nodes[1]):
        if counter == len(nodes[1]):
            code += 1
        else: 
            code = code * 2 + 2
        mapcode[char] = code
        counter += 1
    return mapcode

def hoffman(text):
    arrfreqchars = dict()
    for char in text:
        arrfreqchars[char] = arrfreqchars.setdefault(char,0) + 1
    return codecompute(treehoffman(arrfreqchars))
    
    
mapcode = hoffman(text)

with open('data', 'wb') as file:
    file.write(text.encode('utf-8'))

with open('datazip', 'wb') as file:
    for char in text:
        file.write(bytes([mapcode[char]]))




def checkarray(array):
    for i in range(len(array) - 1):
        if array[i+1] < array[i]:
            return "FALSE"
        return "TRUE"

def halfofarray(arr):
    lenarr = len(arr)
    if lenarr < 2:
        return arr
    middleofarray = math.floor(lenarr/2)
    firsthalf = list()
    for i in range(middleofarray):
        firsthalf.append(arr[i])
    lasthalf = list()
    for i in range(middleofarray, lenarr):
        lasthalf.append(arr[i])
    return firsthalf, lasthalf

def merge(arr1, arr2):
    result = list()
    while(len(arr1) > 0 or len(arr2) > 0):
        if len(arr1) > 0 and len(arr2) > 0:
            if arr1[0] < arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        elif len(arr2) > 0 :
            result.append(arr2.pop(0))
        else:
            result.append(arr1.pop(0)) 
    return result   

def recursiveSort(arr):
    """Рекурсивная сортировка"""
    if len(arr) <= 1:
        return arr
    first, last = halfofarray(arr)
    return merge(recursiveSort(first), recursiveSort(last))
    

def bubblesort(array):
    """Сортировка пузырьком"""
    sorted = 0
    for i in range(len(arr)):
        for e in range(len(arr) - sorted - 1):
            if arr[e] > arr[e + 1]:
                buff = arr[e]
                arr[e] = arr[e + 1]
                arr[e + 1] = buff
        sorted = sorted + 1
    return arr
