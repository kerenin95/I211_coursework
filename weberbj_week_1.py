'''
Week 1 Challenge questions 
'''

# 1
def enter_list():
    input_list = input("Please enter a comma separated list: ")
    new_list = input_list.split(",")

    if len(new_list) % 2 ==0:
        mid = len(new_list) // 2
        return new_list[mid]

    elif len(new_list) % 2 != 0:
        mid = len(new_list) // 2
        return new_list[mid]

    else: 
        return "Somehow this isn't a valid list."

# 2
def names():
    input_names = input("Please enter a comma separated list of words: ")
    name_list = input_names.split(",")

    for name in name_list:
        print(name)
    


if __name__=="__main__":
    print(enter_list())
    names()