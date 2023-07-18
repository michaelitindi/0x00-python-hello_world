-- listing except those names that are empty
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
