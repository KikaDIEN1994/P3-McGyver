def read_maze(file):
  print(f"Opening file : {file}")
  with open(file) as f:
    for line in f:
      print(line.strip())