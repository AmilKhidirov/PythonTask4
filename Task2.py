
with open("file2.txt", "r") as f:
    elements = f.readlines()
    first_element_index = 0
    last_element_index = len(elements) - 1

    print(first_element_index)
    print(last_element_index)

