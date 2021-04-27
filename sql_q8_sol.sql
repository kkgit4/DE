SELECT * FROM match_details
WHERE match_no = 
(SELECT match_no FROM match_details
ORDER BY penalty_score DESC
LIMIT 1)