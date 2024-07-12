#!/bin/python
# -*- coding: utf-8 -*-

import copy
import scipy as sp
import numpy as np

"""
Nous avons un nombre de places disponibles de professeurs par département.
Chaque professeur possède 3 choix de départements classés par ordre de préférence.
Ces professeurs proviennent de 3 concours différents : concours externe, concours interne et 3ème concours. 
Un professeur ne peut pas avoir effectué deux concours distincts. 
Les professeurs de chaque concours sont classés entre eux. 
Il n'existe cependant pas de classement pour l'ensemble des professeurs.
Le problème consiste à affecter un département pour chaque professeurs (ou aucun si toutes les places sont prises). 
Nous souhaitons que les professeurs les mieux classés dans leur concours aient une prédominance de choix que les professeurs les moins bien classés dans ce même concours.
"""

def glouton(interne, externe, troisieme, capacites):
    """
    Cette fonction permet de résoudre le problème de l'affectation des professeurs à l'aide d'un algorithme glouton.
    
    Args:
        interne (list): Liste contenant l'id des candidats ayant passé le concours interne ainsi que leur classement et leurs voeux classés par ordre de préférence.
        externe (list): Liste contenant l'id des candidats ayant passé le concours externe ainsi que leur classement et leurs voeux classés par ordre de préférence.
        troisieme (list): Liste contenant l'id des candidats ayant passé le concours du 3ème concours ainsi que leur classement et leurs voeux classés par ordre de préférence.
        capacites (dict): Dictionnaire contenant le nombre de places disponibles par département et par concours.

    Returns:
        dict: Dictionnaire contenant l'id des professeurs et le département qui leur a été affecté.

    Examples:
        >>> interne = [[1, 1, 'A', 'B', 'C'], [2, 2, 'B', 'A', 'C'], [3, 3, 'A', 'B', 'C']]
        >>> externe = [[4, 1, 'A', 'B', 'C'], [5, 2, 'B', 'A', 'C'], [6, 3, 'A', 'B', 'C']]
        >>> troisieme = [[7, 1, 'A', 'B', 'C'], [8, 2, 'B', 'A', 'C'], [9, 3, 'A', 'B', 'C']]
        >>> departements = ['A', 'B', 'C']
        >>> capacites = {'département': {'A': 160, 'B': 78, 'C': 262}, 'concours': {'externe': 331, 'interne': 1, 'troisieme': 2}}
        >>> glouton(interne, externe, troisieme, departements, capacites)
        {1: 'A', 2: 'B', 3: 'C', 4: 'A', 5: 'B', 6: 'C', 7: 'A', 8: 'B', 9: 'C'}
        """
    result = {}

    # trie des candidats par concours
    interne_trie = copy.deepcopy(interne)
    interne_trie[interne_trie[:, 1].argsort()]
    externe_trie = copy.deepcopy(externe)
    externe_trie[externe_trie[:, 1].argsort()]
    troisieme_trie = copy.deepcopy(troisieme)
    troisieme_trie[troisieme_trie[:, 1].argsort()]

    # copie des capacités
    capacites_courrante = copy.deepcopy(capacites)

    # affectation des candidats
    for i in range(max(len(interne_trie), len(externe_trie), len(troisieme_trie))):
        if i < len(interne_trie):
            for j in range(3):
                if capacites_courrante['département'][interne_trie[i][j + 2]] > 0:
                    result[interne_trie[i][0]] = interne_trie[i][j + 2]
                    capacites_courrante['département'][interne_trie[i][j + 2]] -= 1
                    break
                else:
                    result[interne_trie[i][0]] = 'None'
        if i < len(externe_trie):
            for j in range(3):
                if capacites_courrante['département'][externe_trie[i][j + 2]] > 0:
                    result[externe_trie[i][0]] = externe_trie[i][j + 2]
                    capacites_courrante['département'][externe_trie[i][j + 2]] -= 1
                    break
                else:
                    result[externe_trie[i][0]] = 'None'
        if i < len(troisieme_trie):
            for j in range(3):
                if capacites_courrante['département'][troisieme_trie[i][j + 2]] > 0:
                    result[troisieme_trie[i][0]] = troisieme_trie[i][j + 2]
                    capacites_courrante['département'][troisieme_trie[i][j + 2]] -= 1
                    break
                else:
                    result[troisieme_trie[i][0]] = 'None'
        
    return result

