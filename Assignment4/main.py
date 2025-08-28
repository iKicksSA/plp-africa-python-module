#  opening week3_assign & store each line inside lines
with open("week3_assignment.py", "r") as f:
  lines = f.readlines()
  modified_version = open("week3_assignment_modified.py", "a+")

  # copying the content of week3_assign from "lines" and modifi into a new file "week3...modified"
  for line in lines:

   modified_version.write(line)
   modified_version.write('*\n')
   

  modified_version.close()
  f.close()

  print("File modified successfully!")
  testing = open("week3_assignment_modified.py", "r")
  print(testing.read())
  testing.close()
  
  


file_name = input("Enter a filename to search: ")

try:
  with open(file_name, "r") as f:
    content = f.read()
    print(content)

except FileNotFoundError:
  print("The file you searched doesn't exist.")

except PermissionError:
  print("Permissions denied")

except Exception:
  print("An unexpected errot has occurred.")




