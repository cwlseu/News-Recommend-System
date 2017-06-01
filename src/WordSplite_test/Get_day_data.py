#-*- coding:utf-8 -*-

import Global_param


def transfor_data(day):

    fr = open(Global_param.test_root + 'test/train_lastdat_constant_set1.txt')
    f = open(Global_param.test_root +
             'test/train_lastday_set/train_lastday_set1_%d.txt' % day, 'w')
    for line in fr.readlines():
       # line.strip().split('\t')
        t = line.strip().split('\t')[4]
        if int(line.strip().split('\t')[4]) == day:
            f.write(line)


def transfor_dataset(day):

    fr = open(Global_param.test_root + 'test/train_date_set1.txt')
    f = open(Global_param.test_root +
             'test/train_date_set1/train_date_set1_%d.txt' % day, 'w')
    for line in fr.readlines():
        t = line.strip().split('\t')[4]
        if int(line.strip().split('\t')[4]) == day:
            f.write(line)
