#-*- coding:utf-8 -*-
import sys
sys.path.append('..')
import jieba.analyse
import Global_param


def get_keywords(day):
    fr = open(Global_param.test_root +
              'test/train_date_set1/train_date_set1_%d.txt' % day)
    f1 = open(Global_param.test_root +
              'test/key_words/keywords_%d.txt' % day, 'w')
    txt = ''
    for line in fr.readlines():
        txt = txt + line.strip().split('\t')[3] + ','
    t = jieba.analyse.extract_tags(txt, Global_param.number_jieba)
    for i in t:
        try:
            f1.write(i.encode('utf-8') + '\t')
        except UnicodeEncodeError as e:
            print i

get_keywords(1)