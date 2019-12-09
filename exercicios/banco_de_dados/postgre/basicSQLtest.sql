--1. Qual é o domínio de email mais comum dos usuários inscritos? 
select right(email, length(email) - position('@' in email) ) as dominio
from users
group by right(email, length(email) - position('@' in email) )
having count(*) = (select max(contador)
					from (select count(*) as contador, right(email, length(email) - position('@' in email) )
					  	  from users
					  	  group by right(email, length(email) - position('@' in email) )
				      	  order by 1 desc) as tipo);				


--2. Quantos usuários cadastrados possuem primeiros nomes compostos?
select count(id) as nomes_compostos
from users
where first_name like '% %' 
or first_name like '%-%';

--3. Qual é o percentual de usuários que preencheu todas as informações pessoais do cadastro?
select cast(((select cast(count(id)*100 as decimal(10,2))
					from users
					where first_name is not null
					and last_name is not null
					and email is not null
					and gender is not null)/(select cast(count(id) as decimal(10,2))
											from users)) as decimal(10,2)) as "porcentagem preenchida %";
											
					
--4. Qual o percentual de usuários na base que nunca se matriculou em nenhum curso?					
select cast((select cast(count(id)*100 as decimal(10,2))
				from users
				where id not in (select user_id
								 from enrollments))/
				(select cast(count(id) as decimal(10,2))
				from users) as decimal(10,2)) as nao_matriculou;
			
--5. Qual foi a receita bruta (receita total) do curso com a maior quantidade de alunos inscritos? 
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
select fn_receita_bruta();

--5 E a receita líquida (receita bruta - custo)?**ajustar
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
select (fn_receita_bruta() - fn_custo()) as receita_liquida;

--6. Qual curso atingiu o maior número de matrículas nos primeiros 90 dias de lançamento?
select c.course_name
from enrollments e left join courses c on e.course_id = c.id
where e.created_at - c.created_at <= 90
and e.created_at >= c.created_at
group by course_name
having count(course_id) = (select max(cursos)
				   			from (select count(course_id) as cursos
								  from enrollments x left join courses y on x.course_id = y.id
								  where x.created_at - y.created_at <= 90
								  and x.created_at >= y.created_at --Na tabela cursos, haviam cursos criados após as datas das matrículas
								  group by course_id) as max_cursos);
								  			
--7. Qual é o curso que obteve, em média, as melhores margens de lucro no primeiro semestre de 2019?
select course_name
from courses
where id = (select course_id
					from enrollments e left join courses c on c.id = e.course_id
					where e.created_at between to_date('01/01/2019','DD/MM/YYYY') 
										and to_date('30/06/2019','DD/MM/YYYY')
					group by course_id
					having avg(sale_value_brl-course_cost_brl) = (select max(margem)
																  from (select avg(sale_value_brl-course_cost_brl) as margem
																		from enrollments x left join courses y on y.id = x.course_id
																		where x.created_at between to_date('01/01/2019','DD/MM/YYYY')
																							and to_date('30/06/2019','DD/MM/YYYY')
																		group by course_id) as media_maxima));


--8. Desafio - Qual semestre a Rock Contente não lançou um curso novo

create or replace function semestre_sem_curso()
returns table(sem integer, an text) as $$

DECLARE
 --cursor
 	  j integer;
      i date;
	  anoVar double precision;

begin

			
	--criando tabela temporaria anos
	
	create temporary table anos
	(ano date null CONSTRAINT year_must_be_1st_jan CHECK ( date_trunc('year', ano) = ano ), 
	 semestre int null);
	 
	 anoVar := 2015;
	--inserindo valores na tabela temporaria
	for anoVar in select extract(year from created_at) from courses
	loop
	 insert into anos values
	 	
		(to_date(cast(anoVar as text), 'YYYY'), 1), 
		(to_date(cast(anoVar as text), 'YYYY'), 2);
		anoVar := anoVar + 1;
	end loop;
	j := 0;
	
	for j,i in select id, created_at from courses 
        loop
			j:= j+1;
            if (select cast(date_part('month', created_at) as int) from courses where id = j) <= 6 then
                delete from anos where semestre = 1 and date_part('year', ano) =  (select date_part('year', created_at) from courses where id = j);
            elsif (select cast(date_part('month', created_at) as int) from courses where id = j) > 6 then
                delete from anos where semestre = 2 and date_part('year', ano) =  (select date_part('year', created_at) from courses where id = j);
            end if;
        end loop;
	return query select semestre, cast(to_char(ano,'YYYY') as text) from anos;	
	drop table anos;
end; 
$$ language plpgsql;

select distinct semestre_sem_curso();