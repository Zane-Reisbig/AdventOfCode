class FileLoader:
  mainFile = None
  testFile = None
  subDirAppend = None
  
  def __init__(self, main=None, test=None, appendCWD=False, subDirAppend=""):
    self.subDirAppend = subDirAppend
    
    if main == None: 
      self.mainFile = self.openFile("input.txt", True)
    else:
      self.mainFile = self.openFile(main, appendCWD)
      
    if test == None:
      self.testFile = self.openFile("test_input.txt", True)
    else:
      self.testFile = self.openFile(test, appendCWD)
  
  def openFile(self, fileName, appendCWD):
    if appendCWD:
      import os
      with open(f"{os.getcwd()}\\{self.subDirAppend}\\{fileName}", 'r') as f:
        return f.readlines()

    else:
      with open(f"{fileName}", 'r') as f:
        return f.readlines()



class DiceBag:

  def __init__(self, inputString):
    self.dice = []
    self.gameId = None
    self.tokens = inputString.split(":")
    self.gameId = int(self.tokens[0][len("Game "):])

    self.highRed   = 0
    self.highGreen = 0
    self.highBlue  = 0
    
    self.lowRed   = 999
    self.lowGreen = 999
    self.lowBlue  = 999

    self.currentHandRole = {}
    self.brokenDownRolls = [self.rolls.strip().split(", ") for self.rolls in self.tokens[1].split(";")]
    for self.item in self.brokenDownRolls:
      for self.roll in self.item:
        self.currentHandRole.update({self.roll.split(" ")[1]: int(self.roll.split(" ")[0])})

      self.dice.append(self.currentHandRole)
      self.currentHandRole = {}
    
    
    for self.item in self.dice:
      if 'red' in self.item:
        self.highRed = self.item['red'] if self.item['red'] > self.highRed else self.highRed
        self.lowRed = self.item['red'] if self.item['red'] < self.lowRed else self.lowRed

      if 'green' in self.item:
        self.highGreen = self.item['green'] if self.item['green'] > self.highGreen else self.highGreen
        self.lowGreen = self.item['green'] if self.item['green'] < self.lowGreen else self.lowGreen

      if 'blue' in self.item:
        self.highBlue = self.item['blue'] if self.item['blue'] > self.highBlue else self.highBlue
        self.lowBlue = self.item['blue'] if self.item['blue'] < self.lowBlue else self.lowBlue
    
def main():
  isDev = False
  input = FileLoader(subDirAppend="Day2")

  if isDev:
    input = input.testFile
  else:
    input = input.mainFile
  
  ptOne = part_one(input)
  print(ptOne)
  
  ptTwo = part_two(input)
  print(ptTwo)
    

def part_one(input):
  games = []
  for line in input:
    games.append(DiceBag(line))

  SOT = {'red': 12, 'green': 13, 'blue': 14}
  qualifiedGames = []

  isQualifiedGame = True
  item: DiceBag
  for item in games:
    if item.highRed > SOT['red']:
      isQualifiedGame = False
    
    if item.highGreen > SOT['green']:
      isQualifiedGame = False
    
    if item.highBlue > SOT['blue']:
      isQualifiedGame = False
    
    if isQualifiedGame:
      qualifiedGames.append(item.gameId)
    
    isQualifiedGame = True
  
  return sum(qualifiedGames)

def part_two(input):
  outTotal = []
  for line in input:
    outTotal.append(DiceBag(line))

  powerTotal = []
  item: DiceBag
  for item in outTotal:
    powerTotal.append(item.highBlue * item.highGreen * item.highRed)
  
  return sum(powerTotal)
  

main()
  
  
      