# Getting the Updated Git Repo

The first thing that you want to do every time you start working with the materials we are providing is to check for updates on the files. Here is how you can do that with Git. 

![caution](https://github.com/CRMDA-python/tutorial/blob/master/content/images/caution-h50.png) DO NOT MODIFY THE NOTEBOOK FILES; INSTEAD, SAVE A COPY OF THE NOTEBOOK AND DO ALL YOUR WORK IN THE COPY. Note: if you have already modified the notebooks, just save a copy of it as is, and follow the instructions. 

Make sure that you have closed all of your Jupyter Notebooks (if you don't know how to shut down Jupyter, go [here](https://github.com/CRMDA-python/tutorial/blob/master/shut_down_jupyter.md)). If you are on OS X/Linux, navigate to the "tutorial" directory (that's the directory you cloned during week 1) in Terminal. If you are on Windows, go to the folder you downloaded during week 1, and right click somewhere in the white space. Then select "Git Bash Here". Once you have a command prompt, type the following commands:

```git
git checkout . 
git pull
```

"git checkout" will discard any changes you have made to the notebooks I have provided without deleting the copy that you saved. "git pull" will update the files to reflect the latest changes. 

Once you do that, Git will output something like this:

![git_pull_output](https://github.com/CRMDA-python/tutorial/blob/master/content/images/week2/git_pull_output.png)
