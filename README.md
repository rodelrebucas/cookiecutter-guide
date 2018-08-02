## Quickstart guide for learning cookiecutter

A. Install pipenv 

`pip install pipenv`

B.1 Clone this repo and run to install dependencies

`pipenv install`

B.2 Or you can just run

`pip install cookiecutter`

or

`pipenv install cookiecutter`

C. Create root directory

`mkdir CookieMonster`

D. Create the actual project directory template

`mkdir {{cookiecutter.directory_name}}`

`cd {{cookiecutter.directory_name}}`

`touch {{cookiecutter.file_name}}.py`

    Explanation:
        
    cookiecutter.variable_name, enclosed in jinja template to be replaced when using this template.

E. Go back one directory up or to the root dir

`cd ..`

F. Create cookiecutter.json, this file contains the default values.

`touch cookiecutter.json`

G. Run your cookiecutter

`cookiecutter \path\to\CookieMonster`


F. See running **hooks** to run scripts before or after cookiecutter runs