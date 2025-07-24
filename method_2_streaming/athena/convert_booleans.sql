SELECT *,
       IF(arrest = true, 'True', 'False') AS arrest_label,
       IF(domestic = true, 'True', 'False') AS domestic_label
FROM chicago_crime;
