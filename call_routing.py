# reading the file
from trie_tree import TrieTree


def reading_phone_numbers(file_name):
    '''
    Reading the phone numbers  from the text file and return
    list of phone numbers
    '''
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


def load_routes(routes_and_prices):
    '''
    Load the routes from list of list into trie tree
    '''
    route_tree = TrieTree()

    for pair in routes_and_prices:
        route = pair[0]
        price = float(pair[1])
        route_tree.add(route, price)

    phone_numbers_100 = "project/data/phone-numbers-100.txt"
    phone_numbers_1000 = "project/data/phone-numbers-1000.txt"
    phone_numbers_3 = "project/data/phone-numbers-3.txt"
    phone_numbers_1000 = "project/data/phone-numbers-1000.txt"
    phone_numbers_10k = "project/data/phone-numbers-10000.txt"
    list_of_phone_numbers = reading_phone_numbers(phone_numbers_10k)

    with open('call_costs/call-costs-{}.txt'.format(len(list_of_phone_numbers)), 'w') as file:
        for phone_number in list_of_phone_numbers:
            cost = route_tree.search(str(phone_number))
            # print("phone#:", phone_number)
            # print("cost:", cost)
            file.write('+{}, {}\n'.format(phone_number, cost))


    print("route_tree: ", route_tree.size)
    phone = '34747997'  #0.26
    cost = route_tree.search(phone)
    print("cost: ", cost)
    return route_tree.size


def write_costs(list_of_phone_numbers, route_tree):
    pass
    # with open('call-costs{}.txt'.format(len(list_of_phone_numbers)), 'w') as file:
    #     for phone_number in list_of_phone_numbers:
    #         cost = route_tree.search(phone_number)
    #         file.write('{}, {}'.format(phone_number, cost))


def call_costs():
    """Return a price for each phone number"""
    route_costs_100 = "project/data/route-costs-100.txt"
    route_costs_35000 = "project/data/route-costs-35000.txt"
    route_costs_100k = "project/data/route-costs-106000.txt"
    route_costs_1mln = "project/data/route-costs-1000000.txt"
    route_costs_10mln = "project/data/route-costs-10000000.txt"
    route_costs_4 = "project/data/route-costs-4.txt"

    routes_and_prices = read_routes(route_costs_10mln)
    route_tree_size = load_routes(routes_and_prices)



    return route_tree_size

    

if __name__ == "__main__":
    call_costs()



'''
Optimization Notes:
Want to create an array of lenth 2 with routing number and its price, then load it into the Trie Tree
    - This means reassigning the added array for each [route, cost] in the file that's being read in
'''
