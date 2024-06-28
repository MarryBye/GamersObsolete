CREATE OR REPLACE FUNCTION add_user(user_login VARCHAR(15), user_password VARCHAR(256), user_email VARCHAR(50)) RETURNS VOID AS $$
BEGIN
    INSERT INTO users(user_login, user_password, user_email) VALUES (user_login, user_password, user_email);
END;
$$ LANGUAGE plpgsql