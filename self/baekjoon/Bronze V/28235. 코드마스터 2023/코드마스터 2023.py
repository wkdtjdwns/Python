def switch(key):
  str = {"SONGDO" : "HIGHSCHOOL", "CODE": "MASTER", "2023" : "0611", "ALGORITHM" : "CONTEST"}.get(key)
  print(str)

str = input()
switch(str)
