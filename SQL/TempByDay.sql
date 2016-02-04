CREATE 
VIEW `temperature`.`TempByDay` AS
    SELECT 
        `temperature`.`temperatures`.`devicename` AS `devicename`,
        CAST(`temperature`.`temperatures`.`datetimestamp`
            AS DATE) AS `TempDate`,
        DAYOFMONTH(`temperature`.`temperatures`.`datetimestamp`) AS `TempHour`,
        ROUND(MIN((`temperature`.`temperatures`.`curtemp` / 1000)),
                1) AS `MinTemp`,
        ROUND(MAX((`temperature`.`temperatures`.`curtemp` / 1000)),
                1) AS `MaxTemp`,
        ROUND(AVG((`temperature`.`temperatures`.`curtemp` / 1000)),
                1) AS `AVGTemp`
    FROM
        `temperature`.`temperatures`
    GROUP BY `temperature`.`temperatures`.`devicename` , CAST(`temperature`.`temperatures`.`datetimestamp`
        AS DATE) , DAYOFMONTH(`temperature`.`temperatures`.`datetimestamp`)