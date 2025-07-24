SELECT district,
       COUNT(*) AS violent_night_crimes
FROM chicago_crime
WHERE primary_type IN ('ASSAULT', 'BATTERY', 'ROBBERY', 'HOMICIDE', 'CRIMINAL SEXUAL ASSAULT')
  AND hour(CAST(date AS timestamp)) BETWEEN 20 AND 23 -- 8 PM to 11 PM
  OR hour(CAST(date AS timestamp)) BETWEEN 0 AND 4    -- midnight to 4 AM
GROUP BY district
ORDER BY violent_night_crimes DESC;
