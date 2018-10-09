import sys
sys.path.append('__main__.py')

class Slash:

    def convert_slash(self,inputStr):
        # if inputStr.find("/") != -1:
        if inputStr.__contains__("/"):
            outputStr = inputStr.replace("/", "\\")
        else:
            outputStr = inputStr.replace("\\", "/")
        return outputStr

