num_a = 12345678910000000

def from_left_format_num(num):
    num = str(num)
    if len(num) <= 3:
        return num
    new_num = ''
    skip_num = len(num)%3
    for k in range(skip_num):
        new_num += num[k]
        if num[k] == num[skip_num-1]:
            new_num += ','
    for i in range(len(num)-skip_num):
        if i % 3 == 0 and i != 0:
            new_num += ','
        new_num += num[i+skip_num]
    return new_num

print(from_left_format_num(num_a))
print(from_left_format_num(126437444))
print(from_left_format_num(19723651263452))
print(from_left_format_num(1234))
print(from_left_format_num(38745623785))
print(from_left_format_num(22))
print(from_left_format_num(126))