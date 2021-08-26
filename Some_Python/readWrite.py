# Read all the contents of file
# Read n number of characters by passing parameter
# print(file.read(1))
# Read one single line at a time readLine()
# print(file.readline())

#Print line by line using readLine method

# file = open('test.txt')
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()


# Read the file and store all the lines in list
# reverse the list
# write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    rev = reversed(content)
    with open('test.txt', 'w') as writer:
        for line in rev:
            writer.write(line)