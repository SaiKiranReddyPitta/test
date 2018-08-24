'''
    Author: Sai Kiran Reddy Pitta
    Date: 11-08-2018
'''

def follow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        follow function is called when arg1 wants to follows arg2
        so, this should result in adding arg2 to the followers list of arg1
        update the network dictionary and return it
    '''
    # network = {}
        # for i in range (0, len(list), 2):
        #     if list[i] in network:
        #         network[l_new[0]].append(i)
        # return network
    if arg1 in network:
        network[arg1].append(arg2)
    else:
        follow_list = []
        follow_list.append(arg2)
        network[arg1] = follow_list
    return network

def unfollow(network, arg1, arg2):
    '''
        3 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 and arg2 are two people in the network
        unfollow function is called when arg1 wants to stop following arg2
        so, this should result in removing arg2 from the followers list of arg1
        update the network dictionary and return it
    '''
    # network = {}
    #     for i in range (0, len(list), 2):
    #         if list[i] not in network:
    #             network[l_new[0]].append(i)
    return network
def delete_person(network, arg1):
    '''
        2 arguments are passed to this function
        network is a dictionary representing the social network
        arg1 is a person in the network
        delete_person function is called when arg1 wants to exit from the network
        so, this should result in deleting arg1 from network
        also, before deleting arg1, remove arg1 from the everyone's followers list
        update the network dictionary and return it
    '''
    # network = {}
    #     for i in range (0, len(list), 2):
    #         if list[i] in network:
    #             network[l_new[0]].delete(i)
    return network
def main():
    '''
        handling testcase input and printing output
    '''
    network = eval(input())
    lines = int(input())
    # print(network)
    for i in range(lines):
        i += 1
        line = input()
        output = line.split(" ")
        if output[0] == "follow":
            network = follow(network, output[1], output[2])
        elif output[0] == "unfollow":
            network = unfollow(network, output[1], output[2])
        elif output[0] == "delete":
            network = delete_person(network, output[1])

    print(network)

if __name__ == "__main__":
    main()
