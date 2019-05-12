# reading the file
from trie_tree import TrieTree
def reading_route(file_name):
    '''
    Reading the route costs from the text file and return
    dictionary {route#: cost}
    '''
    with open(file_name) as f:
        dict_of_routes = dict()

        for line in f:
            pair = line.strip().split(',')
            pair[0] = pair[0].replace('+', '')
            dict_of_routes[pair[0]] = pair[1]

            # slicing
            # dict_of_routes[pair[0][1:]] = pair[1]
            # print(pair)
        
        # d = dict(line.strip().split(',') for line in f)
        # return d

    return dict_of_routes


def reading_phone_numbers(file_name):
    '''
    Reading the phone numbers  from the text file and return
    list of phone numbers
    '''
    with open(file_name) as f:
        # remove the '+' sign and reads new line
        f = f.read().replace('+', '').split('\n')
    return f


def call_costs():
    """Return a price for each phone number"""
    phone_number, price = 0, 0
    call_cost = [phone_number, price]
    
    # file_paths 
    route_costs_4 = "project/data/route-costs-4.txt"
    phone_numbers_3 = "project/data/phone-numbers-3.txt"
    # route_costs_10 = "project/data/route-costs-100.txt"
    # phone_numbers_10 = "project/data/phone-numbers-100.txt"

    
    # read routes and phone numbers
    route_costs = reading_route(route_costs_4)
    # create a trie with all the routes
    route = TrieTree(route_costs)
    # # read phone numbers
    # phone_numbers = reading_phone_numbers(phone_numbers_3)
    phone_num_price = route.search("19876543210")
    print("size of trie: ", route.size)
    print(phone_num_price)
    # return call_cost


def main():
    # route_costs_4 = "project/data/route-costs-4.txt"
    # phone_numbers_3 = "project/data/phone-numbers-3.txt"
    # # route_costs_10 = "project/data/route-costs-100.txt"
    # # phone_numbers_10 = "project/data/phone-numbers-100.txt"

    # call_costs = reading_route(route_costs_4)
    # print(len(call_costs))
    # phone_numbers = reading_phone_numbers(phone_numbers_3)
    # print(len(phone_numbers))
    pass


if __name__ == "__main__":
    call_costs()
