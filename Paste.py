import os
from sys import argv
import slash
import pyperclip


def replace_space(inputStr):
    outputStr = ""
    for c in inputStr:
        if c == " ":
            c = "\ "
        outputStr = outputStr + c
    return outputStr


# print(replace_space("test test test"))
Slash = slash.Slash()
input_string = " ".join(argv[1:])
input_string = input_string[3:]
print("in: " + input_string)
output = Slash.convert_slash(input_string)
output = "cd /mnt/c/" + replace_space(output)
print("out: " + output)
pyperclip.copy(output)
final_command = "startBash.bat"

#create dynamic bat file with command
file = open('startBash.bat', 'w')
file.write('C:\Windows\Sysnative\\bash.exe -c "' + output + ' ; exec bash"')
file.close()

print("final command : " + final_command)
os.system(final_command)











# os.system('start /wait cmd /c "dir"')
# os.system("start /wait cmd")

# os.system("dir")
# os.system("cd " + output)
# os.system("start /k PAUSE /wait cmd ")
# os.system("cmd /K C:\SomeFolder\MyApp.exe")
# os.system("Console.ReadKey()")



# output = pyperclip.paste()
# print(output)