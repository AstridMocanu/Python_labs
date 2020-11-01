def domino(mapping):
    new_key = mapping["start"]
    y = []
    y.append(new_key)
    while True:
        if new_key in mapping.keys():
            new_key = mapping[new_key]
            if new_key not in y:
                y.append(new_key)
            else:
                return y

print(domino({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': 'y', 'y': 'start'}))
