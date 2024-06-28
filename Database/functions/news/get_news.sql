CREATE OR REPLACE FUNCTION get_news() RETURNS Table(news_id INTEGER, user_id INTEGER, news_title VARCHAR(30), news_description TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT news.news_id, news.user_id, news.news_title, news.news_description FROM news;
END;
$$ LANGUAGE plpgsql