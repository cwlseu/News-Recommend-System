import top_k
import sys
sys.path.append("../WordSplite_test")
import Global_param

def list_to_dic():
    fr = open(Global_param.test_root + 'test/train_date_set1.txt')
    fr1 = open(Global_param.test_root + 'test/train_lastdat_set1.txt')
    f = open('../../test/lastday_fit_hot_6.txt', 'w')
    dic = {}
    for i in range(1, 32):
        list = []
        dic[i] = list
    for line in fr.readlines():
        dic[int(line.strip().split('\t')[4])].append(
            line.strip().split('\t')[1])
    # print dic

    for k, v in dic.iteritems():
        dic[k] = top_k.find_top(v, 1)
    print dic
    for line1 in fr1.readlines():
        for i in range(0, 1):
            print line1.strip().split('\t')[0] + '\t' + dic[int(line1.strip().split('\t')[4])][i] + '\n'
            f.write(line1.strip().split('\t')[
                    0] + '\t' + dic[int(line1.strip().split('\t')[4])][i] + '\n')

list_to_dic()