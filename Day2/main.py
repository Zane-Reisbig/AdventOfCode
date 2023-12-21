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

    # Me when people say day 2 is a regex challenge 
    self.tokens = inputString.split(":")
    self.gameId = int(self.tokens[0][len("Game "):])

    self.highRed   = 0
    self.highGreen = 0
    self.highBlue  = 0
    
    # Honestly I really couldn't figure out how to do 
    # int.max cuz it doesn't just work :shrug:
    self.lowRed   = 999
    self.lowGreen = 999
    self.lowBlue  = 999

    self.currentHandRole = {}
    # Me when people say day is something...something see above 
    self.brokenDownRolls = [self.rolls.strip().split(", ") for self.rolls in self.tokens[1].split(";")]
    for self.item in self.brokenDownRolls:
      for self.roll in self.item:
        # After breaking down the string we are left with a grand total to turn into an object
        # - {color: amount}, makes it real easy to mess around with later if they aren't just
        # - floating around in here somewhere
        self.currentHandRole.update({self.roll.split(" ")[1]: int(self.roll.split(" ")[0])})

      self.dice.append(self.currentHandRole)
      self.currentHandRole = {}
    
    
    for self.item in self.dice:
      if 'red' in self.item:
        # Check if high and low is set and change accordingly
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

  # Our puzzle input source of truth
  SOT = {'red': 12, 'green': 13, 'blue': 14}
  qualifiedGames = []

  isQualifiedGame = True
  item: DiceBag
  for item in games:
    # Check if SOT is more than what we got
    # if so it aint our game
    if item.highRed > SOT['red']:
      isQualifiedGame = False
    
    if item.highGreen > SOT['green']:
      isQualifiedGame = False
    
    if item.highBlue > SOT['blue']:
      isQualifiedGame = False
    
    if isQualifiedGame:
      # if passed with flying colors let get that bread
      qualifiedGames.append(item.gameId)
    
    isQualifiedGame = True
  
  return sum(qualifiedGames)

def part_two(input):
  outTotal = []
  for line in input:
    # Same as before
    outTotal.append(DiceBag(line))

  powerTotal = []
  item: DiceBag
  for item in outTotal:
    # We already did the hard part, just do a little loopin
    powerTotal.append(item.highBlue * item.highGreen * item.highRed)
  
  return sum(powerTotal)
  

main()
  
  
      