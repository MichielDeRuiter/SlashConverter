import sys
import slash
import pyperclip


class WindowsToLinuxDir:

    def __init__(self):
        pass

    sys.path.append('__main__.py')
    inputStr = "C:\Data\Projecten\Software\SlashConverter"
    inputStr = inputStr[3:]
    Slash = slash.Slash()
    outputStr = Slash.convert_slash(inputStr)
    print("outPUTT: " + outputStr)

    prefix = "cd /mnt/c/"
    outputStr = prefix + outputStr
    output = pyperclip.paste
    print(outputStr)
