#!/bin/python
# -*- coding: utf-8 -*-

def satisfaction(affectations, voeux):
    """
    Cette fonction permet de calculer la satisfaction des professeurs par rapport à leur affectation.
    Nous considérons qu'un professeur est satisfait (1.0) si le département qui lui a été affecté est son premier choix.
    Nous considérons qu'un professeur est partialement (0.25) si le département qui lui a été affecté est son deuxième choix.
    Nous considérons qu'un professeur est insatisfait (0.0) si le département qui lui a été affecté est son troisième choix.
    
    Args:
        affectations (dict): Dictionnaire contenant l'id des professeurs et le département qui leur a été affecté.
        voeux (dict): Dictionnaire contenant l'id des professeurs et leurs voeux classés par ordre de préférence.
    
    Returns:
        float: Le taux de satisfaction des professeurs.
    
    Examples:
        >>> affectations = {1: 'A', 2: 'B', 3: 'C', 4: 'A', 5: 'B', 6: 'C', 7: 'A', 8: 'B', 9: 'C'}
        >>> voeux = {1: ['A', 'B', 'C'], 2: ['B', 'A', 'C'], 3: ['A', 'B', 'C'], 4: ['A', 'B', 'C'], 5: ['B', 'A', 'C'], 6: ['A', 'B', 'C'], 7: ['A', 'B', 'C'], 8: ['B', 'A', 'C'], 9: ['A', 'B', '                
        >>> satisfaction(affectations, voeux)
        1.0
    """
    satisfaction = 0.0
    for professeur, departement in affectations.items():
        if departement == voeux[professeur][0]:
            satisfaction += 1.0
        elif departement == voeux[professeur][1]:
            satisfaction += 0.25
    return satisfaction / len(affectations)