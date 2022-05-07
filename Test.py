import os
os.system('/Library/Developer/CommandLineTools/usr/bin/python3 -m pip install --upgrade pip')
os.system("pip3 install pyfiglet")
from pyfiglet import figlet_format

print(figlet_format("VIDIS TOHLE?", font='starwars'))
