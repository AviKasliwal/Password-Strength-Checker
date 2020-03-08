fin = open("./Data/data_krish.csv", 'r')
fout = open("./Data/tsvFiles/data_krish.tsv", 'wt')

count = 0

fout.write('Password\tStrength\n')

for line in fin:
    if count == 0:
        count += 1
        continue
    
    if line[-7] in ['1', '2', '0']:
        newLine = line[:-8] + "\t" + line[-7] + '\n'
        fout.write(newLine)

fin.close()
fout.close()