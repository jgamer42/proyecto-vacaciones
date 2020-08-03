CREATE TABLE "proyecto_fundacion"
(
    "id" SMALLSERIAL PRIMARY KEY,
    "fundacion" SMALLINT NOT NULL,
    "proyecto" SMALLINT NOT NULL,
    CONSTRAINT "fkFundacion" FOREIGN KEY ("fundacion")
        REFERENCES "fundacion" ("id") ON DELETE CASCADE,
    CONSTRAINT "fkProyecto" FOREIGN KEY ("proyecto")
        REFERENCES "proyecto" ("id") ON DELETE CASCADE
)