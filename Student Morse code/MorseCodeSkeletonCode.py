# Skeleton Program for the AQA AS Summer 2018 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS Programmer Team
# developed in a Python 3 environment


# Version Number : 1.6
import os

SPACE = ' '
EOL = '#'
EMPTYSTRING = ''
FULLSTOP = "."

def ReportError(s):
  print('{0:<5}'.format('*'),s,'{0:>5}'.format('*')) 
        
def StripLeadingSpaces(Transmission): 
  TransmissionLength = len(Transmission)
  if TransmissionLength > 0:
    FirstSignal = Transmission[0]
    while FirstSignal == SPACE and TransmissionLength > 0:
      TransmissionLength -= 1
      Transmission = Transmission[1:]
      if TransmissionLength > 0:
        FirstSignal = Transmission[0]
  if TransmissionLength == 0:
    ReportError("No signal received")
  return Transmission

def StripTrailingSpaces(Transmission): 
  LastChar = len(Transmission) - 1
  while Transmission[LastChar] == SPACE:
    LastChar -= 1
    Transmission = Transmission[:-1]
  return Transmission  

def GetTransmission():
  FileName = input("Enter file name: ")
  if ".txt" not in FileName:
    FileName += ".txt"
  try:
    FileHandle = open(FileName, 'r')
    Transmission = FileHandle.readline()
    FileHandle.close()
    Transmission = StripLeadingSpaces(Transmission)
    if len(Transmission) > 0:
      Transmission = StripTrailingSpaces(Transmission)
      Transmission = Transmission + EOL
    signals = 0
    breaks = 0
    for i in Transmission:
      if i == "=":
        signals += 1
      else:
        breaks += 1
    print(f"{signals+breaks} symbols recieved in transmission consisting of {signals} signals and {breaks} breaks.")
  except:
    ReportError("No transmission found")
    Transmission = EMPTYSTRING
  return Transmission

def GetNextSymbol(i, Transmission):
  if Transmission[i] == EOL:
    print()
    print("End of transmission")
    Symbol = EMPTYSTRING
  else:
    SymbolLength = 0
    Signal = Transmission[i]
    while Signal != SPACE and Signal != EOL:
      i += 1
      Signal = Transmission[i]
      SymbolLength += 1
    if SymbolLength == 1:
      Symbol = '.'
    elif SymbolLength == 3:
      Symbol = '-'
    elif SymbolLength == 0: 
      Symbol = SPACE
    else:
      ReportError("Non-standard symbol received") 
      Symbol = EMPTYSTRING
  return i, Symbol 

def GetNextLetter(i, Transmission):
  SymbolString = EMPTYSTRING
  LetterEnd = False
  while not LetterEnd:
    i, Symbol = GetNextSymbol(i, Transmission)
    if Symbol == SPACE:
      LetterEnd = True
      i += 4
    elif Transmission[i] == EOL:
      LetterEnd = True
    elif Transmission[i + 1] == SPACE and Transmission[i + 2] == SPACE:
      LetterEnd = True
      i += 3
    else:
      i += 1
    SymbolString = SymbolString + Symbol
  return i, SymbolString

def Decode(CodedLetter, Dash, Letter, Dot, MorseCode):
  if CodedLetter not in MorseCode:
    print(f"Invalid Symbol ({CodedLetter}) recieved")
    return "*"
  CodedLetterLength = len(CodedLetter)
  Pointer = 0
  for i in range(CodedLetterLength):
    Symbol = CodedLetter[i]
    if Symbol == SPACE:
      return SPACE
    elif Symbol == '-':
      Pointer = Dash[Pointer]
    else:
      Pointer = Dot[Pointer]
  return Letter[Pointer]

def printMorseCodeSymbols(Letter, MorseCode):
  for i in range(len(Letter)):
    print(f"{Letter[i]}   |   {MorseCode[i]}")

def transmitMorseCode(MorseCode):
  result = SendMorseCode(MorseCode)
  Data = ""
  for i in result[0]:
    if i == ".":
      Data += "= "
    elif i == "-":
      Data += "=== "
    if i == " ":
      Data += "  "
  print("DATA: "+Data)
  fileName = input("Enter name of file: ")
  filePath = os.path.isfile(f"./{fileName}")
  if filePath:
    overWrite = input("File already exists, would you like to overwrite it (Y/N)? ").upper()
    if overWrite == "Y":
      with open(fileName, "w+") as file:
        file.write(Data)
        file.close()
    else:
      while filePath:
        fileName = input("Enter name of file: ")
        filePath = os.path.isfile(f"./{fileName}")
  with open(fileName, "w+") as file:
    file.write(Data)
    file.close()

def ConvertMorseCode(MorseCode, Letter):
  Message = input("Enter a message in Morse Code: ")
  Message = Message.split(" ")
  Output = ""
  for i in Message:
    if i in MorseCode:
      Index = list.index(MorseCode, i)
      Output += Letter[Index]
    elif i == "":
      Output += " "
    else:
      print("Invalid Symbol")  
      Output += "*"
  print(Output)

