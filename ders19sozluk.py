sozluk = {"Python": "Güzel bir dil","Php":"Script Dili"}
print(sozluk["Python"])
for i in sozluk.items():
    print(i)
for i in sozluk.items():
    print(i[0] + " "+ i[1])

for i,j in sozluk.items():
    print(i+ " " + j)