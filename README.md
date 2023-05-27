#  Welcome to Specere Labs Setup!

In order to get up and running you are going to need three things: Git, Conda, and our Python plotting setup. If you want to run something on Bell or Negishi you are also going to need Slurm.

# Essential Setup Tasks
## Git
Git serves two purposes: version control and collaboration. Git is a software you install on your computer, while GitHub is a website that allows people to share their git repositories. If you want to learn how to use git, you can find a guide in the following repository: https://github.itap.purdue.edu/Specere-Lab/git_learning_environment

Install: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

Then access your terminal - it should be a pre installed app.
Navigate in your terminal to the location in your filesystem where you want to run your code. You navigate through your filesystem with two commands. The first is `cd /path/to/directory`. That stands for 'change directory' and puts you in that part of the filesystem. Then the other command is `ls` if you are on linux or mac, and `dir` if you are on windows. That command will tell you which directory you are in so you can make sure you are in the right place.

Where should you store your code? I put it in my documents folder but some people put it on the desktop. 

When you are in the correct location type:

`git clone https://github.itap.purdue.edu/Specere-Lab/specere_labs_setup.git`
You will need to use your username and password - keep in mind that this is NOT the password that ends in ,push, and uses duo login, this is the other one

This will download this git repository into wherever you are in your filesystem. If you open up the app you use to nagivate files, you should be able to see it.

## Conda
Python library dependency conflicts can be messy so unless the library you are downloading is very simple and low level (like Math), or if you have a virtual environment setup, don't directly donwload python libraries. Instead, use Conda which is a lightweight virtual environment specifically for Python. If Conda is not yet installed on your system, use this link:  https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html. If you have Anaconda navigator installed you have Conda.

Once you have conda, type `conda activate` in your terminal. You should see that is says `(base)` before everything else. If that does not work type `bash`. Then it is time to create your conda environment from `specere_env.yml`. Fun fact: `.yml` means that it is a YAML file, and YAML stands for 'YAML aint markup language'. This is known as a recursive acronym similar to GNU which stands for 'GNU's Not Unix'.

To create the new conda environment you run `conda env create -f specere_env.yml'` and to activate it you run `conda activate specere_env`. Now you are running in the specere conda environment and have most libraries you will ever need for work in this lab (and in most scenarios).

## Plotting Library
It is important that our plots look good, and it's also beneficial for there to be a uniform look among all lab plots. Therefore whenver you are going to run a script that makes plots, make sure that you have `plotting_library.py` in the same folder, and that you run it at the begining of the file. If you are using jupyter-notebooks, at the begining of your notebook you should put `%run -i 'plotting_library.py'`. If you are using a regular `.py` file, put `from plotting_library import *` at the beginning of your file

# Optional things that might be useful but are not required

## Jupyter Notebooks
Jupyter Notebooks is a way to make code with lots of plots and math-y explanations nice and presentable. You can even print a PDF of the code, text, and plots when you are done! Notebooks is already installed in the conda environment so activate `specere_env` and then type `jupyter-notebook` into the terminal. A link will appear (or automatically open in your browser). A cell can contain markup language (for writing math and text) or code.

## SLURM (for high performance computers)
### Accessing the Supercomputers
At Specere we have access to two supercomputers: Negishi and Bell. Bell has GPUs, Negishi does not. A general rule of thumb is that if you ever find yourself thinking "I wish I could close my computer and move and move but then the code will stop running and I'll have to start all over" it means you should run your code on a supercomputer.

You access the supercomputers via ssh. SSH stands for Secure Shell and it is a way accessing the terminals of other computers from your own computer's terminal. To access Negishi, you type
`ssh username@negishi.rcac.purdue.edu` and to access Bell you type `ssh username@bell.rcac.purdue.edu`. Then you use your duo login to get in.

However I really do not reccomend doing this, it's easier to set up a 'host'. To do this, navigate to `.ssh/` folder in your home directory. To get to your home directory from your terminal type `cd` and nothing after. Then once you are in your `.ssh` directory type `vi config` and a text editor will open up. You have just created a file called `config` using the `vi` text editor. Some folks who are wrong will say that it is better to use the `nano` or `emacs` text editor but you should not listen to them. To start typing in the vi text editor, press `i` for insert. 

In the `config` file you are going to put the following infornmation
```
Host bell
        HostName bell.rcac.purdue.edu
        User username
Host negishi
        HostName negishi.rcac.purdue.edu
        User username
```
then you close the file by typing `:wq` and then the enter key. What this does is that now instead of typing that whole big mess, you type `ssh negishi` or `ssh bell` to get in.

The second thing I'd reccomend is setting up a private key. Duologin takes a long time and isn't great. A private key allows you to login with no password from your computer and it's extremely secure. What you do is, first create an RSS private key/public key pair by going to the `.ssh` folder and typing `ssh-keygen -t rsa`. When it is finished,  you send the keys to bell and negishi by typing `ssh-copy-id -i ~/.ssh/id_rsa.pub bell` and `ssh-copy-id -i ~/.ssh/id_rsa.pub negishi` respectively. After this, you will be able to login by simply typing `ssh bell` and `ssh negishi` with no password issues.

### Setting up an environment in the supercomputers
You can't use `sudo` in the supercomputer so you will almost certainly need to download miniconda via:

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

You might notice something weird where it breaks everything because of something called a 'python path'. I am not sure why this happens but you solve it by opening `.bashrc` in your home directory and typing `export PYTHONPATH=""` at the very start. That way whenever you log in, your PYTHONPATH is reset to nothing. Then you should be able to install conda. You initialize conda by typing `bash`.

One thing you also might considering doing is typing `touch .hushlogin` in your home directory, which makes a hidden file that gets the long login message to not show up.

### running SLURM
You can run code normally, but if you want to take advantage of the speed of the supercommputers you must use SLURM. SLURM is a scheduling program that makes sure every user gets fairly allocated turns. A sample slurm file is called `slurmsample.sub` and is in the github. You can run it with: `sbatch slurmsample.sub`, check its status with `squeue username`, and cancel it with `scancel ID`. The default in the sample slurm is to run it on the `tbeechem` queue. If you need to use a gpu you should be on Bell not Negishi and change `tbeechem` to `gpu`.  ID can be identified from `squeue username`. Also the text output of the file as it is running can be found in an output file that will be produced when the code starts running. The output file is constantly updating - you can read it by typing `cat outputname` but you should not edit it as it will stop updating if you do. 

### slurm channel overview
Personally, I really only ever use the `gpu` queue on Bell because if I'm running something on a supercomputer it needs a GPU. However there are some other channels on Bell you should know about.

`debug` which has a maxium runtime of 30 minutes and very low memory, so only use it to test things.

`highmem` is for when you keep getting out of memory errors

`multigpu` has several GPUs but your code won't be able to take advantage of it unless you can do multithreading which is hard

`tbeechem` is a queue that can only be used by our lab

`standby` is like a communal version of `tbeechem` and is very lame although it has short waiting times. It's the default if you don't specify channel

Negishi only has `highmem`, `standby`, and `tbeechem`. 
