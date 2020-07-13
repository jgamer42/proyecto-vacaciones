CREATE TABLE "actividad_voluntario"
(
    "id" SMALLSERIAL PRIMARY KEY,
    "voluntario" character varying(255),
    "actividad" smallint,
    CONSTRAINT "fkActividad" FOREIGN KEY ("actividad")
        REFERENCES "actividad" ("id")
        ON DELETE CASCADE,
    CONSTRAINT "fkVoluntario" FOREIGN KEY ("voluntario")
        REFERENCES "voluntario" ("cedula")
        ON DELETE CASCADE
);