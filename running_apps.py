import subprocess
import platform
command = ""
if platform.system() == "Windows":
    command = "tasklist"
elif platform.system() == "Linux":
    command = "ps aux"
elif platform.system() == "Darwin":
    command = "ps aux"
output = subprocess.check_output(command, shell=True, text=True)
print(output)