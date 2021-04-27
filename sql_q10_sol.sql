SELECT * FROM player_mast p
INNER JOIN soccer_country s
ON p.team_id = s.country_id
AND playing_club = 'Liverpool'
AND s.country_abbr = 'ENG'