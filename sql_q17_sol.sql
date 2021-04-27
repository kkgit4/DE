SELECT s.country_name, COUNT(*) AS no_of_referees FROM asst_referee_mast a
INNER JOIN soccer_country s
ON a.country_id = s.country_id
GROUP BY s.country_name
ORDER BY no_of_referees DESC