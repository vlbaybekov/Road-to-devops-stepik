#!/usr/bin/python
import time

file_path = "numbers.txt" 

def write_numbers(): 
    counter = 1 
    while True: 
        print(counter)
        with open(file_path, "a") as file: 
            file.write(str(counter) + "\n") 
            counter += 1 
        time.sleep(1) 

write_numbers() 
