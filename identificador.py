# -*- coding: utf-8 -*-
import csv

tag_vector = []
with open('arquivo1.csv', 'r', encoding="utf8") as listNormas:
    norm_reader = csv.reader(listNormas, delimiter=';')
    next(norm_reader) #pass through the header
    for line in norm_reader: #for each line in the list norm_reader
         sentence = line[14] #we get the text column
         #print(sentence)
         with open('arquivo2.csv', 'r', encoding='utf8') as listTags:
             tag_reader = csv.reader(listTags, delimiter=';')
             next(tag_reader)
             for j in tag_reader:
                tag = j[0] #this gets the first column
                if sentence.upper().find(tag.upper()) != -1:
                    #print('achamos '+ tag)
                    tag_vector.append(tag)
             #print(tag_vector)
             print('O id_normativo', line[0], 'é composto pelas tags\t')
             print(tag_vector)
             tag_vector.clear() #reset the vector for another line iteration
