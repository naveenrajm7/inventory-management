# 1. The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# 2. The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# 3. create root directory for our project in the container
RUN mkdir /inventory_management

# 4. Set the working directory to our project folder
WORKDIR /inventory_management

# 5. Copy the current directory contents into the container at /our_working_dir
ADD requirements.txt /inventory_management/

# 6. Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# 7. Add all our files to working directory in container
ADD . /inventory_management/
