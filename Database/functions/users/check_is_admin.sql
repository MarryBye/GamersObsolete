CREATE OR REPLACE FUNCTION check_is_admin(user_id_arg INTEGER) RETURNS BOOLEAN AS $$
DECLARE
    is_admin BOOLEAN;
BEGIN
    SELECT EXISTS (
        SELECT admins.user_id 
        FROM admins, users
        WHERE admins.user_id = users.user_id AND user_id_arg = users.user_id
    ) INTO is_admin;

    RETURN is_admin;
END;
$$ LANGUAGE plpgsql