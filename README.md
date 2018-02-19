# Healthy Recipes Web App

This project is a web application for displaying different recipes in various courses.

## Required tools:

- [Python **3.6.3**](https://www.python.org/downloads/release/python-363/).
- [Vagrant **1.9.2**](https://www.vagrantup.com/downloads.html).
- [Oracle VM VirtualBox **5.1.30**](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
- [SQLAlchemy](https://www.sqlalchemy.org/download.html).
- [Flask](https://pypi.python.org/pypi/Flask/0.12.2).

## Steps for running:

1. After installing the above links run **`pg_config.sh`** or start your prefered **command line** and enter these commands:
```
pip install --upgrade pip
pip install werkzeug==0.8.3
pip install flask==0.9
pip install Flask-Login==0.1.3
pip install oauth2client
pip install requests
pip install httplib2
```
2. Now double click on `addRecipes.py` to load all recipes to the database.
3. Start your prefered **command line** (if you havn't yet).
4. Change your working directory location to the folder containing  the **project files**.
5. Type `vagrant up` in your command line then press **Enter**, this step may take a while if it's running for the first time.
6. When the command line finshes loading type `vagrant ssh`.
7. Use `cd /vagrant` command to change to `vagrant` directory.
8. Type `python main.py` then press **Enter**.
9. Open any web browser then type `localhost:7070` or `127.0.0.1:7070`.
10. The website should be up and running now. Enjoy :).

**Note**: If you faced an error about ports after typing `vagrant up` simply open `Vagrantfile` with any text editor and change port numbers
found in lines 7 - 9.

## Changable Values

- You can change the **limit** of recipes to be shown in the **latest recipes** section, to do so just open the `main.py` file using **any
text editor** (code editor is prefered).In line `40` you will find this line of code:

```python
latestRecipesLimit = 9
 ```
 
 just **replace** the number `9` with any desired value then **save** and reload the website.
