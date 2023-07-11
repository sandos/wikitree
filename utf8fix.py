#Detect split utf-8 sequences in files, useful for finding where parsing breaks in myheritage GEDCOMs

file = open('mini.ged', encoding='utf-8')

linenr = 1
while True:
    l = file.readline(20000)
    if not l:
        break
    print(f"{linenr} : {l[0:20]}")
    linenr += 1

print("Done")
