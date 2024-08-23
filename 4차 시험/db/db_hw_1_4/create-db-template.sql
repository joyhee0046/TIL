-- Active: 1724202271611@@127.0.0.1@3306
CREATE DATABASE sns_db
    DEFAULT CHARACTER SET = 'utf8mb4';

USE sns_db;

CREATE TABLE users(
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(255),
  email VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );

CREATE Table posts(
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  content TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(user_id) REFERENCES users(id)
  );

-- 필드 추가
ALTER TABLE users
  ADD COLUMN profile_picture VARCHAR(255);

-- 필드 속성 수정
ALTER TABLE users
  DROP COLUMN email;
ALTER TABLE users
  ADD COLUMN email VARCHAR(320);

-- 필드 추가
ALTER Table posts
  ADD title VARCHAR(255);

--필드 속성 수정
ALTER Table posts
  DROP COLUMN content,
  ADD COLUMN content LONGTEXT;