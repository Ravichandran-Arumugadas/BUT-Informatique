"""ARUMUGADAS Ravichandran
Santhirarasa Abinash
Tlaloc
"""
##############
# SAE S01.01 #
##############

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##############
# SAE S01.02 #
##############

def create_network(list_of_friends):
    """
    
    Cette fonction create_network retourne un dictionnaire dont les clés sont de les prénoms du 
    réseau et les valeurs, les prénoms de leurs amis.

    :param list_of_friends: le tableau caractérisant les intéractions entre les personnes 
    :type list_of_friends: list
    :return: un dictionnaire(réseau) dont les clés sont les prénoms et les valeurs le tableau de leurs amis

    """
    
    reseau = {}     #creation d'un dictionnaire vide
    i = 0   #initialisation de la boucle
    while i < len(list_of_friends):  #on parcourt tous les éléments du tableau list_of_friends
        person1 = list_of_friends[i]
                                        #on affecte chaque personne du réseau dans une variable
        person2 = list_of_friends[i+1]
        if person1 in reseau:
            reseau[person1].append(person2)
        else:
            reseau[person1] = [person2]
        if person2 in reseau:
            reseau[person2].append(person1)
        else:
            reseau[person2] = [person1]
        i += 2
    return reseau


def get_people(network):
   
    """
    Cette fonction get_people retourne la liste des personnes de ce réseau dans un tableau

    :param network: un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne
    :type network: list
    :return: la liste des personnes de ce réseau dans un tableau
    """
    
    return list(network)  #on retourne les clés du dictionnaire pour connaître la liste des personnes du réseau



def are_friends(network,person1, person2):
    
    """
    Cette fonction are_friends retourne True si les deux personnes sont amies, et False sinon

    :param network: un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne
    :type network: list
    :param person1: le prénom de la personne dont on cherche le lien d'amitié avec l'autre personne
    :type person1: str
    :param person2: le prénom de la personne dont on cherche le lien d'amitié avec l'autre personne
    :type person2: str
    :return: True si les deux sont amies sinon False

    """
    if person1 in network and person2 in network:   #condition, on regarde si les deux personnes sont dans le reseau
        if person2 in network[person1]:     #condition, si la personne2 se trouve dans la liste des amis de la personne1
            return True
    return  False


def all_his_friends(network, person, group):
    """
    Cette fonction all_his_friends retourne True si la personne est amie avec toutes les personnes du groupe, et False sinon

    :param network: un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne
    :type network: list
    :param person: la prénom de la personne dont on regarde le lien d'amitié avec le groupe de personnes
    :type param: str
    :param group: un tableau de personnes
    :type group: list
    :return: retourne True si la personne est amie avec toutes les personnes sinon False

    """
    i=0     #initialisation de la boucle
    a=network[person]   #on affecte dans une variable la liste des amis  de la personne
    while i<len(group):     #on parcourt tous les éléments du group
        if group[i] in a:   #condition, on regarde l'indice i du tableau group se trouve dans la liste d'amis de la personne  
            i=i+1                                 
        else:
            return False
    return True

def is_a_community(network, group):

    """
    Cette fonction is_a_community retourne True si ce groupe est une communauté, et False sinon

    :param network: un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne
    :type network: list
    :param group: un tableau de personnes
    :type group: list
    :return: retourne True si ce groupe est une communauté, et False sinon

    """   
    i = 0    #initialisation de la boucle
    while i < len(group):   #on parcourt tous les éléments du group
        j = 0
        while j < len(group) and group[i] != group[j]:   #il s'agit de ne pas comparer la même personne quand on parcourt le même groupe  
            if not are_friends(network, group[i], group[j]):
                return False
            j+=1
        i+=1
    return True



def find_community(network, group):
    
    """
    Cette fonction find_community retourne une communauté en fontion de l'heuristique de construction de communauté maximale

    :param network: un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne
    :type network: list
    :param group: un tableau de personnes
    :list group: list
    :return:  retourne une communauté en fonction de l'heuristique

    """    

    commmunaute = []    #creation d'un tableau
    commmunaute.append(group[0])    #on ajoute le premier élément dans le tableau communauté
    i=1
    while i<len(group):     #on parcourt tous les éléments du groupe
        a = all_his_friends(network,group[i],commmunaute)  #on affecte dans une variable une fonction pour faire appel à celle-ci
        if a == True:       #contidion, on regarde si chaque personne du groupe est amie avec la première personne du groupe
            commmunaute.append(group[i])
        i=i+1
    return commmunaute 






def order_by_decreasing_popularity(network, group):
    """
    Cette fonction order_by_decreasing_popularity doit trier l'ensemble des personnes du réseau selon l'ordre decroissant de popularité

    :param network: un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne
    :type network: list
    :param group: un tableau de personnes
    :type group: list
    return: retourne le tableau de personnes selon sa popularité
    
    """
    
    i=0     #initialisation de la boucle
    while i<len(group):     #il s'agit d'éffectuer une tri par sélection
        min = i
        j = i+1
        
        #on compare la popularité de chaque personne afin de trier le groupe
        while j<len(group):     
            if len(network[group[min]])<len(network[group[j]]):
                min = j
            j=j+1
  
        tmp = group[i]
        group[i] = group[min]
        group[min] = tmp
        i=i+1

    return group

    

def find_community_by_decreasing_popularity(network):
    """
    Cette fonction find_community_by_decreasing_popularity doit trier l'ensemble des personnes du réseau selon l'ordre décroissant de popularité puis retourner la communauté trouvée en appliquant l'heuristique de construction de communauté maximale
    
    :param network: un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne
    :type network: list
    :return: retourne la communauté trouvée en appliquant l'heuristique de construction de communauté maximale
    """
    
    #on fait appel à des fonctions qui vont permettre de retourner la communauté trouvée en appliquant l'heuristique de construction de communauté maximale
    liste = get_people(network)   
    communaute_heuristique = find_community(network,liste)
    popularite = order_by_decreasing_popularity(network,communaute_heuristique)

    return popularite
    

def find_community_from_person(network, person):
    """
    Cette fonction find_community_from_person retourne une communaute maximale contenant cette personne

    :param network: un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne
    :type network: list
    :param person: la prénom de la personne dont on regarde le lien d'amitié 
    :type person: list
    :return: retourne une communaute maximale contenant cette personne

    """    
    
    community=[]  #création d'un tableau vide
    community.append(person)   #on ajoute la personne dans le tableau 
    pop = order_by_decreasing_popularity(network, network[person])    #on trie les amies de la personne selon la popularité décroissante
    i=0   
    while i <len(pop):
        if all_his_friends(network, pop[i], community):    #on regarde les liens d'amitiés entre la communauté
            community.append(pop[i])
        i=i+1
    return community

def find_max_community(network):
    """
    Cette fonction find_max_community retourne la plus grande communaute trouvée en appliquant l'heuristique de recherche de communauté maximale donnée par `find_community_from_person` pour toutes les personnes du réseau

    :param network: un dictionnaire dont les clés sont les prénoms des personnes et les valeurs des tableaux contenant la liste des amis de la personne
    :type network: list
    :return: retourne la plus grande communaute trouvée

    """    
    
    ls=get_people(network) #on affecte dans un variable une fonction qui donne la liste des personnes du réseau
    maxi = find_community_from_person(network, ls[0])
    i=1
    while i<len(ls):
        if maxi < find_community_from_person(network, ls[i]):    #il s'agit de comparer chaque communauté pour trouver la plus grande 
            maxi =find_community_from_person(network, ls[i])
        i=i+1
    return maxi