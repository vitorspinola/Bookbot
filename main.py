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
          

def generateReport():
     return None

def main():
     # print(countWords(path_to_frankeinstein, True))
     # readBook(path_to_frankeinstein, False)
     countLetterOccurence(path_to_frankeinstein, False)
     
 #    readBook(path=path_to_frankeinstein)                   worked!! #test for printing
 #   print(readBook(path_to_frankeinstein, True))           worked!! #test for function 
 #   countWords(path_to_frankeinstein, False)               worked!! #test for printing
 #   print(countWords(path_to_frankeinstein, True))         worked!! #test for function
 

 
 
 
main()