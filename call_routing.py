from time import time
from trie_tree import TrieTree


ROUTE_FILE_FORMAT = "project/data/route-costs-{}.txt"
PHONE_FILE_FORMAT = "project/data/phone-numbers-{}.txt"
OUTPUT_FILE_FORMAT = 'call_costs/call-costs-{}.txt'


def read_phone_numbers(file_name, num_phones=None):
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
    Reading the route and costs from the text file and return
    list of list
    '''
    with open(file_name) as f:
        list_of_routes = list()
        for line in f:
            pair = line.strip().split(',')
            route = pair[0].replace('+', '')
            price = pair[1]

            list_of_routes.append([route, price])
    
    print(f"{len(list_of_routes)} of Routes.")
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
    '''
    Search the trie filled with routes and return list of phone number associated its price
    '''
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


def call_costs(num_routes, num_phones):
    """Return a price for each phone number"""
    
    start_time = time()
    
    # Step 1: read route costs and phone numbers
    route_costs = ROUTE_FILE_FORMAT.format(num_routes)
    routes_and_prices = read_routes(route_costs)

    phone_numbers = PHONE_FILE_FORMAT.format(num_phones)
    phone_numbers_list = read_phone_numbers(phone_numbers, 3)

    file_read_time = time() - start_time
    print(f"Time to read 2 files: {file_read_time}")
    start_time = time()

    # Step 2: build trie with routes and costs
    tree = build_trie_with_routes(routes_and_prices)

    build_trie_time = time() - start_time
    print(f"Time to build trie: {build_trie_time}")
    start_time = time()

    

    # Step 3: find call costs with trie
    call_costs = find_call_costs_with_trie(tree, phone_numbers_list)
    
    search_trie = time() - start_time
    print(f"Time to search trie: {search_trie}")
    start_time = time()


    # Step 4: output results to a file
    save_call_costs_to_file(call_costs)
    save_call_cost_time = time() - start_time
    print(f"Time to save call cost time into file: {save_call_cost_time}")
    # start_time = time()

    overall_time = (file_read_time + build_trie_time + search_trie + save_call_cost_time)

    print(f'OverAll_time: {overall_time}')
    

if __name__ == "__main__":
    
    # scenario 2
    # print(RUNTIME_SEPARATOR_FORMAT.format("2"))
    runtime_scen_2 = "======================================== Scenario 2 ========================================"
    print(runtime_scen_2)
    call_costs(106000, 1000) # average search time => 0.00008511543273925781
    

    ## scenario 3
    # runtime_scen_3 = "======================================== Scenario 3 ========================================"
    # print(runtime_scen_3)
    # call_costs(10000000, 10000)  # average search time => 0.0000629425048828125









'''
Optimization Notes:
    Want to create an array of lenth 2 with routing number and its price, then load it into the Trie Tree
    - This means reassigning the added array for each [route, cost] in the file that's being read in

    - While reading the file read as dictionary it might improve the run time.
    and you dont have to validate the price and add smallest one

'''



'''
Runtime Example:

======================================== Scenario 2 ========================================
106680
Time to read 2 files: 0.14192819595336914
Time to build trie: 1.4554429054260254
Time to search trie: 2.2172927856445312e-05
Time to save call cost time into file: 0.0008361339569091797
OverAll_time: 1.5982294082641602

======================================== Scenario 3 ========================================
9996000
Time to read 2 files: 17.282543182373047
Time to build trie: 115.71394801139832
Time to search trie: 6.29425048828125e-05
Time to save call cost time into file: 0.0033838748931884766
OverAll_time: 132.99993801116943
'''
