file1 = open("coding_qual_input.txt")
Lines = file1.readlines()

#form dictionary
diction = {}
for line in Lines:
    values = line.split(" ")
    values[0] = int(values[0])
    values[1] = values[1].strip(' \n\t')
    diction[values[0]] = values[1]

#pick last stepssteps
numline = []
step = 1
index = 1
while(index < len(diction)):
    numline.append(index)
    step+=1
    index+=step
    
#take numbers in numline and form message
message = ""
for num in numline:
    message += diction[num] + " "
message = message.strip()
print(message)