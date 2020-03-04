-- script that displays the max temperature of each state
SELECT hbtn_0c_0, MAX(value) AS max_temp FROM temperature GROUP BY state;
