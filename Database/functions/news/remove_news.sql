CREATE OR REPLACE FUNCTION remove_news(news_id_arg INTEGER, user_id INTEGER) RETURNS VOID AS $$
BEGIN
    IF check_is_admin(user_id) THEN
        DELETE FROM news WHERE news.news_id = news_id_arg;
    END IF;
END;
$$ LANGUAGE plpgsql