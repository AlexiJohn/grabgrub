# Pull from official Dockerhub Python 3.9.7 image
FROM python:3.9.7-alpine

# Update Linux packages
RUN apk update

# Set work directory
WORKDIR /usr/src/app

# Expose port 8080
EXPOSE 8080

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements.txt
COPY ./requirements.txt /usr/src/app/requirements.txt

# Install from previously copied requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

# Copy project files into Docker image's work directory
COPY . /usr/src/app/

# Copy entrypoint.sh script into Docker image
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# Set entrypoint script to the recently copied script
ENTRYPOINT ["sh","/usr/src/app/entrypoint.sh"]