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
     
def countWordOccurence():
     return None


def generateReport():
     return None

def main():
     print(countWords(path_to_frankeinstein, True))
     readBook(path_to_frankeinstein, False)

 
 #    readBook(path=path_to_frankeinstein)                   worked!! #test for printing
 #   print(readBook(path_to_frankeinstein, True))           worked!! #test for function 
 #   countWords(path_to_frankeinstein, False)               worked!! #test for printing
 #   print(countWords(path_to_frankeinstein, True))         worked!! #test for function
 

 
 
 
main()