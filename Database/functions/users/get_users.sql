CREATE OR REPLACE FUNCTION get_users() RETURNS Table(user_id INTEGER, user_login VARCHAR(15), user_email VARCHAR(50)) AS $$
BEGIN
    RETURN QUERY SELECT users.user_id, users.user_login, users.user_email FROM users;
END;
$$ LANGUAGE plpgsql