DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS admins CASCADE;
DROP TABLE IF EXISTS news CASCADE;
DROP TABLE IF EXISTS comments CASCADE;
DROP TABLE IF EXISTS servers CASCADE;

\i Database/functions/validation/check_email.sql
\i Database/functions/validation/check_no_symbols.sql
\i Database/functions/users/check_is_admin.sql
\i Database/functions/admins/add_admin.sql
\i Database/functions/users/get_users.sql
\i Database/functions/users/add_user.sql
\i Database/functions/news/add_comment.sql
\i Database/functions/news/add_news.sql
\i Database/functions/news/get_news.sql
\i Database/functions/news/remove_comment.sql
\i Database/functions/news/remove_news.sql
\i Database/functions/news/get_comments.sql
\i Database/functions/admins/remove_admin.sql
\i Database/functions/servers/add_server.sql
\i Database/functions/servers/get_servers.sql
\i Database/functions/servers/remove_server.sql

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    user_login VARCHAR(15) UNIQUE NOT NULL,
    user_password VARCHAR(256) NOT NULL,
    user_email VARCHAR(50) UNIQUE,

    CONSTRAINT email_format CHECK (check_email(user_email)),
    CONSTRAINT login_format CHECK (check_no_symbols(user_login))
);

CREATE TABLE IF NOT EXISTS admins (
    admin_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS news (
    news_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    news_title VARCHAR(30),
    news_description TEXT,

    CONSTRAINT admin_check CHECK (check_is_admin(user_id))
);

CREATE TABLE IF NOT EXISTS comments (
    comment_id SERIAL PRIMARY KEY,
    news_id INTEGER REFERENCES news(news_id),
    user_id INTEGER REFERENCES users(user_id),
    comment_text VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS servers (
    server_id SERIAL PRIMARY KEY,
    server_name VARCHAR(64),
    server_version VARCHAR(16),
    server_description TEXT,
    server_ip TEXT,
    server_port TEXT
);