# open file streams
inFile = open('testCCNums.txt', 'r')
outFile = open('output.txt', 'w')


# @brief define function to check validity of credit cards
# utilizes Luhn's algorithm
# 1. Starting with the second to last digit (from the right) of the number,
#    multiply every other digit by 2, recording each answer separately.
# 2. Sum all of the individual digits of all the products (not the products themselves) from Step 1.
# 3. To the sum obtained in Step 2, add all of the digits that were not multiplied by 2 in Step 1
# 4. If the last digit of the resulting sum is zero, (i.e., the total modulo 10 is equal to 0), the number is valid.
# @param credit_card_number_0
def is_credit_card_valid(credit_card_number_0):
    # variable deceleration
    length = len(credit_card_number_0)
    # list of digits to be multiplied by 2
    even_index_list = []
    # list of digits not multiplied by 2
    odd_index_list = []
    # numbers to be added, result stored in sum
    even_index_string = ""
    odd_index_string = ""
    # sums for step 1 and 2
    even_index_sum = 0
    odd_index_sum = 0
    # for loop in range <start, stop, step>
    for index_i in range(length - 2, -1, -2):
        # append adds to the trailing end of list_0
        # multiplying every other by two
        even_index_list.append(str(2 * int(credit_card_number_0[index_i])))
        # for loop of list_0
    for credit_card_1 in even_index_list:
        # addition assignment
        even_index_string += credit_card_1
    # strip() removes any extraneous spaces, leading and trailing
    even_index_string = even_index_string.strip()

    for index_i in even_index_string:
        # int() functions converts to integer bit by bit
        # and adds up and stores to sum_0
        even_index_sum += int(index_i)
    # for loop in range <start, stop, step>
    for index_i in range(length - 1, 0, -2):
        # The append() method adds a single item to the end of the list.
        odd_index_list.append(credit_card_number_0[index_i])

    for credit_card_1 in odd_index_list:
        odd_index_string += credit_card_1

    odd_index_string = odd_index_string.strip()
    for index_i in odd_index_string:
        odd_index_sum += int(index_i)
    credit_card_sum = str(even_index_sum + odd_index_sum)
    trailing_digit = int(credit_card_sum[len(credit_card_sum) - 1])
    # Checking if last digit is equal to zero
    # if it is return true else false
    if trailing_digit == 0:
        return 1
    else:
        return 0


# end is_credit_card_valid

def main():
    # variable deceleration
    credit_card_company = None
    eight_hyphens = " -------- "

    for credit_card_number in inFile:
        # strip() removes any extraneous spaces, leading and trailing
        credit_card_number = credit_card_number.strip()
        # stores head digit which is index zero of string number
        first_digit_of_credit_card = credit_card_number[0]
        second_digit_of_credit_card = credit_card_number[1]

        # if leading digit is a 4 than the card is a visa
        if first_digit_of_credit_card == '4':
            credit_card_company = 'VISA: '
        # if leading digit is a 3 and the second digit is a 4 or a 7
        # the card is a mastercard
        elif (first_digit_of_credit_card == '3') & (
                (second_digit_of_credit_card == '4') | (second_digit_of_credit_card == '7')):
            credit_card_company = 'MASTERCARD: '
        # if the leading digit is a 5 and the second digit is a 0 or a 5
        # the card is an american express
        elif (first_digit_of_credit_card == '5') \
                | (int(second_digit_of_credit_card >= '0')
                   & (int(second_digit_of_credit_card <= '5'))):
            credit_card_company = 'AMERICAN EXPRESS: '
        # if the card is valid write out the number, eight dashed, the card issuer, and valid
        # else  the card is not valid and write out the number, eight dashes, and invalid number
        if is_credit_card_valid(credit_card_number):
            temporary_housing = credit_card_number \
                                + eight_hyphens \
                                + credit_card_company \
                                + "VALID\n"
        else:
            temporary_housing = credit_card_number \
                                + eight_hyphens \
                                + "INVALID NUMBER\n"
        outFile.write(temporary_housing)


if __name__ == '__main__':
    main()
# close file streams
inFile.close()
outFile.close()
