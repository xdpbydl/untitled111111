import random

caps = []
choice_str = 'FB'
for i in range(9):
    caps.append(random.choice(choice_str))

caps = ['F', 'B', 'B', 'B', 'B', 'B', 'F', 'F', 'B', 'B', 'B', 'F', 'F']
# cap1 = ['B', 'F', 'B', 'B', 'B', 'B', 'F', 'F', 'F', 'F', 'B', 'F', 'F', 'F']
print(caps)


def please_conform(caps):
    start = forward = backward = 0
    intervals = []
    for i in range(1, len(caps)):
        if caps[start] != caps[i]:
            intervals.append((start, i - 1, caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i
    intervals.append((start, len(caps) - 1, caps[start]))
    if caps[start] == 'F':
        forward += 1
    else:
        backward += 1
    if forward < backward:
        flip = 'B'
    else:
        flip = 'F'
    print(intervals)
    for t in intervals:
        if t[2] == flip:
            print(f'{flip}  People in positions, {t[0]}, "through", {t[1]}, flip you caps')


please_conform(caps)


def please_conform_onepass(cap):
    """
    优化后的代码，
    """
    cap = cap + [cap[0]]
    for i in range(1, len(cap)):
        if cap[i] != cap[i - 1]:
            if cap[i] != cap[0]:
                print(f'Pelple in positions, {i},', end='')
            else:
                print(f'through, {i - 1},flip your cap')


please_conform_onepass(caps)
