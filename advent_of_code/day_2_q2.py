# --- Part Two ---
# The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?
#
# Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.
#
# From the same example as before:
#
# 11-22 still has two invalid IDs, 11 and 22.
# 95-115 now has two invalid IDs, 99 and 111.
# 998-1012 now has two invalid IDs, 999 and 1010.
# 1188511880-1188511890 still has one invalid ID, 1188511885.
# 222220-222224 still has one invalid ID, 222222.
# 1698522-1698528 still contains no invalid IDs.
# 446443-446449 still has one invalid ID, 446446.
# 38593856-38593862 still has one invalid ID, 38593859.
# 565653-565659 now has one invalid ID, 565656.
# 824824821-824824827 now has one invalid ID, 824824824.
# 2121212118-2121212124 now has one invalid ID, 2121212121.
# Adding up all the invalid IDs in this example produces 4174379265.

from collections import Counter

input_list = [
    "119-210","907313-1048019","7272640820-7272795557","6315717352-6315818282",
    "42-65","2234869-2439411","1474-2883","33023-53147","1-15","6151-14081",
    "3068-5955","65808-128089","518490556-518593948","3535333552-3535383752",
    "7340190-7548414","547-889","34283147-34389716","44361695-44519217",
    "607492-669180","7071078-7183353","67-115","969-1469","3636264326-3636424525",
    "762682710-762831570","827113-906870","205757-331544","290-523",
    "86343460-86510016","5536957-5589517","132876-197570","676083-793651",
    "23-41","17920-31734","440069-593347"
]



# input_list = [
#     "11-22", "95-115", "998-1012", "1188511880-1188511890", "222220-222224",
#     "1698522-1698528", "446443-446449", "38593856-38593862", "565653-565659",
#     "824824821-824824827", "2121212118-2121212124"
# ]

def split_input(input_list):
    start = []
    end = []
    for item in input_list:
        s, e = item.split('-')
        start.append(int(s))
        end.append(int(e))
    return start, end

def is_count_greater(number):
    digit_counts =Counter(number)
    for count in digit_counts.values():
        if count < 2:
            return False
    return True

def is_continous(number):
    prev = number[0]
    for digit in number[1:]:
        if digit != prev:
            return False
    return True

def is_half_equal(number):
    len_num = len(number)
    for size in range(1, len_num // 2 + 1):
        if len_num % size == 0:
            part = number[:size]
            if part * (len_num // size) == number:
                return True
    return False


def has_double_digit(number):
    num_str= str(number)
    len_num = len(num_str)
    # if len_num % 2 !=0:
    #     return False
    is_count = is_count_greater(num_str)
    is_continous_number = is_continous(num_str)
    is_half = is_half_equal(num_str)

    if (is_count and is_continous_number) or is_half:
        return True
    return False


start_array , end_array = split_input(input_list)
print(f'start_array:{start_array}')
print(f'end_array:{end_array}')

invalid_product_id = []

for i in range(len(start_array)):
    for number in range(start_array[i], end_array[i]+1):
        result = has_double_digit(str(number))
        if result:
            print(f'found double digit number:{result}')
            invalid_product_id.append(number)


adding_invalid_product_ids = sum(invalid_product_id)
print(f'adding_invalid_product_ids:{adding_invalid_product_ids}')
# adding_invalid_product_ids:46769308485


