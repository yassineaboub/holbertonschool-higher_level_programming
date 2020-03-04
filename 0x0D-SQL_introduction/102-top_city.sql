-- script that displays the top 3 of cities temperature during July and August
SELECT TOP 3 city,
AVG(value) as avg_temp
FROM temperatures
WHERE MONTH(7) OR MONTH(8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

