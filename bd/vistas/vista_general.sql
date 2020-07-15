CREATE VIEW vista_general AS
SELECT "facultad"."nombre" AS facultad, "programa"."nombre" AS programa, "voluntario"."nombre" AS nombre,"voluntario"."apellido" AS apellido, "actividad"."fecha", "actividad"."nombre" AS actividad, "actividad"."descripcion", "actividad"."duracion"
FROM "facultad", "programa", "voluntario", "actividad","actividad_voluntario"
WHERE "facultad"."id" = "programa"."facultad"  
AND "voluntario"."programa" = "programa"."id" 
AND "actividad_voluntario"."voluntario" = "voluntario"."cedula"
AND "actividad"."id" = "actividad_voluntario"."actividad";