DROP FUNCTION IF EXISTS get_comments CASCADE;

CREATE OR REPLACE FUNCTION get_comments(news_id_arg INTEGER, reversed BOOLEAN) RETURNS Table(comment_id INTEGER, user_id INTEGER, comment_text VARCHAR(255)) AS $$
BEGIN
    IF reversed THEN
        RETURN QUERY
        SELECT comments.comment_id, comments.user_id, comments.comment_text 
        FROM comments
        WHERE comments.news_id = news_id_arg ORDER BY comments.comment_id DESC;
    ELSE
        RETURN QUERY
        SELECT comments.comment_id, comments.user_id, comments.comment_text 
        FROM comments
        WHERE comments.news_id = news_id_arg ORDER BY comments.comment_id ASC;
    END IF;
END;
$$ LANGUAGE plpgsql