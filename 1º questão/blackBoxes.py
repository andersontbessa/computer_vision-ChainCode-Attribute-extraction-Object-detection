#o algorimo blackBoxNormalization vai pegar códigos grande e reduzir para códigos menores;

def Normalize(values,smaller):
    len_values = len(values)
    proportion = len_values/smaller

    selected_values = []

    next_idx = 0
    rest = 0

    while next_idx < len_values:
        selected_values.append(values[next_idx])
        rest = (rest +proportion) % 1
        next_idx = int((next_idx + rest + proportion)//1)
    return selected_values
