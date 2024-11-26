# Use the official Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY requirements.txt .  
COPY buy_box_gcp_1 /app/buy_box_gcp_1/ 
COPY gcp_dagster /app/gcp_dagster/ 
COPY include /app/include     

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip setuptools wheel

# Install Dagster and Dagit explicitly
RUN pip install dagster dagit dagster-cloud dagster-dbt pandas_gbq

# Install DBT and its plugins
RUN pip install dbt-core dbt-bigquery dbt-snowflake dbt-postgres dbt-spark

# Expose the port Dagit runs on
EXPOSE 3000

# Set the default command to start Dagit
CMD ["dagit", "-h", "0.0.0.0", "-p", "3000"]
