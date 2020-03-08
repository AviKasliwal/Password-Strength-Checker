fin = open("./Data/common.txt", "r")
fout = open("./Data/tsvFiles/common.tsv", "wt")

fout.write('Password\tStrength\n')

for line in fin:
    line = line[ : -1] + '\t 0\n' # slicing to remove \n of last line
    fout.write(line)
fin.close()
fout.close()
