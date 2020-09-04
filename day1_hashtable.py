import random
import time

"""第一种方法： 使用hash表"""


# 每隔一秒生成一个随机数
def gen_random_num():
    time.sleep(1)
    random_num = random.randint(0, 100)
    return random_num


# hash表存储随机数信息
random_dict = dict()
# 插入的时间
insert_time = 0
# 同步系统的当前时间
cur_time = 0
# 最终的输出结果
res_list = []
if __name__ == '__main__':
    while cur_time < 1000:
        # 生成随机数
        random_num = gen_random_num()

        # 将随机数信息和插入的时间作为键值对插入hash表
        # 因为随机数只会在【1,100】生成，所以这个hash表的键值对不超过100
        random_dict[random_num] = insert_time

        # 插入时间和当前时间同时增加1秒
        cur_time += 1
        insert_time += 1
        # 遍历整个hash表，取出满足插入时间在当前时间向前数60秒范围内的数，以（随机数，持续时间）插入数组
        for number, time_insert in random_dict.items():
            if cur_time - 60 <= time_insert < cur_time:
                res_list.append((number, cur_time - time_insert))
        # 对数组进行排序 按照持续时间从短到长
        res_list = sorted(res_list, key=lambda x: x[1])

        # 输出结果
        print("===================================================")
        for number, last_time in res_list:
            print("随机数为：" + str(number) + ",存活时长为：" + str(last_time))

        # 重置输出的序列
        res_list = []
