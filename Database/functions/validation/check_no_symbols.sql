DROP FUNCTION IF EXISTS check_no_symbols CASCADE;

CREATE OR REPLACE FUNCTION check_no_symbols(txt TEXT) RETURNS BOOLEAN AS $$
BEGIN
    RETURN txt ~* '^[a-zA-Z0-9_]+$';
END;
$$ LANGUAGE plpgsql