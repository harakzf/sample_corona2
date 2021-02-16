CREATE TABLE users (
        id SERIAL NOT NULL, 
        username VARCHAR(200),
        password VARCHAR(200) NOT NULL,
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        updated_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        PRIMARY KEY (id)
);