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
        return f.read()

    else:
      with open(f"{fileName}", 'r') as f:
        return f.read()


class EngineSchematic:
  symbolList = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
    "-", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'",
    "<", ">", ",", "?", "/", "`", "~"
    ]

  def __init__(self, schematic):
    self.schematic = schematic
    self.splitSchematic = schematic.split("\n")
    self.partNumbers = []
    self.partNumbers.append(self.findAdjacentNumbers())

  
  def findAdjacentNumbers(self):
    for i, item in enumerate(self.schematic):
      if item in self.symbolList:
        for ii, returnList in enumerate(self.getAllAdjacentNumbers(i)):
          for item in returnList:
            if item.isdecimal():
              self.getAllNumbersTillSymbol(ii)
  
  
  def getAllNumbersTillSymbol(self, positionRelativeToBase):
    # 0 = above / +
    # 1 = same  / +1 | -1
    # 2 = below / -



    pass
    

  def getAllAdjacentNumbers(self, startIndex):
    lineLength = len(self.schematic.split("\n")[0])
    # For debugging purposed only
    # lookAtSymbol = self.schematic[startIndex]
    # [1, 2, 3]
    # [4, 0, 5]
    # [6, 7, 8]
    i_1 = self.schematic[startIndex - (lineLength + 2)]
    i_2 = self.schematic[startIndex - (lineLength + 1)]
    i_3 = self.schematic[startIndex - (lineLength)]
    
    i_4 = self.schematic[startIndex - 1]
    i_5 = self.schematic[startIndex + 1]
    
    i_6 = self.schematic[startIndex + (lineLength + 2)]
    i_7 = self.schematic[startIndex + (lineLength + 1)]
    i_8 = self.schematic[startIndex + (lineLength)]

    return [
      [i_1, i_2, i_3],
      [i_4, '0', i_5],
      [i_6, i_7, i_8],
    ]
    

def main():
  isDev = True
  input = FileLoader(subDirAppend="Day3")

  if isDev:
    input = input.testFile
  else:
    input = input.mainFile
  
  ptOne = part_one(input)
  print(ptOne)
  

def part_one(input):
  return(EngineSchematic(input))


main()
  