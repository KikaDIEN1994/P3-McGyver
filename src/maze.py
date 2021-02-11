def read_maze(file):
    print(f"Opening file : {file}")
    with open(file) as reader:
        # print(reader.readlines())
        for line in reader.readlines():
            line = line.strip()
            print(line)

    # with open(file) as reader:
    #   print(reader.readlines())
    # for line in f:
    #   print(line.strip())
