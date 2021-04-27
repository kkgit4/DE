SELECT posi_to_play, COUNT(*) FROM player_mast p
INNER JOIN goal_details g
ON p.player_id = g.player_id
GROUP BY posi_to_play


-- Country and by position
-- -----------------------
SELECT country_name, posi_to_play, COUNT(*)  FROM player_mast p
INNER JOIN goal_details g
INNER JOIN soccer_country s
ON p.player_id = g.player_id
AND p.team_id = s.country_id
GROUP BY country_name,  posi_to_play
ORDER BY country_name