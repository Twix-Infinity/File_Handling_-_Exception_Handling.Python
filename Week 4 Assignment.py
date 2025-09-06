file = open("Random_File.txt", "r")
with open("Random_File.txt", "r") as file: data = file.read() 
print(data)

with open("Edited_File.txt", "a") as new_file:
    new_file.write("The snow-covered mountains stood majestically against the clear, blue sky.\n")
    output = "Text written to new file successfully."
print(output)

Requested_File = input("Enter file name: ")
try:
    with open(Requested_File, "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found.")