-- snowdata_table_schema.sql
CREATE VIEW combined_weather_stations_data AS
SELECT location, rre150z0, date
FROM VQHA80
UNION ALL
SELECT location, rre150z0, date
FROM VQHA98;

-- combined_data_aggregation.sql
CREATE VIEW TotalPrecipitationData AS
SELECT
    -- one hour
    (SELECT SUM(rre150z0) FROM combined_weather_stations_data WHERE date >= DATETIME('now', '-60 minutes')) AS total_precipitation_last_hour,

    -- 12 hours
    (SELECT SUM(rre150z0) FROM combined_weather_stations_data WHERE date >= DATETIME('now', '-12 hours')) AS total_precipitation_last_12_hours,

    -- 24 hours
    (SELECT SUM(rre150z0) FROM combined_weather_stations_data WHERE date >= DATETIME('now', '-24 hours')) AS total_precipitation_last_24h,

    -- 2 days
    (SELECT SUM(rre150z0) FROM combined_weather_stations_data WHERE date >= DATETIME('now', '-2 days')) AS total_precipitation_last_2_days,

    -- 7 days
    (SELECT SUM(rre150z0) FROM combined_weather_stations_data WHERE date >= DATETIME('now', '-7 days')) AS total_precipitation_last_week,

    -- 30 days
    (SELECT SUM(rre150z0) FROM combined_weather_stations_data WHERE date >= DATETIME('now', '-1 month')) AS total_precipitation_last_month,

    -- all hours combined
    STRFTIME('%Y-%m-%d %H:00:00', date) AS hour_start,
    SUM(rre150z0) AS total_precipitation_per_hour
FROM combined_weather_stations_data
GROUP BY hour_start
ORDER BY hour_start DESC;

