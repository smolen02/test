f = open("input.txt", "r")
f_out = open("output.txt", "w")

file_content = f.read()

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
count_y = 0

for i in file_content: 
    if (i == 'a') or (i == 'A'):
        count_a = count_a + 1;
    if (i == 'e') or (i == 'E'):
        count_e = count_e +1;
    if (i == 'i') or (i == 'E'):
        count_i = count_i +1;
    if (i == 'o') or (i == 'O'):
        count_o = count_o +1;
    if (i == 'u') or (i == 'U'):
        count_u = count_u +1;
    if (i == 'y') or (i == 'Y'):
        count_y = count_y +1;

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

f.close()
f_out.close()

