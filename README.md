# cmdvocab
Dictionary CLI program written in Python 

### Dependencies 
These are the list of libraries to install using pip3 and pip. Most of these are already in your system by default.
For **ubuntu**,copy & paste this command:
```
$ sudo apt install python3-pip && sudo apt install python-pip
```
- requests
- http
- bs4 
- urllib

Copy & paste this command:
```
pip3 install requests && pip3 install bs4 && pip install urllib3 && pip install http 
```
### How to install script 
<ol>
  <li>Clone this git repository</li>
  <li>Open the folder cmdvocab</li>
  <li>Open a terminal in this folder</li>
  <li>Copy-paste the following commands in the terminal:</li>
</ol>

```
sudo mkdir $HOME/.cmdvocab && sudo cp cmdvocab.py $HOME/.cmdvocab && sudo cp dheeraj.py $HOME/.cmdvocab && sudo cd $HOME/.cmdvocab && sudo mv cmdvocab.py cmdvocab && chmod +777 cmdvocab && cd && echo "alias cmdvocab='$HOME/.cmdvocab/./cmdvocab'" >> ~/.bash_aliases && source ~/.bash_aliases && echo "Successfully installed cmdvocab"  

```
### How to use 
Type **cmdvocab** in a terminal, and you are presented with a help menu. You'll know how to use the program from there.

### NOTE
Use the argument -v or --verbose before the word to be searched

