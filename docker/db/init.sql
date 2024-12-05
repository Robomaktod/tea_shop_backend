-- Initialize the database with some sample data if needed
-- This script runs automatically on container startup

-- Create Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
);

-- Create Teas table
CREATE TABLE IF NOT EXISTS teas (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL
);

-- Create Orders table
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    tea_id INT REFERENCES teas(id),
    quantity INT NOT NULL
);

-- Insert sample data
INSERT INTO teas (name, description, price)
VALUES
    ('Green Tea', 'Refreshing and healthy green tea.', 2.99),
    ('Black Tea', 'Rich and bold black tea.', 3.49),
    ('Herbal Tea', 'Relaxing herbal blend.', 4.25)
ON CONFLICT DO NOTHING;
