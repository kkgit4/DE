SELECT jersey_no, player_name, playing_club, posi_to_play FROM player_mast p
INNER JOIN soccer_country s
ON p.team_id = s.country_id
AND posi_to_play = 'GK'
AND s.country_abbr = 'ENG'