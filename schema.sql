CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS atividades(
    ati_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_atividade TEXT NOT NULL,
    descricao_atividade TEXT NOT NULL,
    data_atividade TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);