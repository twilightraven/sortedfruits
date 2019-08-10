# by WW 3-2018

def main():
   """
       main function
   """
  
   #list that contains a list of 26 fruit names
   fruits = [];
  
   try:
      
       # open file unsorted_fruits.txt in read mode
       infile = open("/users/raven/documents/uop/cs-1101/unsorted_fruits.txt", "r")

       # open file sorted_fruits.txt in write mode
       outfile = open("/users/raven/documents/uop/cs-1101/sorted_fruits.txt", "w")
      
       # read input file line by line
       for line in infile:
   
         # add fruit name to list
            fruits.append(line);
          
       # sort list
       fruits.sort();
      
       # write sorted data to output file
       for fruit in fruits:
          if fruit != "\n":
           # write fruit name along with new line character
           outfile.write(fruit + " \n");
           print (fruit)
              
       # close files
       infile.close();
       outfile.close();
  
   except Exception as ex:
       # handling exceptions
       print(ex);
      
# call main function
main();       
