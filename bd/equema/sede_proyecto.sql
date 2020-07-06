CREATE TABLE "sede_proyecto"
(
    "id" SMALLSERIAL PRIMARY KEY,    
    "proyecto" SMALLINT NOT NULL,
    "sede" SMALLINT NOT NULL,
    CONSTRAINT "fkProyecto" FOREIGN KEY ("proyecto")
        REFERENCES "proyecto" ("id"),
    CONSTRAINT "fkSede" FOREIGN KEY ("sede")
        REFERENCES "sede" ("id")
)