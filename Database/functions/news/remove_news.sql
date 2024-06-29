CREATE OR REPLACE FUNCTION remove_news(news_id_arg INTEGER) RETURNS VOID AS $$
BEGIN
    DELETE FROM news WHERE news_id = news_id_arg;
END;
$$ LANGUAGE plpgsql