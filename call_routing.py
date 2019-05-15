from time import time
# from __future__ import division
# reading the file
from trie_tree import TrieTree


ROUTE_FILE_FORMAT = "project/data/route-costs-{}.txt"
PHONE_FILE_FORMAT = "project/data/phone-numbers-{}.txt"
OUTPUT_FILE_FORMAT = 'call_costs/call-costs-{}.txt'

# RUNTIME_SEPARATOR_FORMAT = "======================================== Scenario {scenario_num} ========================================"


def reading_phone_numbers(file_name, num_phones=None):
    '''
    Reading the phone numbers  from the text file and return
    list of phone numbers
    ''' 
    file_name = PHONE_FILE_FORMAT.format(num_phones)
    with open(file_name) as f:
        # remove the '+' sign and reads new line
        f = f.read().replace('+', '').split('\n')

    return f

def read_routes(file_name):
    '''
    Reading the route costs from the text file and return
    dictionary {route#: cost}
    '''
    with open(file_name) as f:

        list_of_routes = list()

        for line in f:
            pair = line.strip().split(',')
            route = pair[0].replace('+', '')
            price = pair[1]

            list_of_routes.append([route, price])

            # route_tree.add(route_and_price[0], route_and_price[1])

        print(len(list_of_routes))

    return list_of_routes


def build_trie_with_routes(routes_and_prices):
    '''
    Load the routes from list of list into trie tree
    '''
    route_tree = TrieTree()

    for pair in routes_and_prices:
        route = pair[0]
        price = float(pair[1])
        route_tree.add(route, price)
    
    return route_tree
    # return route_tree.size


def find_call_costs_with_trie(route_tree, phone_numbers_list):
    call_costs = []
    for phone_number in phone_numbers_list:
        cost = route_tree.search(str(phone_number))
        call_costs.append((phone_number, cost))
    return call_costs


def save_call_costs_to_file(phones_and_call_costs):
    '''
    Write the costs of calling each phone number to an output file.
    '''
    file_name = OUTPUT_FILE_FORMAT.format(len(phones_and_call_costs))
    with open(file_name, 'w') as file:
        for phone_number, cost in phones_and_call_costs:
            # print("phone#:", phone_number)
            # print("cost:", cost)
            file.write('+{}, {}\n'.format(phone_number, cost))


    # print("route_tree: ", route_tree.size)
    # phone = '34747997'  #0.26
    # cost = route_tree.search(phone)
    # print("cost: ", cost)


def write_costs(list_of_phone_numbers, route_tree):
    pass
    # with open('call-costs{}.txt'.format(len(list_of_phone_numbers)), 'w') as file:
    #     for phone_number in list_of_phone_numbers:
    #         cost = route_tree.search(phone_number)
    #         file.write('{}, {}'.format(phone_number, cost))


def call_costs(num_routes, num_phones):
    """Return a price for each phone number"""
    route_costs_100 = ROUTE_FILE_FORMAT.format(100)
    route_costs_35000 = "project/data/route-costs-35000.txt"
    route_costs_100k = "project/data/route-costs-106000.txt"
    route_costs_1mln = "project/data/route-costs-1000000.txt"
    route_costs_10mln = "project/data/route-costs-10000000.txt"
    route_costs_4 = "project/data/route-costs-4.txt"

    start_time = time()

    # Step 1: read route costs and phone numbers
    route_costs = ROUTE_FILE_FORMAT.format(num_routes)
    routes_and_prices = read_routes(route_costs)

    phone_numbers = PHONE_FILE_FORMAT.format(num_phones)
    phone_numbers_list = reading_phone_numbers(phone_numbers, 3)

    file_read_time = time() - start_time
    print(f"Time to read 2 files: {file_read_time}")
    start_time = time()

    # Step 2: build trie with routes and costs
    tree = build_trie_with_routes(routes_and_prices)

    build_trie_time = time() - start_time
    print(f"Time to build trie: {build_trie_time}")
    start_time = time()

    phone_numbers_100 = "project/data/phone-numbers-100.txt"
    phone_numbers_1000 = "project/data/phone-numbers-1000.txt"
    phone_numbers_3 = "project/data/phone-numbers-3.txt"
    phone_numbers_1000 = "project/data/phone-numbers-1000.txt"
    phone_numbers_10k = "project/data/phone-numbers-10000.txt"

    # Step 3: find call costs with trie
    call_costs = find_call_costs_with_trie(tree, phone_numbers_list)
    
    search_trie = time() - start_time
    print(f"Time to Search trie: {search_trie}")
    start_time = time()


    # Step 4: output results to a file
    save_call_costs_to_file(call_costs)
    save_call_cost_time = time() - start_time
    print(f"Time to save_call_cost_time in trie: {save_call_cost_time}")
    # start_time = time()

    overall_time = (file_read_time + build_trie_time + search_trie + save_call_cost_time)

    print(f'OverAll_time: {overall_time}')
    

if __name__ == "__main__":
    # scenario 2
    

    # print(RUNTIME_SEPARATOR_FORMAT.format("2"))
    call_costs(106000, 1000) # search time => 0.00008511543273925781
    

    # scenario 2
    # call_costs(100, 10)



'''
Optimization Notes:
Want to create an array of lenth 2 with routing number and its price, then load it into the Trie Tree
    - This means reassigning the added array for each [route, cost] in the file that's being read in
'''
