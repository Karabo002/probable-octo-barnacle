# Use the official Python base image
FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt into the container
#COPY requirements.txt .

# Copy the rest of the application code into the container
COPY  . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port your application will run on (replace 8080 with your port number)
EXPOSE 8080

# Define environment variable (if needed)
#ENV NAME World

# Run your application
CMD ["python", "movies.py"]
#Replace your_app.py with the name of your Python script.

