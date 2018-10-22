from collections import Counter
def total_fruit(tree):
    count = Counter()
    start = 0
    ret = []
    for j in range(len(tree)):
        count[tree[j]] += 1
        while len(count) >= 3:
            count[tree[start]] -=1
            if count[tree[start]] == 0:
                count.pop(tree[start])
            start += 1
        ret.append(j-start +1)
    return max(ret)

assert total_fruit([1,0,1,4,1,4,1,2,3]) == 5