-- script that displays the max temperature of each state
SELECT state, MAX(value) AS max_temp FROM temperature GROUP BY state;
