from collections import defaultdict

class Node(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1   # 节点创建时就被访问了，访问次数置为1
        self.prev = None
        self.next = None

# 构建一个双向链表
def new_list():
    dummy = Node()
    dummy.prev = dummy
    dummy.next = dummy
    return dummy


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        # 记录当前最少被访问的次数，在移除最不常用项时使用
        self.min_freq = 1
        # key值到节点的映射
        self.key_node_map = dict()
        # 节点被访问频次到对应双向链表的映射
        self.freq_list_map = defaultdict(new_list)

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
        if node:
            node.value = value
            return

        # 达到容量需要做额外操作
        if len(self.key_node_map) == self.capacity:     
            dummy = self.freq_list_map[self.min_freq]
            back_node = dummy.prev
            del self.key_node_map[back_node.key]
            self.remove(back_node)
        #创建一个新节点
        node = Node(key, value)
        self.key_node_map[key] = node
        self.push_front(self.freq_list_map[1], node)
        self.min_freq = 1

    # 删除一个节点
    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
    
    # 将给定节点移到给定链表的头部
    def push_front(self, dummy, x):
        x.prev = dummy
        x.next = dummy.next
        x.prev.next = x
        x.next.prev = x
    
    # 获取key对应的节点，并移到正确的位置
    def get_node(self, key):
        if key not in self.key_node_map:
            return None
        node = self.key_node_map[key]
        self.remove(node)
        dummy = self.freq_list_map[node.freq]
        if dummy.next == dummy:     # 移除节点后当前链表为空
            if node.freq == self.min_freq:  # 当前链表的访问次数最少
                self.min_freq = self.min_freq + 1
        node.freq = node.freq + 1
        self.push_front(self.freq_list_map[node.freq], node)
        return node


if __name__ == '__main__':
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4