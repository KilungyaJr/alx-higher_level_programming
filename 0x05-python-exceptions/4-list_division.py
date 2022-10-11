#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            div_list.append(my_list_1[i] / my_list_2[i])
            continue
        except ZeroDivisionError:
            print("division by 0")
            div_list.append(0)
        except TypeError:
            print("wrong type")
            div_list.append(0)
        except IndexError:
            print("out of range")
            div_list.append(0)
        finally:
            pass
    return div_list
