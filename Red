Create a directory for your WordPress project 
mkdir my-wordpress-project
Navigate to it in your terminal.
cd my-wordpress-project
Inside your project directory, create a file
nano Dockerfile
In the Dockerfile, start by specifying the base image
# Use an official WordPress image as the base image
FROM wordpress:latest
#Set author label
LABEL maintainer="manjushindhe123@gmail.com"
Use the Expose port 80
EXPOSE 80
#Command to run when the container starts
CMD ["apache2-foreground"]
Save the changes to your Dockerfile and exit your text editor

