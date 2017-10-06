#!/usr/bin/python
# -*- coding: UTF-8 -*-


class LinkListNode(object):
    """
    链表结点
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)


class LinkList(object):
    """
    链表类
    """
    def __init__(self):
        self.head = LinkListNode()  # 表的头指针
        self.tail = self.head   # 表的尾指针

    def __str__(self):
        head = self.head.next
        output_str = "LinkList["
        while head:
            output_str += str(head.data)+", "
            head = head.next
        output_str += "]"
        return output_str

    def is_empty(self):
        return self.head == self.tail

    def clear(self):
        while not self.is_empty():
            self.pop_front()

    def push_back(self, data):
        self.tail.next = LinkListNode(data)
        self.tail = self.tail.next

    def back(self):
        if self.is_empty():
            return None
        else:
            return self.tail.data

    def pop_back(self):
        if self.head != self.tail:
            cur_node = self.head
            while cur_node.next != self.tail:
                cur_node = cur_node.next
            del cur_node.next
            cur_node.next = None
            self.tail = cur_node

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.head.next.data

    def push_front(self, data):
        self.head.next = LinkListNode(data, self.head.next)
        if self.tail == self.head:   # 如果加入第一个结点 则需要重设尾指针
            self.tail = self.head.next

    def pop_front(self):
        cur_node = self.head.next
        if cur_node:
            self.head.next = cur_node.next
            if not self.head.next:  # 如果删除后为空 则需要重设尾指针
                self.tail = self.head
            del cur_node

    def remove_at(self, index):
        cur_node = self.head.next
        prev_node = self.head
        loop_index = 0
        while cur_node:
            if loop_index == index:
                prev_node.next = cur_node.next
                if cur_node == self.tail:   # 删除最后一个元素 则需要重设尾指针
                    self.tail = prev_node
                del cur_node
                return True
            else:
                prev_node = cur_node
                cur_node = cur_node.next
                loop_index += 1
        return False

    @staticmethod
    def print_list(list_head):
        """
        打印链表
        :param list_head: 链表头结点
        :return:None
        """
        output_str = str(list_head)
        print(output_str)

if __name__ == "__main__":
    link_list = LinkList()
    print("push back 5")
    link_list.push_back(5)

    print("push front 4")
    link_list.push_front(4)

    print("push back 6")
    link_list.push_back(6)

    print("push front 3")
    link_list.push_front(3)

    LinkList.print_list(link_list)

    print("remove at 2:", link_list.remove_at(2))
    LinkList.print_list(link_list)

    print("remove at 4:", link_list.remove_at(4))
    LinkList.print_list(link_list)

    print("push back 7")
    link_list.push_back(7)

    print("push back 8")
    link_list.push_back(8)

    LinkList.print_list(link_list)
    print("back is: ", link_list.back())
    print("front is: ", link_list.front())

    print("pop front")
    link_list.pop_front()

    print("pop back")
    link_list.pop_back()

    print("pop front")
    link_list.pop_front()

    print("pop back")
    link_list.pop_back()

    print("pop front")
    link_list.pop_front()

    print("is list empty ? %s" % link_list.is_empty())
    print("push back 3")
    link_list.push_back(3)
    print("is list empty ? %s" % link_list.is_empty())
    LinkList.print_list(link_list)

    print("clear list")
    link_list.clear()

    LinkList.print_list(link_list)

