import time
import random
#coding:utf-8
"""第二种方法：双向循环链表"""
"""没能实现最后一条需求，第一种方法实现了"""

class DNode(object):
    def __init__(self, prev, next, value):
        self.prev = prev  # 前驱
        self.next = next  # 后继
        self.value = value  # 值


class DoubleLinkTable(object):
    def __init__(self):
        self.nCount = 0  # 节点个数
        self.nHead = DNode(None, None, None)  # 表头
        self.nHead.prev = self.nHead  # 表头的前驱后继都是自己
        self.nHead.next = self.nHead  # 表头的前驱后继都是自己
        self.node = self.nHead

    # 节点数目
    def size(self):
        return self.nCount

    # 判断链表是否为空
    def is_empty(self):
        return self.nCount == 0

    # 获取index位置的节点
    def getnode(self, index):
        if index == 0:
            return self.nHead
        if index < 0 or index > self.nCount:
            raise Exception('IndexOutOfBounds')

        # 二分正向查找
        if index < self.nCount / 2:
            self.node = self.nHead.next
            i = 0
            while i < index - 1:
                self.node = self.node.next
                i += 1
            return self.node
        # 反向查找剩余部分
        self.node = self.nHead.prev
        rindex = self.nCount - index
        j = 0
        while j < rindex:
            self.node = self.node.prev
            j = j + 1
        return self.node

    # 插入新节点（后插）
    def insert(self, index, value):
        now_node = self.getnode(index)
        new_node = DNode(None, None, value)
        new_node.prev = now_node
        new_node.next = now_node.next
        now_node.next.prev = new_node
        now_node.next = new_node
        self.nCount += 1

    def change(self, index, value):
        now_node = self.getnode(index)
        now_node.value = value

    def delete(self, index):
        if index == 0:
            raise Exception('0 is not allowed!')
        now_node = self.getnode(index)
        now_node.prev.next = now_node.next
        now_node.next.prev = now_node.prev
        self.nCount -= 1

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.nHead
        last_time = 0
        # print(cur.value)
        while cur.prev != self.nHead and (cur.prev.value != None):
            cur = cur.prev
            print('随机数的值:' + str(cur.value) + ' 持续时间：' + str(last_time) + '秒')
            last_time += 1

    def travel1(self, now_node):
        """从最新插入数据的地方反向遍历链表"""
        if self.is_empty():
            return
        cur = now_node
        last_time = 0
        # print(cur.value)
        while cur.prev != now_node and (cur.prev.value != None):
            print('随机数的值:' + str(cur.value) + ' 持续时间：' + str(last_time) + '秒')
            cur = cur.prev
            last_time += 1


# 每隔一秒生成一个随机数
def gen_random_num():
    time.sleep(1)
    random_num = random.randint(0, 100)
    return random_num




# 使用dict模拟hash表，用于存储随机数信息，key为随机数的值，value为随机数在双向链表中的位置
hash_table = dict()
cur_random_list = []

if __name__ == '__main__':
    DCLinkList = DoubleLinkTable()
    cur_time = 0  # 开始的时刻 防止程序一直运行
    index = 0
    while cur_time < 1000:
        cur_time += 1
        random_num = gen_random_num()
        cur_random_list.append(random_num)
        # print(random_num)

        if DCLinkList.size() < 60:
            DCLinkList.insert(index, random_num)

            print("当前随机数列表： " + str(cur_random_list))
            DCLinkList.travel()
        elif DCLinkList.size() == 60:
            # pass
            index = index % 60
            DCLinkList.change(index, random_num)
            now_node = DCLinkList.getnode(index)

            print("当前随机数列表： " + str(cur_random_list))
            DCLinkList.travel1(now_node)
        index += 1