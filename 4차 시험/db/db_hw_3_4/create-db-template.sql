CREATE DATABASE library_db
    DEFAULT CHARACTER SET = 'utf8mb4';

USE library_db;

CREATE TABLE authors (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100)
);

CREATE TABLE genres (
  id INT PRIMARY KEY AUTO_INCREMENT,
  genre_name VARCHAR(100)
);

CREATE TABLE books (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(100),
  author_id INT,
  genre_id INT,
  FOREIGN KEY (author_id) REFERENCES authors(id),
  FOREIGN KEY (genre_id) REFERENCES genres(id)
);

INSERT INTO 
  authors (name)
VALUES 
  ('J.K. Rowling'),
  ('George R.R. Martin'),
  ('J.R.R. Tolkien'),
  ('Isaac Asimov'),
  ('Agatha Christie');

INSERT INTO 
  genres (genre_name)
VALUES
  ('Fantasy'),
  ('Science Fiction'),
  ('Mystery'),
  ('Thriller');

INSERT INTO 
  books (title, author_id, genre_id)
VALUES
  ("Harry Potter and the Philosopher's Stone", 1, 1),
  ('Harry Potter and the Chamber of Secrets', 1, 1),
  ('A Game of Thrones', 2, 1),
  ('A Clash of Kings', 2, 1),
  ('The Hobbit', 3, 1),
  ('The Lord of the Rings', 3, 1),
  ('Foundation', 4, 2),
  ('I, Robot', 4, 2),
  ('Murder on the Orient Express', 5, 3),
  ('The Mysterious Affair at Styles', 5, 3),
  ('The Girl with the Dragon Tattoo', 5, 4);


-- 인덱스 추가
CREATE INDEX idx_authors_name
ON authors(id);
CREATE INDEX idx_genres_genre_name
ON genres(id);

-- inner join 조회문
SELECT books.title, authors.name, genres.genre_name
FROM books 
INNER JOIN authors
  ON authors.id = books.author_id
INNER JOIN genres
  ON books.genre_id = genres.id
WHERE authors.name='J.K. Rowling' AND genres.genre_name='Fantasy';