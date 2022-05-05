import ast


def str_to_dict(str_a):
    return ast.literal_eval(str_a)

aa = str_to_dict("{'1':'dfdf'}")
print(type(aa))