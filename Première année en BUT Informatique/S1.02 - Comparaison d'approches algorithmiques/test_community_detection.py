from community_detection import *

 
def test_create_network():
    assert create_network([]) == {}
    
    assert create_network(["Alice","Bob","Alice","Dominique","Bob","Charlie","Bob","Dominique"]) == {"Alice" : ["Bob", "Dominique"],"Bob" : ["Alice", "Charlie", "Dominique"],"Charlie" : ["Bob"],"Dominique" : ["Alice", "Bob"]}
    
    assert create_network(["Muriel","Yasmine","Muriel","Joël", "Yasmine", "Joël","Yasmine","Thomas","Joël","Nassim","Joël","Andrea","Joël", "Ali","Nassim",
        "Andrea","Nassim","Ali","Andrea", "Ali","Thomas","Daria","Thomas", "Carole","Daria","Carole","Thierry", "Axel", "Leo","Thierry","Axel","Leo","Valentin", "Leo","Valentin","Andrea"]) == { 
    
        'Muriel': ['Yasmine', 'Joël'],'Yasmine': ['Muriel', 'Joël', 'Thomas'],'Joël': ['Muriel', 'Yasmine', 'Nassim', 'Andrea', 'Ali'],'Thomas': ['Yasmine', 'Daria', 'Carole'],'Nassim': ['Joël', 'Andrea', 'Ali'],
        'Andrea': ['Joël', 'Nassim', 'Ali', 'Valentin'],'Ali': ['Joël', 'Nassim', 'Andrea'],'Daria': ['Thomas', 'Carole'],
        'Carole': ['Thomas', 'Daria'],'Thierry': ['Axel', 'Leo'],'Axel': ['Thierry', 'Leo'],'Leo': ['Thierry', 'Axel', 'Valentin'],'Valentin': ['Leo', 'Andrea']}
        
    print("Test de la fonction create_network : OK ")

network={"Alice" : ["Bob", "Dominique"],"Bob" : ["Alice", "Charlie", "Dominique"],"Charlie" : ["Bob"],"Dominique" : ["Alice", "Bob"]}

def test_get_people():
    assert get_people(network)== ["Alice", "Bob", "Charlie", "Dominique"]
    assert get_people({'Alice': ['Bob', 'Charlie'], 'Bob': ['Alice', 'Denis'],'Charlie': ['Alice'], 'Denis': ['Bob']})== ["Alice", "Bob", 'Charlie', "Denis"]
    assert get_people({})== []
    print("Test de la fonction get_people : OK ")

test_get_people()


def test_are_friend():
    assert are_friends(network, 'Charlie', 'Dominique')==False
    assert are_friends(network, 'Alice', 'Dominique')==True
    assert are_friends(network, 'Alice', 'JeanFort')==False
    assert are_friends(network, 'Charlie', 'Bob')==True
    print( "Test de la fonction are_friends : OK ")

test_are_friend()


def test_all_his_friends():
    assert all_his_friends(network, 'Alice', ["Bob", "Dominique"])==True
    assert all_his_friends(network, 'Bob', ["Alice", "Charlie", "Dominique"])==True
    assert all_his_friends(network, 'Alice', ["Bob", "Charlie"])==False
    assert all_his_friends (network,  'Charlie', ["Bob", "Alice"])==False
    print("Test de la fonction all_his_friends : OK ")


test_all_his_friends()



def test_is_a_community():
    assert is_a_community(network, ["Alice", "Charlie"])==False
    assert is_a_community(network, ["Alice", "Bob", "Dominique"])==True
    assert is_a_community(network, ["Dominique", "Bob", "Charlie"])==False
    print("Test de la fonction is_a_community : OK ")

test_is_a_community()


def test_find_community():
    assert find_community(network, ["Alice", "Bob", "Charlie", "Dominique"])==["Alice", "Bob", "Dominique"]
    assert find_community(network, ["Charlie", "Alice", "Bob", "Dominique"])==["Charlie", "Bob"]
    assert find_community(network,["Charlie", "Alice", "Dominique"])==["Charlie"]
    print("Test de la fonction find_community : OK ")


test_find_community()



def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity(network, ["Bob", "Charlie", "Dominique"])==["Bob", "Dominique", "Charlie"]
    assert order_by_decreasing_popularity(network, ["Charlie", "Alice"])==["Alice", "Charlie"]
    assert order_by_decreasing_popularity(network, ["Bob", "Charlie", "Alice"])==["Bob", "Alice", "Charlie"]
    print( "Test de la fonction order_by_decreasing_popularity : OK")

test_order_by_decreasing_popularity()


def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity(network)==["Bob", "Alice", "Dominique"]
    assert find_community_by_decreasing_popularity({'Alice': ['Bob', 'Charlie'], 'Bob': ['Alice', 'Denis'],'Charlie': ['Alice'], 'Denis': ['Bob']})==["Alice", "Bob"]
    assert find_community_by_decreasing_popularity({'Bob': ['Denis'], 'Denis': ['Bob']})==["Bob","Denis"]
    print("Test de la fonction find_community_by_decreasing_popularity : OK ")

test_find_community_by_decreasing_popularity()


def test_find_community_from_person():
    assert find_community_from_person(network, 'Alice')==["Alice", "Bob", "Dominique"]
    assert find_community_from_person(network, 'Charlie')==["Charlie","Bob"]
    assert find_community_from_person(network, 'Bob')==["Bob","Alice","Dominique"]
    print("Test de la fonction find_community_from_person : OK ")


test_find_community_from_person()

def test_find_max_community():
    assert find_max_community(network)==['Dominique', 'Bob', 'Alice']
    assert find_max_community({'Alice': ['Bob', 'Charlie'], 'Bob': ['Alice', 'Denis'],'Charlie': ['Alice'], 'Denis': ['Bob']})==['Denis', 'Bob']
    print("Test de la fonction find_max_community : OK ")

test_find_max_community()