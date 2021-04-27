SELECT COUNT(*)
FROM match_details m1
INNER JOIN match_details m2
ON m1.match_no = m2.match_no
AND  ABS(m1.goal_score - m2.goal_score) = 1
AND m1.decided_by = 'N'