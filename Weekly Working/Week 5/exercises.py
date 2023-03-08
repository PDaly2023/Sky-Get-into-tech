from collections import Counter

#Question 1
def cels_to_fahr(celcius):
    fahr =((9 * celcius) / 5) + 32
    return fahr


print(cels_to_fahr(-5))
print(cels_to_fahr(30))
print(cels_to_fahr(100))

print('\n')

#Question 2
def multip_tables(number, maximum=12):

    for i in range(1,maximum+1):
        print(number * i)
    return


num_choice = input('Please input the number you would like to see the multiplication table for:')
multip_tables(int(num_choice))

#Question 3
def average_number(numbers_list, average_type = 2):
    if average_type == 1: #mean:
        # all numbers added together, divided by number of elements
        result = 0
        for i in numbers_list:
            result += int(i)
        print('The sum of the input numbers is:', result)
        mean = result / len(numbers_list)
        print('The mean average of the input numbers is:', mean)

    if average_type == 2: #mode:
        # The most commonly occuring value
        count = dict(Counter(numbers_list))
        print('The modal average of the input numbers is:', max(count, key=count.get))


    if average_type == 3: #median:
        # Place all values in order, smallest to highest. find the one in the middle
        numbers_list.sort()
        if len(numbers_list) %2 == 0:
            middle_number = int(len(numbers_list) / 2)
            left_middle = int(numbers_list[middle_number-1])
            right_middle = int(numbers_list[middle_number])
            median = (left_middle + right_middle) / 2
            print('the median value of the numbers given is:', median)

        else:
            middle_number = int((len(numbers_list) +1) / 2)
            median = (numbers_list[middle_number-1])
            print('the median value of the numbers given is:', median)
    return


print('\n')

av_type = input('''Which Average type would you like?
1. Mean
2. Mode
3. Median\n''')

numbers_chosen = (input('Please add your numbers separated by a comma:'))
numbers_list = numbers_chosen.split(',')

average_number(numbers_list, int(av_type))


