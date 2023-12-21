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


class Line:
  lookUp = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
  }
  
  firstNumber: int = None
  secondNumber: int = None
  baseString: str = None
  joinedValue: int = ""
  processedString: str = ""

  def __init__(self, input: str, doSpelledNumbers: bool):
    self.baseString = input
    self.get_numbers_from_line(doSpelledNumbers)
    
    if self.firstNumber == None or self.secondNumber == None:
      raise Exception(f"Unable to parse: {input}")

    self.joinedValue = f"{self.firstNumber}{self.secondNumber}"
    self.joinedValue = int(self.joinedValue)

  
  def get_numbers_from_line(self, doSpelledNumbers):
    # shorter than self.baseString
    line = self.baseString
    # same ^
    first = ""
    # same ^
    final = ""

    for index, char in enumerate(line):
      # if it is a decimal, great! thats it!
      if char.isdecimal():
        first = int(char) if first == "" else first
        final = int(char)

      # lets parse it
      elif doSpelledNumbers:
        for number in self.lookUp:
          # get initial string value, kinda self explain
          choppedString = line[index:]
          # chop the initial string value to the length of the look up table value   
          choppedString = choppedString[:len(number)]
          
          # assuming we find a line with valid number strings it will be the value of choppedString   
          if number == choppedString:
            first = self.lookUp[number] if first == "" else first
            final = self.lookUp[number]

    # poor mans return statement
    self.firstNumber = first
    self.secondNumber = final

def main():
  isDev = False

  # if isDev:
  #   with open(r"C:\Users\zaned\Desktop\Non-Education\_Code\AdventOfCode\Day1\test_input.txt", 'r') as f:
  #     puzzleInput = f.readlines();
  # else:
  #   with open(r"C:\Users\zaned\Desktop\Non-Education\_Code\AdventOfCode\Day1\input.txt", 'r') as f:
  #     puzzleInput = f.readlines();

  puzzleInput = None
  input = FileLoader(subDirAppend="Day1")
  if isDev:
    puzzleInput = input.testFile
  else:
    puzzleInput = input.mainFile
    

  ptOne = part_one_solver(puzzleInput)
  print(ptOne)

  ptTwo = part_two_solver(puzzleInput)
  print(ptTwo)
    
def part_one_solver(input):
  # Do NOT Parse written numbers
  return sum([Line(line, False).joinedValue for line in input])

def part_two_solver(input):
  # Do Parse written numbers
  return sum([Line(line, True).joinedValue for line in input])

main()
  
  
  
  
  
  