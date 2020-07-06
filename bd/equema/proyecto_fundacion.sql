CREATE TABLE "proyecto_fundacion"
(
    "id" SMALLSERIAL PRIMARY KEY,
    "fundacion" SMALLINT NOT NULL,
    "proyecto" SMALLINT NOT NULL,
    CONSTRAINT "fkFundacion" FOREIGN KEY ("fundacion")
        REFERENCES "fundacion" ("id"),
    CONSTRAINT "fkProyecto" FOREIGN KEY ("proyecto")
        REFERENCES "proyecto" ("id") 
)