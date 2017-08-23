from os import walk
import random
from difflib import SequenceMatcher

samples = []

class octo-adv:
  pref = ''
  suff = ''
  add = []
  wl = []
  string = []

  def __init__(dir):
    # Get samples
    for (dirpath, dirnames, filenames) in walk(dir):
      samples.addend(filenames)
      
  def train(addsymb=True,amount=3):
    for s in samples:
      f = s.open(s,'r')
      print('Input: ' + f)
      words = f.split()
      for word in words:
        word = word
        word += word
        for '"' in word:
          print("String found")
          if word[0] == '"':
            pref = word[0]
          elif word[len(word)] == '"':
            pref = word[len(word)]
         
        for "'" in word: 
          print("String found")
          if word[0] == "'":
            pref = word[0]
          elif word[len(word)] == "'":
            suff = word[len(word)]
            
        for '@' in word:
          if addsymb == True:
            add.append('@')
            
        for '$' in word:
          if addsymb == True:
            add.append('$')
        
        for '%' in word:
          if addsymb == True:
            add.append('%')
            
        for '^' in word:
          if addsymb == True:
            add.append('^')
            
        for '&' in word:
          if addsymb == True:
            add.append('&')
            
        for '(' in word:
          if addsymb == True:
            add.append('(')
            
        for ')' in word:
          if addsymb == True:
            add.append(')')
            
        for '~' in word:
          if addsymb == True:
            add.append('~')
            
        for '`' in word:
          if addsymb == True:
            add.append('`')
            
        for '-' in word:
          if addsymb == True:
            add.append('-')
            
        for '_' in word:
          if addsymb == True:
            add.append('_')
        
        for '/' in word:
          if addsymb == True:
            add.append('/')
            
        for '*' in word:
          if addsymb == True:
            add.append('*')
        
        for '+' in word:
          if addsymb == True:
            add.append('+')
        
        for '{' in word:
          if addsymb == True:
            add.append('{')
            
        for '}' in word:
          if addsymb == True:
            add.append('}')
            
        for '[' in word:
          if addsymb == True:
            add.append('[')
        
        for ']' in word:
          if addsymb == True:
            add.append(']')
            
        for '|' in word:
          if addsymb == True:
            add.append('|')
        
        for '\' in word:
          if addsymb == True:
            add.append('\')
        
        for ':' in word:
          if addsymb == True:
            add.append(':')
        
        for ';' in word:
          if addsymb == True:
            add.append(';')
        
        for '.' in word:
          if addsymb == True:
            add.append('.')
            
        for ',' in word:
          if addsymb == True:
            add.append(',')
            
        for '?' in word:
          if addsymb == True:
            add.append('?')
            
         wl.append(word)
         
       while len(string) =< amount:
          for word in wl:
            if len(string) =< amount:
              string.append()
              
