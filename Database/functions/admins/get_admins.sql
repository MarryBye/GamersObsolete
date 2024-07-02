DROP FUNCTION IF EXISTS get_admins CASCADE;

CREATE OR REPLACE FUNCTION get_admins(reversed BOOLEAN) RETURNS Table(user_id INTEGER, user_login VARCHAR(15), user_email VARCHAR(50)) AS $$
BEGIN
    IF reversed THEN
        RETURN QUERY
        SELECT admins.user_id, users.user_login, users.user_email FROM users, admins WHERE admins.user_id = users.user_id ORDER BY admins.admin_id DESC;
    ELSE 
        RETURN QUERY
        SELECT admins.user_id, users.user_login, users.user_email FROM users, admins WHERE admins.user_id = users.user_id ORDER BY admins.admin_id ASC;
    END IF;
END;
$$ LANGUAGE plpgsql