def evolution(interne, externe, troisieme, capacites):
    """
    Cette fonction permet de résoudre le problème de l'affectation des professeurs à l'aide d'un algorithme évolutionniste.
    Ce dernier utilise un algorithme génétique pour résoudre le problème issu de la bibliothèque scipy.
    
    Args:
        interne (list): Liste contenant l'id des candidats ayant passé le concours interne ainsi que leur classement et leurs voeux classés par ordre de préférence.
        externe (list): Liste contenant l'id des candidats ayant passé le concours externe ainsi que leur classement et leurs voeux classés par ordre de préférence.
        troisieme (list): Liste contenant l'id des candidats ayant passé le concours du 3ème concours ainsi que leur classement et leurs voeux classés par ordre de préférence.
        capacites (dict): Dictionnaire contenant le nombre de places disponibles par département et par concours.

    Returns:
        dict: Dictionnaire contenant l'id des professeurs et le département qui leur a été affecté.

    Examples:
        >>> interne = [[1, 1, 'A', 'B', 'C'], [2, 2, 'B', 'A', 'C'], [3, 3, 'A', 'B', 'C']]
        >>> externe = [[4, 1, 'A', 'B', 'C'], [5, 2, 'B', 'A', 'C'], [6, 3, 'A', 'B', 'C']]
        >>> troisieme = [[7, 1, 'A', 'B', 'C'], [8, 2, 'B', 'A', 'C'], [9, 3, 'A', 'B', 'C']]
        >>> departements = ['A', 'B', 'C']
        >>> capacites = {'département': {'A': 160, 'B': 78, 'C': 262}, 'concours': {'externe': 331, 'interne': 1, 'troisieme': 2}}
        >>> evolution(interne, externe, troisieme, departements, capacites)
        {1: 'A', 2: 'B', 3: 'C', 4: 'A', 5: 'B', 6: 'C', 7: 'A', 8: 'B', 9: 'C'}
        """
    result = {}

    # Initialisation des variables
    departements = capacites['département']
    concours = capacites['concours']
    voeux = {prof[0]: prof[2:] for prof in np.concatenate((interne, externe, troisieme))}
    classements = {prof[0]: prof[1] for prof in np.concatenate((interne, externe, troisieme))}
    professeurs = list(voeux.keys())
    nb_departements = len(departements)
    nb_professeurs = len(professeurs)
    nb_generations = 100
    nb_population = 100
    nb_mutation = 0.5
    nb_crossover = 0.5
    bounds = [(0, nb_departements - 1) for _ in range(nb_professeurs)]

    def aptitude(affectations, voeux, classements, departments):
        """
        Cette fonction permet de calculer l'aptitude d'une solution.
        L'aptitude est calculée en fonction de la satisfaction des professeurs par rapport à leur affectation.
        De plus, un professeur mieux classé dans son concours doit avoir une prédominance de choix par rapport à un professeur moins bien classé dans ce même concours.

        Args:
            affectations (dict): Dictionnaire contenant l'id des professeurs et le département qui leur a été affecté.
            voeu (dict): Dictionnaire contenant l'id des professeurs et leurs voeux classés par ordre de préférence.
            classements (dict): Dictionnaire contenant l'id des professeurs et leur classement par concours.

        Returns:
            float: L'aptitude de la solution.
        """
        score = 0
        dept_assignments = {dept["id"]: 0 for dept in departments}

        # Liste pour vérifier les affectations par ordre de rang
        ranked_assignments = []

        for prof_id, dept in affectations.items():
            if dept != -1:
                if dept_assignments[dept] < next(d["capacity"] for d in departments if d["id"] == dept):
                    rank = classements[prof_id]
                    pref_index = voeux[prof_id].index(dept) if dept in voeux[prof_id] else len(voeux[prof_id])
                    score += (pref_index + 1) * rank
                    dept_assignments[dept] += 1
                    ranked_assignments.append((rank, pref_index))
                else:
                    score += len(classements) * (len(voeux[prof_id]) + 1) * rank

        # Trier les affectations par rang de professeur
        ranked_assignments.sort(key=lambda x: x[0])

        # Vérifier les préférences pour ajouter des pénalités si nécessaire
        for j in range(len(ranked_assignments) - 1):
            current_rank, current_pref_index = ranked_assignments[j]
            next_rank, next_pref_index = ranked_assignments[j + 1]
            if current_rank < next_rank and current_pref_index > next_pref_index:
                penalty = (current_pref_index - next_pref_index) * (next_rank - current_rank)
                score += penalty

        return score

    result = sp.optimize.differential_evolution(aptitude, bounds, args=(voeux, classements, departements), maxiter=nb_generations, popsize=nb_population, mutation=nb_mutation, recombination=nb_crossover)