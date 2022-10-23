## How to Fork using github CLI

First, download and install [`Github CLI tools`](https://cli.github.com/)

Then, in your favorite command line

    //login to gh cli
    gh auth login --web
    
Find the github url to the repo you want to fork, it will look something like `https://github.com/learn-devops-fast/spock-lizard-docker.git`
    
    //fork using the cli command
    gh repo fork https://github.com/learn-devops-fast/spock-lizard-docker.git --clone

