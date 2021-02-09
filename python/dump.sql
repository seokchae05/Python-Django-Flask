BEGIN TRANSACTION;
CREATE TABLE users(id  INTEGER PRIMARY KEY, username text, email text,     phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'kim','seokchae@naver.com','010-xxxx-1112','lee.com','2021-02-09 14:55:24');
INSERT INTO "users" VALUES(2,'lee','aaa@naver.com','010-xxxx-5666','q.com','2021-02-09 14:55:24');
INSERT INTO "users" VALUES(3,'king','asda@naver.com','010-2222-2222','qa.com','2021-02-09 14:55:24');
INSERT INTO "users" VALUES(4,'g','add@naver.com','010-3333-2132','1.com','2021-02-09 14:55:24');
COMMIT;
