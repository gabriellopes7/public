
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

