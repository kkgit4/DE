SELECT * FROM player_mast
WHERE player_id = (
SELECT DISTINCT(m.player_gk) FROM soccer_country s
INNER JOIN match_details m
ON s.country_id = m.team_id
AND country_abbr = 'GER'
AND play_stage = 'G')