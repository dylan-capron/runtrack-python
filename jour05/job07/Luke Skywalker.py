def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            prochain_multiple_de_5 = (note // 5 + 1) * 5
            if prochain_multiple_de_5 - note < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(note)
    return notes_arrondies
liste_notes = [83, 62, 45, 39, 92]
notes_arrondies = arrondir_notes(liste_notes)
print("Notes brutes :", liste_notes)
print("Notes arrondies  :", notes_arrondies)
