DROP FUNCTION IF EXISTS get_comments CASCADE;

CREATE OR REPLACE FUNCTION get_comments(news_id_arg INTEGER) RETURNS Table(comment_id INTEGER, user_id INTEGER, comment_text VARCHAR(255)) AS $$
BEGIN
    RETURN QUERY
    SELECT comments.comment_id, comments.user_id, comments.comment_text 
    FROM comments
    WHERE comments.news_id = news_id_arg;
END;
$$ LANGUAGE plpgsql