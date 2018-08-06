'''
Author: Sai Kiran Reddy Pitta - 20186002
Date: 06-08-2018
Encoding: Utf-8
'''

def paying_debt_off_in_a_year(unpaid_balance, yearly_interest_rate, monthly_payment_rate):
    '''to calculate remaining balance'''
    balance_copy = unpaid_balance

    iterator_j = 1
    while iterator_j <= 12:
        montly_interest_rate = yearly_interest_rate / 12.0
        minimum_monthly_payment = monthly_payment_rate*balance_copy
        monthly_unpaid_balance = balance_copy - minimum_monthly_payment
        balance_copy = monthly_unpaid_balance + (montly_interest_rate * monthly_unpaid_balance)
        iterator_j += 1
    return "Remaining balance: "+str(round(balance_copy, 2))
def main():
    '''main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(paying_debt_off_in_a_year(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()
    