DROP FUNCTION IF EXISTS get_servers CASCADE;

CREATE OR REPLACE FUNCTION get_servers() RETURNS Table(server_id INTEGER, server_name VARCHAR(64), server_version VARCHAR(16), server_description TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT servers.server_id, servers.server_name, servers.server_version, servers.server_description FROM servers;
END;
$$ LANGUAGE plpgsql