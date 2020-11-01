def build_xml_element(tag, content, **key_values):
    string = ""
    string += "<" + tag + " "
    for elem in key_values.items():
        string += elem[0] + "= \"" + elem[1] + "\" "
    string += ">" + content + "</" + tag + ">"
    return string



print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link "))
