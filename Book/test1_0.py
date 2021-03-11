import random

caps = []
choice_str = 'TF'
for i in range(10):
    caps.append(random.choice(choice_str))

# caps = ['T', 'F', 'T', 'T', 'T', 'F', 'F', 'T', 'T', 'T']
print(caps)


def keep_com(caps_list):
    str_a = []
    str_b = []
    str_c = []
    no_a = -10
    no_b = -10

    for no, val in enumerate(caps_list):
        if val == choice_str[0]:
            str_a.append(no + 1)
        elif val == choice_str[1]:
            str_b.append(no + 1)

    def com_a_b(a_b_list):
        ll = []
        for a in range(len(a_b_list)):
            try:
                a_b_list[a + 1]
            except:
                break
            if a_b_list[a + 1] - a_b_list[a] == 1:
                continue
            else:
                ll.append(a_b_list[a])
        return ll

    print(str_a)
    print(str_b)
    print(com_a_b(str_a))
    print(com_a_b(str_b))


# keep_com(caps)


def keep_com_a(caps_l):
    caps_l += [caps_l[0]]
    for u in range(1, len(caps_l)):
        if caps_l[u] != caps_l[u - 1]:
            if caps_l[u] != caps_l[0]:
                print(f'从{u}开始，', end='')
            else:
                print(f'到{u - 1}结束，反转。')


keep_com_a(caps)
