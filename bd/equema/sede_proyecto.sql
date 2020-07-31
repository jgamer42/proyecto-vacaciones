CREATE TABLE "sede_proyecto"
(
    "id" SMALLSERIAL PRIMARY KEY,    
    "proyecto" SMALLINT NOT NULL,
    "sede" SMALLINT NOT NULL,
    CONSTRAINT "fkProyecto" FOREIGN KEY ("proyecto")
        REFERENCES "proyecto" ("id") ON DELETE CASCADE,
    CONSTRAINT "fkSede" FOREIGN KEY ("sede")
        REFERENCES "sede" ("id") ON DELETE CASCADE
)