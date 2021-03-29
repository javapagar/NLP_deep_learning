from sqlite import SqliteDB
createQuestions ="CREATE TABLE IF NOT EXISTS questions(\
            id INTEGER PRIMARY KEY,\
            title text NOT NULL,\
            content text NULL,\
            link text NOT NULL,\
            answer text NULL)"

dropQuestions ="Drop TABLE questions"

createIntermediate = "CREATE TABLE IF NOT EXISTS questions_tags(\
            id_question INTEGER NOT NULL,\
            id_tag INTEGER NOT NULL,\
            FOREIGN KEY(id_question) REFERENCES questions(id) ON DELETE CASCADE,\
            FOREIGN KEY(id_tag) REFERENCES tags(id) ON DELETE CASCADE)"
dropQuestionsTags ="Drop TABLE questions_tags"
createTags = "CREATE TABLE IF NOT EXISTS tags(\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            tag text NOT NULL)"
dropTags ="Drop TABLE tags"
insertReg ="INSERT INTO questions(id,title, content, link, answer) VALUES (?,?,?, ?, ?)"

deleteQuestions = "DELETE FROM questions"

insertTag = "INSERT INTO tags (tag) VALUES (?)"

selectTag = "SELECT * FROM tags WHERE tag = ?"

queryParams=('python',)
script = [("INSERT INTO questions(id,title, content, link, answer) VALUES (?,?,?,?,?)",[1,'hola','hola', 'hola', 'hola']),("INSERT INTO questions(id,title, content, link, answer) VALUES (?,?,?,?,?)",[2,'hola','hola', 'hola', 'hola'])]
db = SqliteDB('db/Stackoverflow.db')
db.connect()
resp = db.executeQuery(deleteQuestions)

db.close()
