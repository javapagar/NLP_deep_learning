#questions table
CREATE_QUESTIONS ="CREATE TABLE IF NOT EXISTS questions(\
            id INTEGER PRIMARY KEY,\
            title text NOT NULL,\
            content text NULL,\
            link text NOT NULL,\
            answer text NULL)"
INSERT_QUESTIONS_REDUCED ="INSERT INTO questions(id,title,link) VALUES (?,?,?)"

INSERT_QUESTIONS ="INSERT INTO questions(id,title, content, link, answer) VALUES (?,?,?, ?, ?)"

DELETE_QUESTIONS = "DELETE FROM questions"

FIND_QUESTION ="SELECT * FROM questions WHERE id = ?"

#intermediate table
CREATE_QUESTIONS_TAGS = "CREATE TABLE IF NOT EXISTS questions_tags(\
            id_question INTEGER NOT NULL,\
            id_tag INTEGER NOT NULL,\
            FOREIGN KEY(id_question) REFERENCES questions(id) ON DELETE CASCADE,\
            FOREIGN KEY(id_tag) REFERENCES tags(id) ON DELETE CASCADE)"

INSERT_QUESTION_TAG = "INSERT INTO questions_tags (id_question,id_tag) VALUES (?,?)"

#tag table
CREATE_TAG = "CREATE TABLE IF NOT EXISTS tags(\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            tag text NOT NULL)"

FIND_TAG ="SELECT * FROM tags WHERE tag = ?"

INSERT_TAG = "INSERT INTO tags (tag) VALUES (?)"


