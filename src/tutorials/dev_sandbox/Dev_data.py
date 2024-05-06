if __name__ == "__main__":
    example_list = [1, 2, 3]
    example_list.insert(0, "beginnning of list")
    example_list.append("end of list")
    print(example_list)

    last = example_list[-1]
    print(last)

    print("reverse list {}".format(example_list[::-1]))
    print("remove last reverse list {}".format(example_list[-2::-1]))

    dictio = {0: "0", 1: "1", -1: "1"}
    print(dictio[-1])
