declare @id int, @Ano int, @Mes int, @MesTemp int 

select Distinct Id, month(created_at) as mes, year(created_at) as ano into #temp from COURSES

create table #SemestreSemCurso(ano int null, semestre varchar(100) null)

WHILE EXISTS (select * from #temp)
BEGIN
	SELECT TOP 1 @Id = id from #temp
    SET @MesTemp = (select mes from #temp where Id = @Id)
	IF @MesTemp BETWEEN 1 and 6
		BEGIN
			SET @Ano = (SELECT ano FROM #temp WHERE Id = @Id)
			INSERT INTO #SemestreSemCurso values (@Ano, 'Primeiro Semestre')
		END
	IF @MesTemp >= 7 
		BEGIN
			SET @Ano = (SELECT ano FROM #temp WHERE Id = @Id)
			INSERT INTO #SemestreSemCurso values (@Ano, 'Segundo Semestre')
		END
    delete FROM #temp where Id = @Id
end

SELECT * FROM #SemestreSemCurso
SELECT * FROM #temp
Drop table #SemestreSemCurso
Drop table #temp