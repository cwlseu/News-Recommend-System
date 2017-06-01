def find_top(l, number):
  """Get the `number` of top frequence item in `l`  """
  top_list = []
  for j in range(0, number):
    items = dict([(l.count(i), i) for i in l])
    max_value = items[max(items.keys())]
    top_list.append(max_value)
    l = delect_key(l, max_value)
  return top_list


def delect_key(l, key):
    for i in l:
        if i == key:
            l.remove(key)
    return l

if __name__ == '__main__':
    l = ['33', '1', '412', '1', '35', '33', '412', '412']
    print find_top(l, 3)
