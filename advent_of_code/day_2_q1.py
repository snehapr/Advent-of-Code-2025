# --- Day 2: Gift Shop ---

# You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.
#
# As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.
#
# As it turns out, one of the younger Elves was playing on a gift shop computer and managed to add a whole bunch of invalid product IDs to their gift shop database! Surely, it would be no trouble for you to identify the invalid product IDs for them, right?
#
# They've even checked most of the product ID ranges already; they only have a few product ID ranges (your puzzle input) that you'll need to check. For example:
#
# 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124
# (The ID ranges are wrapped here for legibility; in your input, they appear on a single long line.)
#
# The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).
#
# Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
#
# None of the numbers have leading zeroes; 0101 isn't an ID at all. (101 is a valid ID that you would ignore.)
#
# Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:
#
# 11-22 has two invalid IDs, 11 and 22.
# 95-115 has one invalid ID, 99.
# 998-1012 has one invalid ID, 1010.
# 1188511880-1188511890 has one invalid ID, 1188511885.
# 222220-222224 has one invalid ID, 222222.
# 1698522-1698528 contains no invalid IDs.
# 446443-446449 has one invalid ID, 446446.
# 38593856-38593862 has one invalid ID, 38593859.
# The rest of the ranges contain no invalid IDs.
# Adding up all the invalid IDs in this example produces 1227775554.


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


def has_double_digit(number):
    num_str= str(number)
    len_num = len(num_str)
    if len_num % 2 !=0:
        return False
    half = len_num // 2
    return num_str[:half] == num_str[half:]



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
# adding_invalid_product_ids:31000881061


