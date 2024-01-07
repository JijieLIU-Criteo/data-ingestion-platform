# Start from the Bitnami Spark image
FROM docker.io/bitnami/spark:2

USER root

# Update package lists
RUN apt-get update

# Install Python and pip
RUN install_packages python3-pip

# Upgrade pip
RUN pip3 install --upgrade pip

# Install Jupyter Lab
RUN pip3 install jupyterlab pyspark==2.4.6

# Create a directory for your work
RUN mkdir /workspace

# Set the working directory
WORKDIR /workspace

ENV PYSPARK_SUBMIT_ARGS="--master spark://spark-master:7077 pyspark-shell"

# Expose the port Jupyter Lab will run on
EXPOSE 8888

# Set the command to start Jupyter Lab
CMD ["jupyter", "lab", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
