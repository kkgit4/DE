SELECT m.referee_id, venue_id, COUNT(*) AS no_matches_worked FROM referee_mast r
INNER JOIN match_mast m
ON r.referee_id = m.referee_id
GROUP BY m.referee_id, venue_id
ORDER BY m.referee_id