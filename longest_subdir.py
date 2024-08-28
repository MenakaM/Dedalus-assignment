import os
import sys

def longest_subdir(directory):
    longest_name= " "

  for item in os.listdir(directory):
      path = os.path.join(directory,item)
      if os.path.isdir(path):
          if len(item)> len(longest_name):
              longest_name = item
  return longest_name

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(" longest subdir is <directory> ")
        sys.exit(1)

    directory = sys.argv[1]

    res= longest_subdir(directory)

    print(res)
          

      
