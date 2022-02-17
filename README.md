<br/>
  <h1 align="center">Datoscout Django Template </h1>


### Built With

* [Django](https://www.djangoproject.com/)
* [Tailwind CSS](https://tailwindcss.com/)
<br/><br/>

<!-- GETTING STARTED -->
## Getting Started

1. Clone the official repo [templateDjangoTailwind]( https://github.com/jlkhermes38/templateDjangoTailwind)

2. Create your environment (cf. Useful commands section)
3. Install the libraries
```sh
  pip install -r requirements.txt
  ```
4. Create .env file in the root level (NPM_BIN_PATH optional for tailwind)
```sh
  SECRET_KEY='django-insecure-@+@%xgdyp_e%!(=3a0i1g=t)h1n-plm_#o(j$m(qr@#ms30f_-'
  ALLOWED_HOSTS="*"
  DEBUG=True
  NPM_BIN_PATH=r"D:\nodejs\npm.cmd"
  ```

5. Run ./run_manage.sh script
```sh
  ./run_manage.sh
  ```

6. Install precommit and test it in commit
```sh
  pre-commit install
  ```

7. Install and test django-tailwind package
```sh
  python manage.py tailwind install
  python manage.py tailwind start
  ```


8. Admin page in url: [http://127.0.0.1:8000/adminjlk/](http://127.0.0.1:8000/adminjlk/)

<br>


<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**, but to facilitate the revision, they must respect the current versioning policy described here below:
### Set-up
1. Pull last changes from master (`git pull origin master`)
2. Create a Feature branch (`git checkout -b feature/AmazingFeature`) or a bug fix branch (`git checkout -b bugfix/AmazingBugFix`)
3. Be sure to use linters as black and install pre-commit & black if needed (cf. How to section - precommit using at least the .yaml described)
### Developpment
1. Code your feature of bugfix
2. Create or update always your .gitignore/requirements.txt files
3. Adapt or create tests files related yo your development
4. Test there is no code regression (`python manage.py test -v 2`)
6. Git add your changes (`git add . `)
7. Commit your Changes (`git commit -m 'Add some AmazingFeature'`) verifying it uses pre-commit
8. Verify that you have last changes from master in your current branch (`git pull origin master`) to avoid conflicts with latest developments
10. Push to the Branch (`git push origin feature/AmazingFeature`)
11. Open a Pull Request when everything is ended
<br><br>

## Code structure

### Apps structure (TBD)

### Creating superuser and sqlite test database


# How to

In the following section, there is small documentation to go faster in the deployment and good coding practices.
<br><br>

## Virtual environments

Please always use environments and adapt to be inline with requirements.txt

1. Create a new environment & activate
  ```sh
  # Windows
> python -m venv .venv
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> .venv\Scripts\Activate.ps1
(.venv) >

# macOS
% python3 -m venv .venv
% source .venv/bin/activate
(.venv) %
  ```

## Test command

- python manage.py test -v 2

2. Deactivate current environment
  ```sh
  # Windows
(.venv) > deactivate
>
# macOS
(.venv) % deactivate
%
  ```
<br/><br/>


## .gitignore

Adding a .gitignore file is a must to modern development and to be able to contribute between larger teams. There are a lot of templates and it should be updated if needed, but a standard we'll use for this project is the following:

```sh
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Media files
media/
# Elastic Beanstalk Files
.elasticbeanstalk/*
!.elasticbeanstalk/*.cfg.yml
!.elasticbeanstalk/*.global.yml

node_modules
*.json
*.config.js

#IDE
.idea/
.DS_Store
```

### To remove the directory from git repo

```sh
git rm -r one-of-the-directories
```
## Linters

In order to meet the best code-quality standards, you should use linters every time before you commit to ensure good quality standards.

A good article describing the benefits of linters is the following.
[https://sourcelevel.io/blog/what-is-a-linter-and-why-your-team-should-use-it](https://sourcelevel.io/blog/what-is-a-linter-and-why-your-team-should-use-it)

In our project, we will mainly use Black but others linters could be added. Linters and using pre-commit is strongly recommended to automate the checks. A good extensive article describing interactions is the following:

[https://codeburst.io/tool-your-django-project-pre-commit-hooks-e1799d84551f
](https://codeburst.io/tool-your-django-project-pre-commit-hooks-e1799d84551f
)
<br><br>

## Black

Black is a Python code formatter. It will reformat your entire file in place

according to the Black code style, which is pretty close to PEP8.

To quote the project README:

> Black is the uncompromising Python code formatter. By using it, you agree to

> cede control over minutiae of hand-formatting. In return, Black gives you speed,

> determinism, and freedom from `pycodestyle` nagging about formatting. You will

> save time and mental energy for more important matters.

- Configuration file: `pyproject.toml`
- Editor/IDE configuration: https://black.readthedocs.io/en/stable/editors.html
<br><br>

<!-- test -->
## Pre-commit

[pre-commit](https://github.com/pre-commit/pre-commit) is a Python framework for git hook management — we’ll use it to run Black against every commit you make to your project.

To configurate easily:
https://medium.com/gousto-engineering-techbrunch/automate-python-code-formatting-with-black-and-pre-commit-ebc69dcc5e03

Then, adding to run automatically Django tests, our **.pre-commit-config.yaml** file should be the following
```sh
repos:
    - repo: https://github.com/pre-commit/pre-commit-hooks
      rev: v4.0.1
      hooks:
        # See https://pre-commit.com/hooks.html for more hooks
        - id: check-ast
        - id: check-case-conflict
        - id: check-executables-have-shebangs
        - id: check-merge-conflict
        - id: debug-statements
        - id: end-of-file-fixer
        - id: name-tests-test
          args: [ "--django" ]
        - id: trailing-whitespace

    - repo: https://github.com/rtts/djhtml
      rev: 'v1.4.10'
      hooks:
        - id: djhtml

    - repo: https://github.com/ambv/black
      rev: 21.12b0
      hooks:
      - id: black

    - repo: local
      hooks:
        - id: django-test
          name: django-test
          entry: python manage.py test -v 1
          always_run: true
          pass_filenames: false
          language: system
```
Run: `pre-commit install`
Finally, run the following command: `pre-commit autoupdate`

<br><br>

## Install Tailwind via npm

## Requirements

For development, you will only need Node.js and a node global package, installed in your environement.

### Node
- #### Node installation on Windows

  Just go on [official Node.js website](https://nodejs.org/) and download the installer.
Also, be sure to have `git` available in your PATH, `npm` might need it (You can find git [here](https://git-scm.com/)).

- #### Node installation on Ubuntu

  You can install nodejs and npm easily with apt install, just run the following commands.

      $ sudo apt install nodejs
      $ sudo apt install npm

- #### Other Operating Systems
  You can find more information about the installation on the [official Node.js website](https://nodejs.org/) and the [official NPM website](https://npmjs.org/).

If the installation was successful, you should be able to run the following command.

    $ node --version
    v8.11.3

    $ npm --version
    6.1.0

- ### Make a package.json file

      $ npm init -y

- Install tailwindCSS package and some other packages with npm

      $ npm install -D tailwindcss@latest autoprefixer@latest

- Create a index.html file and style.css file

Inside the style.css file paste the below code and leave the html page for now

    $ @tailwind base;
    $ @tailwind components;
    $ @tailwind utilities;

Now generate a fully compiled Tailwind CSS file from style.css

    $ npx tailwindcss -i style.css -o tailwind.css

Use the compiled tailwind.css file inside our index.html, to do that paste the below code in your html file

    $  <link href="tailwind.css" rel="stylesheet">

- #### Create your configuration file
     If you’d like to customize your Tailwind installation, generate a config file for your project using the Tailwind CLI utility included when you install the tailwindcss npm package:

    $ npx tailwindcss init

This will create a minimal tailwind.config.js file at the root of your project:

    $ // tailwind.config.js
    $ module.exports = {
    $   purge: [],
    $   darkMode: false, // or 'media' or 'class'
    $   theme: {
    $     extend: {},
    $   },
    $   variants: {},
    $   plugins: [],
    $ }

 Learn more about configuring Tailwind in the [configuration documentation](https://tailwindcss.com/docs/configuration).#


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact
jorge@datoscout.com
