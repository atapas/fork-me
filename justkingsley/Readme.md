## This is my Contribution to this year's October Fest.

### Working on local repo

→ 1. git init

→ 2. git add .

→ 3. git commit -m "description"

→ 4. git branch -M branchName

### Adding to online repo

→ 5. git remote add origin repoUrl

→ 6. git push -u origin branchName

### Committing to online repo

→ 1. git add .

→ 2. git commit -m "**description**"

→ 3. git push -u origin **branchName**

### Detaching Head

You can detach the `HEAD` which is the symbolic name for the current commit

- code snippet
    
    // To detach head we do:
    git checkout <headposition> 
    //for example
    git checkout C3 // moving head to C3
    
    

### Checkout

git checkout <branchname> ^ // to move head upward.
git checkout -b <branchname> // create new branch and checkout to it.
