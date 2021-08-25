jijin_file_dict = {159949: [58, '1'], 'BZ': [57, '1'], 588000: [54, '1']}
n=1
for k, v in jijin_file_dict.items():
    if k == "BZ":
        print(v[1])
        v[1] = f"bz{str(n + 1)}.xls"
        print(v[1] + '111')
    else:
        v[1] = f"{str(n + 1)}.xls"
print(jijin_file_dict)
print(jijin_file_dict['BZ'][1])
