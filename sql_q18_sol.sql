SELECT match_no, COUNT(*) AS no_fouls FROM player_booked
GROUP BY match_no
ORDER BY no_fouls DESC
LIMIT 1
