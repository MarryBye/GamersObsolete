DROP FUNCTION IF EXISTS add_server CASCADE;

CREATE OR REPLACE FUNCTION add_server(server_name VARCHAR(64), server_version VARCHAR(16), server_description TEXT, user_id INTEGER) RETURNS VOID AS $$
BEGIN
    IF check_is_admin(user_id) THEN
        INSERT INTO servers(server_name, server_version, server_description) VALUES (server_name, server_version, server_description);
    END IF;
END;
$$ LANGUAGE plpgsql