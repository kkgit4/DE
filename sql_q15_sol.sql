SELECT referee_id, COUNT(*) AS no_of_bookings FROM player_booked p
INNER JOIN match_mast m 
ON p.match_no = m.match_no
GROUP BY referee_id
ORDER BY no_of_bookings DESC