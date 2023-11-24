def draw_rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height - 1:
            print('-' * width)
        else:
            # Autres lignes : côtés verticaux
            print('|' + ' ' * (width - 2) + '|')
draw_rectangle(10, 3)
