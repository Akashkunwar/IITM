-- Problem Statement: 
-- 1. Q002flisdb: Write an SQL statement to find the name of those managers who became managers after the year '2020'.[Database: FLIS] flisdb:
select name from managers 
    where since > '2020-12-31'

-- 2. Q002flisdb: Write an SQL statement to find the team id and name of the team whose home-jersey color(jersey_home_color) is 'Black'..[Database: FLIS] flisdb:
select team_id, name from teams 
    where jersey_home_color = 'Black'

-- 3. Q005flisdb: Write an SQL statement to find the player name and jersey number of players from the team: 'Rainbow'.[Database: FLIS] flisdb:
select name, jersey_no from players 
    where team_id  in 
    (select team_id from teams 
        where name = 'Rainbow')

-- 4. Q003lisdb: Write an SQL statement to find the first names and dob (student_fname, dob) of students who belong to the department with department code as 'ME' and who were born after '2003-06-15'.[Database: LIS] lisdb:
select student_fname, dob from students 
    where department_code = 'ME' and dob > '2003-06-15'

-- 5. Q001lisdb: Write an SQL statement to find the first names of faculty (faculty_fname) who belong to the department: 'Mechanical Engineering'.
select faculty_fname from faculty 
    where department_code 
    in (select department_code from departments 
        where department_name = 'Mechanical Engineering')