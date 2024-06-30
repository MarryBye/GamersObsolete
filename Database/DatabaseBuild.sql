DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS admins CASCADE;
DROP TABLE IF EXISTS news CASCADE;
DROP TABLE IF EXISTS comments CASCADE;

DROP FUNCTION IF EXISTS check_email CASCADE;
DROP FUNCTION IF EXISTS check_no_symbols CASCADE;
DROP FUNCTION IF EXISTS check_is_admin CASCADE;
DROP FUNCTION IF EXISTS add_admin CASCADE;
DROP FUNCTION IF EXISTS get_users CASCADE;
DROP FUNCTION IF EXISTS add_user CASCADE;
DROP FUNCTION IF EXISTS add_comment CASCADE;
DROP FUNCTION IF EXISTS add_news CASCADE;
DROP FUNCTION IF EXISTS get_news CASCADE;
DROP FUNCTION IF EXISTS remove_comment CASCADE;
DROP FUNCTION IF EXISTS remove_news CASCADE;
DROP FUNCTION IF EXISTS get_comments CASCADE;
DROP FUNCTION IF EXISTS remove_admin CASCADE;

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
)