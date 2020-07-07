
CREATE TABLE "actividad"
(
    "id" SMALLSERIAL PRIMARY KEY,
    "voluntario" CHARACTER  varying(255),
    "proyecto" SMALLINT NOT NULL,
    "nombre" CHARACTER varying(255) NOT NULL,
    "descripcion" CHARACTER varying(255) NOT NULL,
    "duracion" INTEGER NOT NULL,
    "fecha" DATE NOT NULL,
    CONSTRAINT "proyecto" FOREIGN KEY ("proyecto")
        REFERENCES "proyecto" ("id"),
    CONSTRAINT "voluntario" FOREIGN KEY ("voluntario")
        REFERENCES "voluntario" ("cedula") ON DELETE CASCADE
)