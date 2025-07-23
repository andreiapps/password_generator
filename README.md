# Password Generator
Password Generator is an app that can generate random passwords. To run the app from source code, install the pyperclip module with ```sudo pip3 install pyperclip``` and download and run the main.py file. To build it from the source, open a terminal and run the following commands:

```
sudo pip3 install pyperclip pyinstaller # install the pyperclip(used for copying the password to the clipboard) and the pyinstaller(used for packaging the app into an executable) modules
cd Downloads # Replace "Downloads" with the location of the main.py file if you saved it somewhere else
pyinstaller --name "passgen" --onefile --noconsole main.py # Build the app
```
Now you can go to the location of the main.py file, enter in the dist directory and double-click the file to run it. You will have to repeat this every time you want to launch it. You can also delete the passgen.spec file and the build directiory, as they are not needed.

This program is licensed under the GPL-v3 license.
