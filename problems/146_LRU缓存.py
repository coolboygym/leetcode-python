class Node(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_value_map = dict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.get_node(key)
        return node.value if node else -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.get_node(key)
        # key已经存在
        if node:
            node.value = value
            return
        # key不存在，创建新节点并移到最前面
        node = Node(key, value)
        self.key_value_map[key] = node
        self.push_front(node)
        # 数量超过容量，在映射表和链表中都删除最后一个节点
        if len(self.key_value_map) > self.capacity:
            last_node = self.dummy.prev
            del self.key_value_map[last_node.key]
            self.remove(last_node)
    
    # 获取key对应的节点，并移到链表最前面(因为该节点被访问了)
    def get_node(self, key):
        if key not in self.key_value_map:
            return None
        node = self.key_value_map[key]
        self.remove(node)
        self.push_front(node)
        return node
    
    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
    
    # 把节点移到表头
    def push_front(self, x):
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


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
