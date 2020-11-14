import time

def print_ftim():

    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

    return time_string

