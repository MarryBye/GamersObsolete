DROP FUNCTION IF EXISTS remove_comment CASCADE;

CREATE OR REPLACE FUNCTION remove_comment(comment_id_arg INTEGER, user_id INTEGER) RETURNS VOID AS $$
BEGIN
    IF check_is_admin(user_id) THEN
        DELETE FROM comments WHERE comments.comment_id = comment_id_arg;
    END IF;
END;
$$ LANGUAGE plpgsql