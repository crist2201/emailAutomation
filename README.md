# emailAutomationProject

This python project can send emails based on any template to different email addresses. 

# Installation

### Open a cmd prompt and write the following commands:
```
# Clone the repo
$ git clone https://github.com/crist2201/emailAutomation.git

# Change the working directory
$ cd emailAutomation

# Install the requirements
$ pip install -r requirements.txt
```
# Usage
### To use this project configure the following files:
#### Go to ```config/config.properties``` file 
  * Set all the configuration field for the project
#### Go to ```config/config.json``` file
  * Set your ```email```
  * Set your ```password```. You have to create an app password: https://support.google.com/accounts/answer/185833?hl=en
### Then go to the project directory and run the following command:
```$ python main.py```
### In order to change the template files, follow the next steps:
1. Go to ```resources/templates```
2. Add your message template to ```messages``` folder
3. Add your data/clientes template to ```data``` folder
4. Add your words to replace template to ```replaceWords``` folder.
