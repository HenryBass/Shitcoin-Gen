import random

name = ""

supply = ""

symbol = ""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letters = list(letters)

name_words = ["elon", "musk", "doge", "coin", "shibu", "inu", "mars", "obama", "sussy", "moon"]

funny_num = ["69", "420", "21", "911", "666", "80085"]

for i in range(0, 3):
  name += random.choice(name_words)

for i in range(0, 5):
  supply += random.choice(funny_num)

for i in range(0, 4):
  symbol += str(random.choice(letters))

token = open("template.sol", "r")

script = token.read()

newToken = script.replace("TOKENNAME", name)

newToken = newToken.replace("MAXSUPPLY", supply)

newToken = newToken.replace("SMBL", symbol)


newtoken = open("token.sol", "r+")
newtoken.write(newToken)

token.close()
newtoken.close()