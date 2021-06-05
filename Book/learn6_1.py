def compare(group_a, group_b):
    if sum(group_a) > sum(group_b):
        result = 'left'
    elif sum(group_a) < sum(group_b):
        result = 'rigth'
    elif sum(group_a) == sum(group_b):
        result = 'equal'
    return result


def split_coins(coins_list):
    length = len(coins_list)
    group1 = coins_list[0:length // 3]
    group2 = coins_list[length // 3:length // 3 * 2]
    group3 = coins_list[length // 3 * 2:length]
    return group1, group2, group3


def find_fake_group(group1, group2, group3):
    result_1_2 = compare(group1, group2)
    if result_1_2 == 'left':
        fake_group = group1
    elif result_1_2 == 'rigth':
        fake_group = group2
    elif result_1_2 == 'equal':
        fake_group = group3
    return fake_group


def coin_comparison(coin_list):
    counter = 0
    curr_list = coin_list
    while len(curr_list) > 1:
        group1, group2, group3 = split_coins(curr_list)
        curr_list = find_fake_group(group1, group2, group3)
        counter += 1
    fake = curr_list[0]
    print(f'The fake coin is coin{coin_list.index(fake) + 1} in the original list')


