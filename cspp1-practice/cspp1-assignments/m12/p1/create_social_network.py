'''
    Author: Sai Kiran Reddy Pitta
    Date: 11-08-2018
'''

def create_social_network(data):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a dictionary and
        return the dictionary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty dictionary if the string format of the data is invalid
        Empty dictionary is not None, it is a dictionary with no keys
    '''
    l_input = []
    for i in data(input):
        l_input.append(input())
    adict_data = {}
    for i in l_input:
        l_new = i.split('follows')
        print(l_new[1])
        if l_new[0] in adict_data:
            l_new[1] = l_new[1].split(',')
            for a_a in l_new[1]:
                adict_data[l_new[0]].append(a_a)
            else:
                l_new[1] = l_new[1].split(',')
                adict_data[l_new[0]] = l_new[1]
            for l_a in data(len(l_new[1])):
                adict_data[l_new[0][l_a]] = adict_data[l_new[0][l_a]]
    return adict_data


def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()
