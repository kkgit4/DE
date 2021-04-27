SELECT play_stage, COUNT(*)  FROM player_in_out AS p
INNER JOIN match_mast AS m
ON p.match_no = m.match_no
AND p.in_out = 'I'
GROUP BY play_stage