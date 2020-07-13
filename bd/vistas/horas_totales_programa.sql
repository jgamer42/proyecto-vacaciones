CREATE VIEW vista_programa AS
SELECT "programa"."nombre",  SUM("actividad"."duracion") AS HORA
FROM "programa", "voluntario", "actividad", "actividad_voluntario"
WHERE "voluntario"."programa" = "programa"."id"
AND "voluntario"."cedula" = "actividad_voluntario"."voluntario"
AND "actividad"."id" = "actividad_voluntario"."id"
GROUP BY "programa"."nombre"