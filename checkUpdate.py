import git 
import os

print("Checking for updates")

git_dir = "C:/Fetch Suppliers/"
g = git.cmd.Git(git_dir)
msg = g.pull()

print(msg)
os.system("echo Last Update: & git log -1 --pretty=%B")
