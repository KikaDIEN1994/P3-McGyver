with open('./src/assets/level.txt') as f:
    line = f.readline()
    while line:
        #print("Line : {}".format(line.strip()))
        print("---", line.strip(), "---")
        i = 0
        for c in line:
            print(f"[{i}] '{c}'")
            i += 1
        line = f.readline()
    f.close()