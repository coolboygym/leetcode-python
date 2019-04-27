class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.double_list = DoubleList()
        self.mapping = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        target_node = self.mapping.get(key, None)
        if target_node is not None:
            result = target_node.value
            self.double_list.delete(target_node)
            self.double_list.insert(target_node)
            return result
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        target_node = self.mapping.get(key, None)
        if target_node is not None:
            target_node.value = value
            self.double_list.delete(target_node)
            self.double_list.insert(target_node)
        else:
            if self.size == self.capacity:
                temp_key = self.double_list.delete_tail_node()
                self.size -= 1
                del self.mapping[temp_key]
            new_node = ListNode(key=key, value=value)
            self.mapping[key] = new_node
            self.double_list.insert(new_node)
            self.size += 1


class ListNode(object):
    def __init__(self, key=None, value=None):
        self.left_pointer = None
        self.right_pointer = None
        self.key = key
        self.value = value

    def get_value(self):
        return self.value


class DoubleList(object):
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.right_pointer = self.tail
        self.tail.left_pointer = self.head

    def insert(self, target_node):
        # 在链表开头插入新节点
        second_node = self.head.right_pointer
        target_node.right_pointer = second_node
        target_node.left_pointer = self.head
        self.head.right_pointer = target_node
        second_node.left_pointer = target_node

    @staticmethod
    def delete(target_node):
        # 删除指定的节点
        front_node = target_node.left_pointer
        behind_node = target_node.right_pointer
        front_node.right_pointer = behind_node
        behind_node.left_pointer = front_node
        target_node.left_pointer = None
        target_node.right_pointer = None

    def delete_tail_node(self):
        # 删除在队尾的节点
        target_node = self.tail.left_pointer
        key = target_node.key
        self.delete(target_node)
        return key


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
