# command to install vertual environment
'''python -m venv "name"'''

# Activating a virtual environment
'''
Unix/Mac - source env/bin/activate
windows - .\env\Scripts\activate
'''

# Leaving the virtual environment
'''deactivate'''

# Installing from local archives
'''py -m pip install requests-2.18.4.tar.gz'''

# Using requirements files
'''
example you could create a requirements.txt file containing:
requests==2.18.4
google-auth==1.1.0
'''
# And tell pip to install all of the packages in this file using the -r flag:
'''py -m pip install -r requirements.txt'''

# Freezing dependencies
# Pip can export a list of all installed packages and their versions using the freeze command:
'''py -m pip freeze'''

# get requirments.txt file of all installed pakages using below commond
''' windows - pip freeze > requirements.txt '''
''' linux/ubantu - pip3 freeze > requirements.txt '''

# install all pakages from requirments.txt file using below commond
'''windows - pip install -r requirements.txt'''
'''ubantu/linux - pip3 install -r requirements.txt'''





