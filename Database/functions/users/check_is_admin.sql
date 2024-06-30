CREATE OR REPLACE FUNCTION check_is_admin(user_id_arg INTEGER) RETURNS BOOLEAN AS $$
DECLARE
    is_admin BOOLEAN;
BEGIN
    SELECT EXISTS (
        SELECT admins.user_id 
        FROM admins
        WHERE admins.user_id = user_id_arg
    ) INTO is_admin;

    RETURN is_admin;
END;
$$ LANGUAGE plpgsql