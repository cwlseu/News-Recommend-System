#-*- coding:utf-8 -*-
from collections import defaultdict
import Global_param


def delete_duplicate():
    with open(Global_param.test_root + 'test/result.txt') as f, \
            open(Global_param.test_root + 'test/train_date_set1.txt') as f1, \
            open(Global_param.test_root + 'test/result_no_repeat.txt', 'w') as fr:
        dic = defaultdict(list)
        num = 0
        for line1 in f1.readlines():
            dic[line1.strip().split('\t')[0]].append(
                line1.strip().split('\t')[1])

        for line in f.readlines():
            try:
                [user, new] = line.strip().split('\t')
                if new not in dic[user]:
                    fr.write(line)
                    num = num + 1
            except:
                continue
        print "detete_duplicate 消除重复项，推荐列表中去重已经阅览过的, 还剩 %d" % num

if __name__ == '__main__':
    delete_duplicate()
