#imports
import os

#initializing global variables
path_to_frankeinstein = "./books/frankeinstein.txt"         #new function would be to loop inside the local book repository, but then we would need to add the ./books folder to the repository removing it from ./.gitignore
path_to_x = None

def readBook(path, other_function_request):
     response = None
     try:
          if type(path) != str:
               raise Exception("no path string was parsed to the readBook function!")
          
          # check if the path actually exists:
          check = os.path.exists(path)
          if check != True:
               raise Exception("Path does not exist.")
          
          with open(f'{path}') as f:
               file_contents = f.read()
          f.close()
          
          if file_contents == "":
               raise Exception(f"Nothing inside the file {path}")
          else:
               if other_function_request==True:
                    response = file_contents
               else:
                    response = print(file_contents)
     except Exception as e:
          print(f"An error Occurred: {e}")
     
     return response

def countWords(path, other_function_request):
     response = None
     try: 
          content = readBook(path, True)
          
          if content != "":
               words = content.split()
               count_words = len(words)
               
               if other_function_request == True: 
                    response = count_words
               else:
                    response = print(f"This book has {count_words} words!!")
          
          else:
               raise Exception("Could not read words, check the line below for more information.")

     except Exception as e:
          print(e)
     return response
     
def countLetterOccurence(path, other_function_request):
     try:
          content = readBook(path, True)
          whitespaces = 0
          for i in content:
               if i == " ":
                    whitespaces += 1
               else:
                    pass
          letters_dict = {' ' : whitespaces }
          raw  = content.lower().split()
          raw_content = []
          for i in raw:
               for j in i:
                    raw_content.append(j)
               
          unique_letters = list(set([i for i in raw_content]))
          if len(unique_letters) == 1:
               letters_dict =  {unique_letters[0]: 1}
          elif len(unique_letters) == 0:
               letters_dict = {}
               raise Warning("No unique characters were found in this book, returning empty dictionary")
          else:
               for unique_letter in unique_letters:
                    occurences_count = 0
                    for letter in raw_content:
                         if letter == unique_letter:
                              occurences_count += 1
                         else:
                              pass
                    letters_dict.update({unique_letter: occurences_count})
     except Exception as e:
          print(f"An error Occurred: {e}")
     if other_function_request is True:
          return letters_dict
     else:
          return print(letters_dict)
          

def generateReport(path):
     try:
          countDict = countLetterOccurence(path, True)
          ##output text
          
          list_of_keys = list(countDict.keys())
          list_of_values = list(countDict.values())
          
          def print_report():
               print("*"*10)
               print(f"Begin {path} report")
               print("*"*10)
               for index in range(len(list_of_keys)):
                    if list_of_keys[index] != " " and list_of_keys[index] != '.' and list_of_keys[index] != "#":
                         print(f"The '{list_of_keys[index]}' character was found {list_of_values[index]} times")               
               print("*"*10)
               print(f"Ending {path} report")
               print("*"*10)
          
          
     except Exception as e:
          print(f"An error occurred: {e}")
     return print_report()

def main():
     while True:
          try:
               choice = -1
               while choice not in range (0,5):
                    print("_________________________________")
                    print("1 *** read frankeinstein")
                    print("2 *** get number of words in book")
                    print("3 *** get a report about the book")
                    print("4 *** exit program !)")
                    print("_________________________________")
                    print(" ")
                    choice = int(input("insert your choice here: "))        
                    if choice not in range(0,5):
                         print("please choose a number available in the current menu...")
                    else:
                         if choice == 1:
                              readBook(path_to_frankeinstein, False)
                              choice = -1
                         elif choice == 2:
                              countWords(path_to_frankeinstein, False)
                              choice = -1
                         elif choice == 3:
                              generateReport(path_to_frankeinstein)
                              choice = -1
                         else:
                              print("Exiting program, thanks for testing")
                              exit()
          except Exception as e:
               print(f"An exception occurred: {e}")
                         
          
          return 0
     

 

 
 
 
main()