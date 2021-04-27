SELECT referee_id, COUNT(*) AS no_of_bookings FROM player_booked p
INNER JOIN match_mast m 
ON p.match_no = m.match_no
GROUP BY referee_id
ORDER BY no_of_bookings DESC

SELECT m.referee_id, r.referee_name, COUNT(*) AS no_of_bookings FROM player_booked p
INNER JOIN match_mast m 
INNER JOIN referee_mast r
ON p.match_no = m.match_no
AND m.referee_id = r.referee_id
GROUP BY m.referee_id, referee_name
ORDER BY no_of_bookings DESC
