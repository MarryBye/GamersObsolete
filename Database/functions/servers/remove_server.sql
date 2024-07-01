DROP FUNCTION IF EXISTS remove_server CASCADE;

CREATE OR REPLACE FUNCTION remove_server(server_id_arg INTEGER, user_id INTEGER) RETURNS VOID AS $$
BEGIN
    IF check_is_admin(user_id) THEN
        DELETE FROM servers WHERE servers.server_id = server_id_arg;
    END IF;
END;
$$ LANGUAGE plpgsql