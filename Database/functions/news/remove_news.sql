DROP FUNCTION IF EXISTS remove_news CASCADE;

CREATE OR REPLACE FUNCTION remove_news(news_id_arg INTEGER, user_id INTEGER) RETURNS VOID AS $$
BEGIN
    IF check_is_admin(user_id) THEN
        DELETE FROM comments WHERE comments.news_id = news_id_arg;
        DELETE FROM news WHERE news.news_id = news_id_arg;
    END IF;
END;
$$ LANGUAGE plpgsql