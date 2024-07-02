DROP FUNCTION IF EXISTS get_news CASCADE;

CREATE OR REPLACE FUNCTION get_news(reversed BOOLEAN) RETURNS Table(news_id INTEGER, user_id INTEGER, news_title VARCHAR(30), news_description TEXT) AS $$
BEGIN
    IF reversed THEN
        RETURN QUERY
        SELECT news.news_id, news.user_id, news.news_title, news.news_description FROM news ORDER BY news.news_id DESC;
    ELSE 
        RETURN QUERY
        SELECT news.news_id, news.user_id, news.news_title, news.news_description FROM news ORDER BY news.news_id ASC;
    END IF;
END;
$$ LANGUAGE plpgsql