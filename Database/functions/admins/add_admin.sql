CREATE OR REPLACE FUNCTION add_admin(user_id INTEGER) RETURNS VOID AS $$
BEGIN
    INSERT INTO admins(user_id) VALUES (user_id);
END;
$$ LANGUAGE plpgsql