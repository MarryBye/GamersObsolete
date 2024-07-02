DROP FUNCTION IF EXISTS get_users CASCADE;

CREATE OR REPLACE FUNCTION get_users(reversed BOOLEAN) RETURNS Table(user_id INTEGER, user_login VARCHAR(15), user_email VARCHAR(50)) AS $$
BEGIN
    IF reversed THEN
        RETURN QUERY SELECT users.user_id, users.user_login, users.user_email FROM users ORDER BY users.user_id DESC;
    ELSE
        RETURN QUERY SELECT users.user_id, users.user_login, users.user_email FROM users ORDER BY users.user_id ASC;
    END IF;
END;
$$ LANGUAGE plpgsql