-- Problem Statement: 
-- 1. Q004flisdb: Write an SQL statement to find the match number of the match held on '2020-05-15' and the name of the fourth referee who refereed that match. Print match_num first, followed by respective fourth referee name. Note: fourth referee is to be obtained from the 'fourth_referee' attribute.[Database: FLIS] flisdb:
select m.match_num, r.name from matches as m left join match_referees as mr on m.match_num = mr.match_num left join referees as r on mr.fourth_referee = r.referee_id where m.match_date = '2020-05-15'

-- 2. Q004flisdb: Write an SQL statement to find the name of the eldest player in the team named 'Arawali'.[Database: FLIS] flisdb:
select name from players where dob in (select min(dob) from players where team_id in (select team_id from teams where name = 'Arawali'))

-- 3. Q003flisdb: Write an SQL statement to find the name and dob of the players who belongs from the team names 'Amigos' or 'Black Eagles'. flisdb:
select name, dob from players where team_id in (select team_id from teams where name = 'Amigos' or name = 'Black Eagles')

-- 4. Q005lisdb: Write an SQL statement to find department_code and member_type of the students who have issued (borrowed) books on '2021-08-02'. lisdb:
select d.department_code, m.member_type from 
(select * from members where member_no in 
(select member_no from book_issue where doi = '2021-08-02')) as m 
left join students as s on s.roll_no = m.roll_no 
left join departments as d on d.department_code = s.department_code

-- 5. Q002lisdb: Write an SQL statement to find the book titles and the number of copies of the books which has the word 'Management' in their title.[Database: LIS] lisdb:
select title, count(*)
from book_catalogue as b join book_copies as c
on b.isbn_no = c.isbn_no
where title like '%Management%' group by title