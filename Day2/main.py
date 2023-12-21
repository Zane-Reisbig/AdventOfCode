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
    


def main():
  input = FileLoader()
  
  
      