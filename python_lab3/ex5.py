def validate_dict(valid_rules, dictionary):
    for rule in valid_rules:
        if rule[0] in [elem[0] for elem in dictionary.items()]:
            if rule[1] in dictionary[rule[0]]:
                if dictionary[rule[0]].index(rule[1]) > 0:
                    return False
            else:
                return False
            if rule[2] in dictionary[rule[0]]:
                if dictionary[rule[0]].index(rule[2]) < 1 and dictionary[
                    rule[0]].index(rule[2]) + len(rule[2]) > len(dictionary[rule[0]]):
                    return False
            else:
                return False
            if rule[3] in dictionary[rule[0]]:
                if dictionary[rule[0]].index(rule[3]) + len(
                        rule[3]) > len(dictionary[rule[0]]):
                    return False
            else:
                return False
        else:
            return False
    return True


print(validate_dict({("key1", "", "inside", ""), ("key3", "start", "middle", "winter")},
                    dictionary={"key1": "come inside, it's too cold out", "key3": "this is not valid"}))
