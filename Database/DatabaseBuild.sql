\i Database/check_email.sql
\i Database/check_no_symbols.sql
\i Database/check_is_admin.sql
\i Database/add_admin.sql
\i Database/get_users.sql
\i Database/add_user.sql

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