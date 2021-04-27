SELECT player_name FROM player_mast p
INNER JOIN goal_details g
ON p.player_id = g.player_id
AND posi_to_play = 'DF'
ORDER BY player_name