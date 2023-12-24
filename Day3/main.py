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

class PartInformation:
  def __init__(self, char):
    self.symbolChar = char
    self.partNumbers = []
  
  def appendPartNumber(self, partNumber):
    self.partNumbers.append(partNumber)


class EngineSchematic:
  symbolList = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
    "-", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'",
    "<", ">", ",", "?", "/", "`", "~"
    ]

  def __init__(self, schematic):
    self.schematic = schematic
    self.splitSchematic = schematic.split("\n")
    self.schematicHeaderSize = len(self.splitSchematic[0])
    self.partNumbers = []
    self.partNumbers.append(self.findAdjacentNumbers())
    self.partInfomation:list[PartInformation] = []

  
  def findAdjacentNumbers(self):
    for i, item in enumerate(self.schematic):
      if item in self.symbolList:
        print(self.getAllAdjacentNumbers(i))
    

  def getAllAdjacentNumbers(self, startIndex):
    lineLength = len(self.schematic.split("\n")[0])
    # For debugging purposed only
    # lookAtSymbol = self.schematic[startIndex]
    # [1, 2, 3]
    # [4, 0, 5]
    # [6, 7, 8]
    adj = []
    hold = None
    
    if (hold:=self.schematic[startIndex - (lineLength + 2)]).isdecimal():
      adj.append(self._digitHunter(startIndex - (lineLength + 2)))

    if (hold:=self.schematic[startIndex - (lineLength + 1)]).isdecimal():
      adj.append(self._digitHunter(startIndex - (lineLength + 1)))

    if (hold:=self.schematic[startIndex - (lineLength)]).isdecimal():
      adj.append(self._digitHunter(startIndex - (lineLength)))

    if (hold:=self.schematic[startIndex - 1]).isdecimal():
      adj.append(self._digitHunter(startIndex - 1))

    if (hold:=self.schematic[startIndex + 1]).isdecimal():
      adj.append(self._digitHunter(startIndex + 1))

    if (hold:=self.schematic[startIndex + (lineLength + 2)]).isdecimal():
      adj.append(self._digitHunter(startIndex + (lineLength + 2)))

    if (hold:=self.schematic[startIndex + (lineLength + 1)]).isdecimal():
      adj.append(self._digitHunter(startIndex + (lineLength + 1)))

    if (hold:=self.schematic[startIndex + (lineLength)]).isdecimal():
      adj.append(self._digitHunter(startIndex + (lineLength)))

    return adj    

  def _digitHunter(self, startIndex):
    builtDigit = ""

    currentChar = ""
    iterator = 0
    while currentChar not in self.symbolList and currentChar != ".":
      builtDigit += currentChar
      currentChar = self.schematic[startIndex + iterator]
      
      iterator += 1
    
    currentChar = ""
    iterator = 0
    while currentChar not in self.symbolList and currentChar != ".":
      if iterator != 0:
        builtDigit = currentChar + builtDigit
        currentChar = self.schematic[startIndex + iterator]
        
      iterator -= 1
      
    return int(builtDigit)
      
    
  def _0(self):
    """
    If a bitshift occurs this will be called
    """
    print("THE HUMANITY, THE SOLAR FLARES, THE DOWNRIGHT ABSURTITY OF IT ALL")
    print("the opps")

    return "the opps"
    
    

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
  