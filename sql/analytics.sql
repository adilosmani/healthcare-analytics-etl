-- Visits by department + average duration
SELECT
  department,
  COUNT(*) AS visit_count,
  ROUND(AVG(visit_duration_hours), 2) AS avg_duration_hours,
  ROUND(AVG(cost), 2) AS avg_cost
FROM visits
GROUP BY department
ORDER BY visit_count DESC;

-- Top 3 most expensive visits
SELECT visit_id, department, cost
FROM visits
ORDER BY cost DESC
LIMIT 3;
