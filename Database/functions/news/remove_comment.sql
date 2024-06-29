CREATE OR REPLACE FUNCTION remove_comment(comment_id_arg INTEGER) RETURNS VOID AS $$
BEGIN
    DELETE FROM comments WHERE comment_id = comment_id_arg;
END;
$$ LANGUAGE plpgsql