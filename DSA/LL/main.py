class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    cur = head
    while cur:
        print(cur.data, end=' ')
        cur = cur.next
    print('')


def search(head, val):
    cur = head
    pos = 1
    while cur:
        if cur.data == val:
            return pos
        pos += 1
        cur = cur.next
    return -1


def insert_at_front(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node


def insert_at_end(head, val):
    new_node = Node(val)
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = new_node
    return head


def insert_at_pos(head, pos, val):
    new_node = Node(val)
    cur = head
    prev = None
    cur_pos = 1
    while cur and cur_pos < pos:
        if cur_pos == pos:
            break
        else:
            cur_pos += 1
            prev = cur
            cur = cur.next
    new_node.next = cur
    if prev is None:
        head = new_node
    else:
        prev.next = new_node
    return head


def delete_first(head):
    if head is None:
        return None
    return head.next


def delete_last(head):
    if head is None:
        return None
    if head.next is None:
        return None
    cur = head
    while cur.next.next:
        cur = cur.next
    cur.next = None
    return head


def reverse_list(head):
    cur = head
    prev = None
    next_node = head.next
    while cur.next:
        cur.next = prev
        prev = cur
        cur = next_node
        next_node = next_node.next
    cur.next = prev
    return cur


def insert_sorted(head, data):
    temp = Node(data)
    if head is None:
        return temp
    elif data < head.data:
        temp.next = head
        return temp
    else:
        cur = head
        while cur.next and cur.next.data < data:
            cur = cur.next
        temp.next = cur.next
        cur.next = temp
        return head


def sum_of_items(head):
    ans = 0
    cur = head
    while cur:
        ans += cur.data
        cur = cur.next
    return ans


def recursive_reverse(head):
    if head is None or head.next is None:
        return head
    sub_list_head = recursive_reverse(head.next)
    sub_list_tail = head.next
    sub_list_tail.next = head
    head.next = None
    return sub_list_head


def add_two_list(head1, head2):
    cur1 = head1
    while cur1:
        data = cur1.data
        head2 = insert_sorted(head2, data)
        cur1 = cur1.next
    return head2


head = Node(15)
node1 = Node(21)
node2 = Node(32)

head.next = node1
node1.next = node2

print_list(head)

print(search(head, 13))

head = insert_at_front(head, 14)
print_list(head)

head = insert_at_end(head, 48)
print_list(head)

head = insert_at_pos(head, 8, 61)
print_list(head)

head = insert_at_pos(head, 1, 13)
print_list(head)

print('soted way')
head = insert_sorted(head, 23)
print_list(head)

print(f'Sum of items: {sum_of_items(head)}')

head = delete_last(head)
print_list(head)

head = delete_first(head)
print_list(head)

print('Reverse')
head = recursive_reverse(head)
print_list(head)
