
# --------------------------RECURSION-----------------------------

def to_string(n):
    str_nums = '0123456789'

    if n < 10:
        return str_nums[n]

    new_n = n // 10
    mod_n = n % 10
    return toString(new_n) + str_nums[mod_n]


def reverse_string(my_string):
    if len(my_string) == 0:
        return my_string
    return my_string[-1] + reverse_string(my_string[:-1])

# print(reverse_string('abcdef'))


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

# print(fibonacci(6))


def get_sum(lst):

    if len(lst) == 1:
        return lst[0]

    return lst[0] + get_sum(lst[1:])

print(get_sum([1, 2, 3, 4])


def get_index(s, lst):
    if not lst:
        return None

    if s == lst[0]:
        return 0


def sortedInsert(head, data):
    if not head.data:
        head.data = data
    elif data < head.data:
        new_head = DoublyLinkedListNode(data)
        new_head.next = head
        head.prev = new_head
        return new_head
    cur = head
    while cur.next:
        if data < cur.next.data:
            break
        else:
            cur = cur.next
    saved = cur.next
    cur.next = DoublyLinkedListNode(data)
    cur.next.prev = cur
    cur.next.next = saved
    return head








