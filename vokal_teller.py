import matplotlib.pyplot as plt

f = open("input.txt", "r")
f_out = open("output.txt", "w")

file_content = f.read()

#--------------------------------------------------

vokal_array = ['a', 'e', 'i', 'o', 'u', 'y']
n = len(vokal_array)
telle_array = [0]*n
for i in file_content:
    index = 0
    for k in vokal_array:
        if (i.lower() == k):
            telle_array[index] = telle_array[index] +1
        index = index + 1
index = 0 
for k in vokal_array: 
    f_out.write(k)
    f_out.write(": ")
    f_out.write(str(telle_array[index]))
    f_out.write("\n")
    index = index + 1


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
vokaler = vokal_array
antall_vokaler = telle_array
ax.bar(vokaler,antall_vokaler)
plt.show()


#----------------------------------------------------

f_out.write("\n")
f_out.write("\n")
f_out.write("\n")

#----------------------------------------------------

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
count_y = 0
count_all = 0
for i in file_content: 
    if (i == 'a') or (i == 'A'):
        count_a = count_a + 1;
    if (i == 'e') or (i == 'E'):
        count_e = count_e +1;
    if (i == 'i') or (i == 'I'):
        count_i = count_i +1;
    if (i == 'o') or (i == 'O'):
        count_o = count_o +1;
    if (i == 'u') or (i == 'U'):
        count_u = count_u +1;
    if (i == 'y') or (i == 'Y'):
        count_y = count_y +1;
count_all = count_all + count_a + count_e + count_i + count_o + count_u + count_y
f_out.write("A or a: ")
f_out.write(str(count_a))
f_out.write("\n")
f_out.write("E or e: ")
f_out.write(str(count_e))
f_out.write("\n")
f_out.write("I or i: ")
f_out.write(str(count_i))
f_out.write("\n")
f_out.write("O or o: ")
f_out.write(str(count_o))
f_out.write("\n")
f_out.write("U or u: ")
f_out.write(str(count_u))
f_out.write("\n")
f_out.write("Y or y: ")
f_out.write(str(count_y))
f_out.write("\n")
f_out.write("all: ")
f_out.write(str(count_all))

#------------------------------------------------------------------------

f.close()
f_out.close()

