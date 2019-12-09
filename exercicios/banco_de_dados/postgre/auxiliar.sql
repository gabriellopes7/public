--function receita bruta
create or replace function fn_receita_bruta() returns decimal
    language plpgsql
as
$$

BEGIN

   RETURN (
	  select cast(sum(sale_value_brl) as decimal(10,2))
		from enrollments
		where course_id = (select course_id 
							from enrollments
							group by course_id
							having count(user_id) = (select max(alunos)
													from (select count(user_id) as alunos
														  from enrollments
														  group by course_id) as max_alunos))
   );
   
END;
$$;


--function custo

create or replace function fn_custo() returns decimal
    language plpgsql
as
$$

BEGIN

   RETURN (
	  select (select max(alunos)
		from (select count(user_id) as alunos
			from enrollments
			group by course_id) as max_alunos) *(select course_cost_brl
												from courses c, enrollments e
												where c.id = e.course_id
												group by c.id
												having c.id = (select course_id 
																from enrollments
																group by course_id
																having count(user_id) = (select max(alunos)
																						  from (select count(user_id) as alunos
																								from enrollments
																								group by course_id) as max_alunos)))
   );
   
END;
$$;


--view dos cursos com discriminacao de cursos
create or replace view vw_courses
as
	  select *,
			(
				CASE 
					WHEN cast(date_part('month', created_at) as int) > 6 THEN 2
					ELSE 1
				END
			) as semester,
			cast(date_part('year', created_at) as int) as year
		from courses


--selects das funcoes e views
select fn_receita_bruta()
select fn_custo()
select * from vw_semester


--receita liquida
select (fn_receita_bruta() - fn_custo()) as receita_liquida



loop 
declare cr_courses
	cr_courses := select * from vw_courses
	open cr_courses
		begin
		local_year := 2000
			loop 
			local_year:=local_year+ 1 -- colocar condição de parada local_year <= (date_part('year', now())
				if (cr_courses.semester = 1  or cr_courses.semester = 2) and cr_courses.year = local_year
					begin
						existe						
					end
				else if cr_courses.semester = 1 and cr_courses.year = local_year
					begin
						PRINT 'semestre 2'						
					end
				else if cr_courses.semester = 2 and cr_courses.year = local_year
					begin
						PRINT 'semestre 1'						
					end
				else 
					begin
						PRINT cr_courses.year
						PRINT 'semestre 1'
						PRINT 'semestre 2'
					end
				
			loop end
		loop end
		



COPY
(
    
	select e.created_at - c.created_at as datas
	from enrollments e left join courses c on e.course_id = c.id
	
)
TO 'D:\Documentos\select2.csv'
DELIMITER ';'
CSV HEADER