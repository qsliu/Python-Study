# Python Virtual Environment

https://docs.python-guide.org/dev/virtualenvs/

* Installing virtualenv

  ```
  pip install --user virtualenv
  ```

  Test your installation:

```
	$ virtualenv --version
```

* Basic Usage
  * Create a virtual environment for a project:

```
$ cd my_project_folder
$ virtualenv venv
```

`virtualenv venv` will create a folder in the current directory which will contain the Python executable files, and a copy of the `pip` library which you can use to install other packages. The name of the virtual environment (in this case, it was `venv`) can be anything; omitting the name will place the files in the current directory instead.

**Note**

‘venv’ is the general convention used globally. As it is readily available in ignore files (eg: .gitignore’)

This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named `venv`.

You can also use the Python interpreter of your choice (like `python2.7`).

```
$ virtualenv -p /usr/bin/python2.7 venv
```

or change the interpreter globally with an env variable in `~/.bashrc`:

```
$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2.7
```

* ​	To begin using the virtual environment, it needs to be activated:

```
$ source venv/bin/activate
```

The name of the current virtual environment will now appear on the left of the prompt (e.g. `(venv)Your-Computer:your_project UserName$)` to let you know that it’s active. From now on, any package that you install using pip will be placed in the `venv` folder, isolated from the global Python installation.

For Windows, same command which is mentioned in step 1 can be used for creation of virtual environment. But, to activate, we use the following command.

Assuming that you are in project directory:

```
PS C:\Users\suryav> \venv\Scripts\activate
```

Install packages as usual, for example:

```
$ pip install requests
```

* ​	If you are done working in the virtual environment for the moment, you can deactivate it:

```
$ deactivate
```

This puts you back to the system’s default Python interpreter with all its installed libraries.

To delete a virtual environment, just delete its folder. (In this case, it would be `rm -rfmy_project`.)

After a while, though, you might end up with a lot of virtual environments littered across your system, and it’s possible you’ll forget their names or where they were placed.

**Note**

Python has included venv module from version 3.3. For more details: [venv](https://docs.python.org/3/library/venv.html).



# Python Virtual Environment Introduction

https://www.geeksforgeeks.org/python-virtual-environment/

