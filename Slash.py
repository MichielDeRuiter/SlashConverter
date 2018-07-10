# import the necessary packages
import argparse
import sys
from sys import argv

inputStr = " ".join(argv[1:])

if inputStr.__contains__("/"):
    outputStr = inputStr.replace("/", "\\")
else:
	outputStr = inputStr.replace("\\", "/")

print("OUTPUT STRING: " + outputStr)

#arguments
# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-n", "--reverse", required=False,
# help="Convert forward slash to backslash. Type --reverse for the input")
# args = vars(ap.parse_args())

# if "".format(args["reverse"]):
# else:

# import the necessary packages
# import argparse
# 1
# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-n", "--name", required=False,
# 	help="name of the user")
# args = vars(ap.parse_args())
#
# # display a friendly message to the user
# print("Hi there {}, it's nice to meet you!".format(args["name"]))

# print("The script is called:", argv[0]) #slicing our list for the first item
