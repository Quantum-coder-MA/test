def resoudre_jump_game(plateau, chemin_exécute, etats_visites):
    # 1. Test d'objectif : il ne reste plus qu'un seul jeton sur le plateau
    if compter_jetons(plateau) == 1:
        return chemin_exécute  

    # Optimisation (Mémoïsation) : éviter de réexplorer un plateau déjà traité
    cle_plateau = obtenir_empreinte(plateau)
    if cle_plateau in etats_visites:
        return None
    etats_visites.add(cle_plateau)

    # 2. Génération de tous les coups valides depuis la configuration actuelle
    coups_valides = generer_coups_valides(plateau)

    # 3. Exploration recursive des coups
    for coup in coups_valides:
        # Appliquer le saut (déplacer le jeton et supprimer les jetons sautés)
        nouveau_plateau = appliquer_saut(plateau, coup)
        chemin_exécute.append(coup)

        # Appel récursif
        resultat = resoudre_jump_game(nouveau_plateau, chemin_exécute, etats_visites)
        if resultat is not None:
            return resultat  # Solution trouvée, on remonte le résultat

        # BACKTRACK : Annulation du coup si la branche mène à un échec
        chemin_exécute.pop()

    return None  # Échec : aucune solution à partir de cette configuration