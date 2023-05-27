#  Welcome to Mechanical Labs Setup!

At Specere Labs I developed a setup system so as to get mechanical engineering students up and running with code as fast as possible, with example files and such. I saw that it could be easily adapted to other labs - here is a generalized version. If you think this would be useful please fork!

In order to get up and running you are going to need three things: Git, Conda, and our Python plotting setup. If you want to run something on a supercomputer you are also going to need Slurm.

# Essential Setup Tasks
## Git
Git serves two purposes: version control and collaboration. Git is a software you install on your computer, while GitHub is a website that allows people to share their git repositories.

Install: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Then access your terminal - it should be a pre installed app.
Navigate in your terminal to the location in your filesystem where you want to run your code. You navigate through your filesystem with two commands. The first is `cd /path/to/directory`. That stands for 'change directory' and puts you in that part of the filesystem. Then the other command is `ls` if you are on linux or mac, and `dir` if you are on windows. That command will tell you which directory you are in so you can make sure you are in the right place.

Where should you store your code? I put it in my documents folder but some people put it on the desktop. 

When you are in the correct location type:

`git clone https://github.itap.purdue.edu/Specere-Lab/specere_labs_setup.git`

This will download this git repository into wherever you are in your filesystem. If you open up the app you use to nagivate files, you should be able to see it.

### learn git in four commands
Lets say you change some code in your git folder and want to share it with everybody on your github. You type:
`git add .`
`git commit -m 'I fixed this and this bug'`
`git push origin`

This uploads your code. Then lets say somebody else commits code and you want it on your computer. You type:
`git pull`

## Conda
Python library dependency conflicts can be messy so unless the library you are downloading is very simple and low level (like Math), or if you have a virtual environment setup, don't directly donwload python libraries. Instead, use Conda which is a lightweight virtual environment specifically for Python. If Conda is not yet installed on your system, use this link:  https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html. If you have Anaconda navigator installed you have Conda.

Once you have conda, type `conda activate` in your terminal. You should see that is says `(base)` before everything else. If that does not work type `bash`. Then it is time to create your conda environment from `specere_env.yml`. Fun fact: `.yml` means that it is a YAML file, and YAML stands for 'YAML aint markup language'. This is known as a recursive acronym similar to GNU which stands for 'GNU's Not Unix'.

To create the new conda environment you run `conda env create -f specere_env.yml'` and to activate it you run `conda activate specere_env`. Now you are running in the specere conda environment and have most libraries you will ever need for work in this lab (and in most scenarios).

## Plotting Library
It is important that our plots look good, and it's also beneficial for there to be a uniform look among all lab plots. Therefore whenver you are going to run a script that makes plots, make sure that you have `plotting_library.py` in the same folder, and that you run it at the begining of the file. If you are using jupyter-notebooks, at the begining of your notebook you should put `%run -i 'plotting_library.py'`. If you are using a regular `.py` file, put `from plotting_library import *` at the beginning of your file

# Optional things that might be useful but are not required

## Jupyter Notebooks
Jupyter Notebooks is a way to make code with lots of plots and math-y explanations nice and presentable. You can even print a PDF of the code, text, and plots when you are done! Notebooks is already installed in the conda environment so activate `specere_env` and then type `jupyter-notebook` into the terminal. A link will appear (or automatically open in your browser). A cell can contain markup language (for writing math and text) or code.