def SendEncryptedMorseCode(MorseCode):
  user = input("Enter The Message: ")
  cipher = int(input("Enter Caser Cipher: "))
  MorseCodeString = ""
  cMessage = ""
  for i in user:
    if i != " ":
      cMessage += chr(ord(i) + cipher)
    else:
      cMessage += i
  for i in range(len(cMessage)):
    PlainTextLetter = cMessage[i]
    if PlainTextLetter == SPACE:
      Index = 0
    elif PlainTextLetter == FULLSTOP:
      Index = 27
    else: 
      Index = ord(PlainTextLetter) - ord('A') + 1
    CodedLetter = MorseCode[Index]
    MorseCodeString = MorseCodeString + CodedLetter + SPACE
  print(MorseCodeString)

def CalculateTransmissionTime(mCMessage):
  Time = 0
  print(len(mCMessage))
  for i in range(len(mCMessage)):
    print(i)
    if mCMessage[i] == ".":
      Time += 1
    elif mCMessage[i] == "-":
      Time += 3
    elif mCMessage[i] == " ":
      if i != len(mCMessage)-1:
        if mCMessage[i+1] == " "and mCMessage[i+2] == " ":
          Time += 7
        else:
          Time += 3
      else:
        Time += 3
    Time += 1
  print(f"Your message will take {Time} time units to send")

def ReceiveMorseCode(Dash, Letter, Dot, MorseCode): 
  PlainText = EMPTYSTRING
  MorseCodeString = EMPTYSTRING
  Transmission = GetTransmission() 
  LastChar = len(Transmission) - 1
  i = 0
  while i < LastChar:
    i, CodedLetter = GetNextLetter(i, Transmission)
    MorseCodeString = MorseCodeString + SPACE + CodedLetter
    PlainTextLetter = Decode(CodedLetter, Dash, Letter, Dot, MorseCode)
    PlainText = PlainText + PlainTextLetter
  ctr = 0
  wCtr = 0
  for i in MorseCodeString:
    if i == "-" or i == ".":
      ctr += 1
  for i in PlainText:
    if i != " ":
      wCtr += 1
  print(f"{ctr} symbols recieved:\n{MorseCodeString}")
  print(f"Which represent {wCtr} characters:\n{PlainText}")

def SendMorseCode(MorseCode):
  Quatenery = ""
  containsLower = False
  PlainText = input("Enter your message (uppercase letters and spaces only): ")
  for i in PlainText:
    if i.islower():
      containsLower = True
  if containsLower:
    PlainText = PlainText.upper()
    print(f"Only uppercase letters can be used, your message has to be converted to: {PlainText}")
  PlainTextLength = len(PlainText)
  MorseCodeString = EMPTYSTRING
  for i in range(PlainTextLength):
    PlainTextLetter = PlainText[i]
    if PlainTextLetter == SPACE:
      Index = 0
    elif PlainTextLetter == FULLSTOP:
      Index = 27
    else: 
      Index = ord(PlainTextLetter) - ord('A') + 1
    CodedLetter = MorseCode[Index]
    for i in CodedLetter:
      if i == ".":
        Quatenery += "2"
      elif i == "-":
        Quatenery += "3"
      elif i == " ":
        Quatenery += "1"
    Quatenery += "0"
    MorseCodeString = MorseCodeString + CodedLetter + SPACE
  Quatenery = Quatenery[:-1]
  CalculateTransmissionTime(MorseCodeString)
  return(MorseCodeString, Quatenery)

def DisplayMenu(mOption):
  print()
  print("Main Menu")
  print("=========")
  print("R - Receive Morse code")
  print("S - Send Morse code")
  print("P - Print Morse code symbols")
  print("T - Transmit Morse Code")
  print("C - Convert Morse Code")
  print("E - Send Encrypted Message")
  print(f"V - Change to {mOption} Morse code")
  print("X - Exit program")
  print()

def GetMenuOption():
  MenuOption = EMPTYSTRING
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ").upper()
    Options = ["R", "S", "P", "T", "X", "C", "E", "V"]
    if MenuOption not in Options:
        print("Invalid choice, please choose a letter from the menu:")
        DisplayMenu()
  return MenuOption
    
def SendReceiveMessages():
  Dash = [20,23,27,0,24,1,0,17,0,21,0,25,0,15,11,0,0,0,2,22,13,0,0,10,0,0,0]
  Dot = [5,18,2,0,2,9,0,26,0,19,0,3,0,7,4,0,0,0,12,8,14,6,0,16,0,0,0]
  Letter = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.']

  MorseCode = [' ','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.-.-.-']

  ProgramEnd = False
  mOptions = ["American", "International"]
  mOption = mOptions[1]
  notOption = mOptions[0]
  while not ProgramEnd:
    DisplayMenu(notOption) 
    print(f"System is currently using the {mOption} version of Morse code.")
    MenuOption = GetMenuOption()
    if MenuOption == 'R':
      ReceiveMorseCode(Dash, Letter, Dot, MorseCode)
    elif MenuOption == 'S':
      Printer = (SendMorseCode(MorseCode))
      print(Printer[0])
      print(Printer[1])
    elif MenuOption == "P":
      printMorseCodeSymbols(Letter, MorseCode)
    elif MenuOption == "T":
      transmitMorseCode(MorseCode)
    elif MenuOption == "C":
      ConvertMorseCode(MorseCode, Letter)
    elif MenuOption == "E":
      SendEncryptedMorseCode(MorseCode)
    elif MenuOption == "V":
      if mOption == mOptions[1]:
        notOption = mOption
        mOption = mOptions[0]
      else:
        notOption = mOption
        mOption = mOptions[1]
    elif MenuOption == 'X':
      ProgramEnd = True
    

if __name__ == "__main__":
  SendReceiveMessages()
