import sys
from collections import defaultdict
sys.path.append("..")
import WordSplite_test.Global_param

distance_time = 10000

"""
u_id, article_id, timestamp, title, current_mouth_day
5218791 100648598   1394463264  消失前的马航370   8

"""
def get_user_last():
    with  open(WordSplite_test.Global_param.test_root +
              'test/train_date_set1.txt') as f1, \
            open(WordSplite_test.Global_param.test_root +
              'test/train_lastdat_constant_set1.txt', 'w') as fr:
        dic = defaultdict(list)
        for line in f1.readlines():
            dic[line.strip().split('\t')[0]].append(int(line.strip().split('\t')[2]))

        for k, v in dic.iteritems():
            list1 = list(set(v))
            # print list1
            t1 = max(list1)
            # print t1
            list1.remove(t1)
            # print list1
            if list1:
                t2 = max(list1)
                # print t2
                # print t1 - t2
            else:
                t2 = -5000
            if (t1 - t2) <= distance_time:
                dic[k] = str(t1)

        for line2 in f1.readlines():
            if dic[line2.strip().split('\t')[0]] == line2.strip().split('\t')[2]:
                fr.write(line2)

if __name__ == '__main__':
    get_user_last()
