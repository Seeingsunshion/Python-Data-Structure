#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    检测链表中是否有环
"""

import collections
import sys


class LinkListNode(object):
    """
    链表结点
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)

# 使用命名的元组 表示一个输入的测试用例
# 包含 元素个数 元素数组 以及环形开始结点的位置(从1开始索引)
InputCase = collections.namedtuple('InputCase', 'elementCount elements loopToIndex')


def loop_detect_by_map(list_head):
    """
    使用map判断链表中是否存在环
    :param list_head: 表头结点 表头为空结点
    :return: 1如果存在环 否则0
    """
    visited_nodes = {}
    cur_node = list_head
    while cur_node:
        node_id = id(cur_node)
        if node_id in visited_nodes:
            return 1
        visited_nodes[node_id] = True
        cur_node = cur_node.next
    return 0


def loop_detect_by_pointer(list_head):
    """
    使用fast slow指针检测环是否存在
    :param list_head: 链表头结点
    :return: 1如果存在环 否则0
    """
    if not list_head:
        return 0
    slow = list_head.next
    fast = slow
    # 慢指针step=1 快指针step=2
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if not slow or not fast:
            return 0
        if fast == slow:
            return 1
    return 0


def floyd_cycle_detection(list_head):
    """
    Floyd 环检测算法
    :param list_head: 链表头结点
    :return:返回环入口位置 不存在环时返回0
    """
    if not list_head:
        return 0
    slow = list_head.next
    fast = slow
    has_loop = False
    # 慢指针step=1 快指针step=2
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if not slow or not fast:
            return 0
        if fast == slow:
            has_loop = True
            break
    if not has_loop:
        return 0
    # 将慢指针放到链表头 两个指针均以step=1移动直到相遇时 即为环的入口位置
    slow = list_head.next
    node_index = 1
    while slow != fast:
        slow = slow.next
        fast = fast.next
        node_index += 1
    return node_index


def make_test_case_link_list(input_case):
    """
    为测试用例建立链表
    :param input_case: 输入的测试用例
    :return: 该测试用例对应的链表
    """
    the_loop_node = None
    list_head = LinkListNode()
    tail_node = list_head
    for index, element in enumerate(input_case.elements):
        tail_node.next = LinkListNode(element)
        tail_node = tail_node.next
        if index + 1 == input_case.loopToIndex:
            the_loop_node = tail_node
    tail_node.next = the_loop_node
    return list_head


def parse_test_input_file(input_file_name):
    """
    解析输入的测试文件
    :param input_file_name: 输入文件路径
    :return: 测试用例
    """
    with open(input_file_name, "r") as f:
        lines = f.read().splitlines()
    case_count = int(lines[0])
    line_index = 1
    test_cases = []
    for i in range(case_count):
        parts = lines[line_index:line_index+3]
        element_count = int(parts[0])
        elements = [int(x) for x in parts[1].split(" ")]
        tail_point_to = int(parts[2])
        test_cases.append(InputCase(element_count, elements, tail_point_to))
        line_index += 3
    return test_cases


if __name__ == "__main__":
    input_cases = parse_test_input_file("input.txt")
    if not input_cases:
        print("input test case not right")
        sys.exit(-1)
    for case in input_cases:
        head_node = make_test_case_link_list(case)
        #print("%s" % (loop_detect_by_map(head_node) == 1))
        print("loop index= %s" % (floyd_cycle_detection(head_node)))
