# Bash Shell Cheatsheet
Hey there! I am Shaykh Farhan. Today we are going to learn about bash.

## What is bash?
Bash is a command processor that typically runs in a text window, where the user types commands that cause actions. It is a Unix shell and command language, and it's the default shell on most Linux and macOS systems. Let's dive into some commands.

## Navigation

```bash
cd directory_name     # Change directory
pwd                  # Print working directory
ls                   # List files and directories
ls -l                # List files with details
ls -a                # List all files, including hidden ones
```


## File Operations

```bash
touch filename       # Create an empty file
cp source destination # Copy file or directory
mv source destination # Move or rename file or directory
rm file_name         # Remove file
rm -r directory_name # Remove directory and its contents
```


## Text Editing

```bash
nano file_name       # Open file in nano text editor
vim file_name        # Open file in vim text editor
cat file_name        # Display content of a file
echo "text" > file   # Create or overwrite file with text

```
## Process Management

```bash
ps                   # Display running processes
ps aux               # Display detailed process information
kill process_id      # Terminate a process
killall process_name # Terminate all processes with a name
```
## Permissions

```bash
chmod +x file        # Add execute permission to a file
chmod -r file        # Remove read permission from a file
chown user:group file # Change owner and group of a file
```
## System Informations

```bash
uname -a             # Display system information
df -h                # Display disk space usage
free -m              # Display memory usage
```
## Redirections

```bash
command > file       # Redirect output to a file (overwrite)
command >> file      # Redirect output to a file (append)
command < file       # Redirect input from a file
command1 | command2  # Pipe output of command1 to command2
```
## Conditional Statement

```bash
if [ condition ]; then
  # commands to execute if condition is true
fi

case "$variable" in
  pattern1) 
    # commands for pattern1
    ;;
  pattern2) 
    # commands for pattern2
    ;;
  *) 
    # commands for other patterns
    ;;
esac
```
## Loops

```bash
for item in list; do
  # commands to execute for each item in the list
done

while [ condition ]; do
  # commands to execute while condition is true
done
```
## Functions

```bash
function_name() {
  # commands in the function
  echo "Hello, $1!"
}

# Call the function
function_name "John"
```
## Conclusion
That's it for today. I will see ya with next cheat sheet. Don't forget to give it a star.
