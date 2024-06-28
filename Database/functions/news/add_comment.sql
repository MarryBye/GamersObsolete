CREATE OR REPLACE FUNCTION add_comment(news_id INTEGER, user_id INTEGER, comment_text VARCHAR(255)) RETURNS VOID AS $$
BEGIN
    INSERT INTO comments(news_id, user_id, comment_text) VALUES (news_id, user_id, comment_text);
END;
$$ LANGUAGE plpgsql