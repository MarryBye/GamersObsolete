DROP FUNCTION IF EXISTS remove_admin CASCADE;

CREATE OR REPLACE FUNCTION remove_admin(user_id_arg INTEGER) RETURNS VOID AS $$
BEGIN
    IF check_is_admin(user_id) THEN
        DELETE FROM admins WHERE admins.user_id = user_id_arg;
    END IF;
END;
$$ LANGUAGE plpgsql