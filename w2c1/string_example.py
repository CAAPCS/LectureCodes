
def compute_tip(total_bill, tip=0.15):
    return total_bill * tip

def get_string_to_last_char(str):
    return str[:-1]

if __name__ == '__main__':

    print(compute_tip(100, tip=0.2))

    # example_string = "hello!"
    #
    # # 'H' -> 'e' -> 'l' -> 'l' -> 'o' -> '!'
    # # 0      1       2     3       4      5
    #
    # print(example_string[-6])
    #
    # print(example_string[:-1])
