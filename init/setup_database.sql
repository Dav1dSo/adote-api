USE adotepet;

-- Create the pets table
CREATE TABLE IF NOT EXISTS pets (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL
);

-- Create the people table
CREATE TABLE IF NOT EXISTS people (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    pet_id INT NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);

-- Insert data into the pets table
INSERT INTO pets (name, type)
VALUES
    ('cobra', 'snake'),
    ('Caos', 'dog'),
    ('gata', 'cat'),
    ('jorgin', 'hamster'),
    ('burros', 'donkey'),
    ('shrek', 'ogre'),
    ('betinha', 'dog');