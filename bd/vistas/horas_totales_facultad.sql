CREATE VIEW vista_facultad AS
SELECT "facultad"."nombre",  SUM("actividad"."duracion") AS HORA
FROM "facultad", "programa", "voluntario", "actividad", "actividad_voluntario"
WHERE "facultad"."id" = "programa"."facultad"  
AND "voluntario"."programa" = "programa"."id" 
AND "voluntario"."cedula" = "actividad_voluntario"."voluntario"
AND "actividad"."id" = "actividad_voluntario"."actividad"
GROUP BY "facultad"."nombre";