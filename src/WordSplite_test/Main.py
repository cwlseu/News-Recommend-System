#-*- coding:utf-8 -*-
import sys
sys.path.append('..')
import Get_day_data
import Get_keywords
import Get_keynews
import Delete_Repeat
import Get_hot_result
import Global_param


def main():
    for i in range(1, Global_param.number_day):
        Get_day_data.transfor_data(i)
        Get_day_data.transfor_dataset(i)
        Get_keywords.get_keywords(i)
        Get_keynews.get_keynews(i)
    Delete_Repeat.delete_duplicate()
    Get_hot_result.get_hot_result(Global_param.hot_rate)
if __name__ == '__main__':
	main()

