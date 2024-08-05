-- Create the database
CREATE DATABASE weather_db;

-- Connect to the new database
\c weather_db

-- Create a test table to verify initialization
CREATE TABLE initialization_check (
    id SERIAL PRIMARY KEY,
    initialized_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert a record to confirm the initialization
INSERT INTO initialization_check DEFAULT VALUES;