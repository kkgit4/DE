SELECT COUNT(DISTINCT(player_id)) FROM match_captain m
INNER JOIN player_mast p
ON m.player_captain = p.player_id
AND posi_to_play = 'GK'