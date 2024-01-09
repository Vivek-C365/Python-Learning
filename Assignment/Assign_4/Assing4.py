# Get user input
number = int(input("Enter a number between 0 and 999: "))

# Define dictionaries for numbers 0-20 and tens places
numbers_dict = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen"
}
tens_dict = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
             7: "seventy", 8: "eighty", 9: "ninety"}

if 0 <= number <= 999:
    if number in numbers_dict:
        print(numbers_dict[number])
    elif number < 100:
        ten = number // 10
        one = number % 10
        if one == 0:
            print(tens_dict[ten])
        else:
            print(tens_dict[ten] + "-" + numbers_dict[one])
    else:
        hundred_val = number // 100
        remainder = number % 100
        ten = remainder // 10
        one = remainder % 10
        
        print("hundred_value", hundred_val)
        print("remainder", remainder)
        print("ten_value",ten)
        print("one_value",one)

        if remainder == 0:
            print(numbers_dict[hundred_val] + " hundred")
        elif remainder < 20:
            print(numbers_dict[hundred_val] + " hundred  " + numbers_dict[remainder])
        else:
            if one == 0:
                print(numbers_dict[hundred_val] + " hundred " + tens_dict[ten])
            else:
                print(numbers_dict[hundred_val] + " hundred " + tens_dict[ten] + "-" + numbers_dict[one])
else:
    print("Please enter a number between 0 and 999.")
