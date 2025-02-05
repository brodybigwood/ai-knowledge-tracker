import deepseek
import commandr

with open("compare.txt",'r') as file:
    preamble = file.read()

def compare(new, existing):
    return commandr.getJSON(preamble, f"input: new topics (to be added): {new}, existing topics (to be merged with): {existing}")

