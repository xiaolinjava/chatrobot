BEGIN;
CREATE TABLE "books_publisher" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL,
    "address" varchar(50) NOT NULL,
    "city" varchar(60) NOT NULL,
    "state_province" varchar(30) NOT NULL,
    "country" varchar(50) NOT NULL,
    "website" varchar(200) NOT NULL
)
;
CREATE TABLE "books_author" (
    "id" integer NOT NULL PRIMARY KEY,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(40) NOT NULL,
    "email" varchar(75) NOT NULL
)
;
CREATE TABLE "books_book_authors" (
    "id" integer NOT NULL PRIMARY KEY,
    "book_id" integer NOT NULL,
    "author_id" integer NOT NULL REFERENCES "books_author" ("id"),
    UNIQUE ("book_id", "author_id")
)
;
CREATE TABLE "books_book" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(100) NOT NULL,
    "publisher_id" integer NOT NULL REFERENCES "books_publisher" ("id"),
    "publication_date" date NOT NULL
)
;
CREATE INDEX "books_book_22dd9c39" ON "books_book" ("publisher_id");
COMMIT;

BEGIN;
CREATE TABLE "qAnda_qanda" (
    "id" integer NOT NULL PRIMARY KEY,
    "question" varchar(100) NOT NULL,
    "answer" varchar(100) NOT NULL
)
;
COMMIT;
