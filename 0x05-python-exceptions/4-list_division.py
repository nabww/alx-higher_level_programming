#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    count = 0
    i = 0
    new_list = []
        for i in range(list_length):
            try:
            r = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except TypeError:
                print("Wrong type")
                new_list.append(0)
            except IndexError:
                print("out of range")
                new_list.append(0)
            finally:
                new_list.append(0)
        return new_list
