CREATE OR REPLACE FUNCTION add_news(user_id INTEGER, news_title VARCHAR(30), news_description TEXT) RETURNS VOID AS $$
BEGIN
    INSERT INTO news(user_id, news_title, news_description) VALUES (user_id, news_title, news_description);
END;
$$ LANGUAGE plpgsql