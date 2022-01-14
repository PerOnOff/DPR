def funkcija(file):
    num_lines = sum(1 for line in open(file))
    print(num_lines)

