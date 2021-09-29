def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1



path = input("Please give a path to a file :")
name_exit = input("Please entre the name of the exit file")


file_len = file_len(path)
file_DATA = open(path, "r")
file_CSV = open (name_exit+".csv", "w")

for i in file_len:
	line = file_DATA.read(i)
	line.replace(" " , ";")
	file_DATA.writelines(line)

file_DATA.close()
file_CSV.close()

