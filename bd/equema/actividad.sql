
CREATE TABLE "actividad"
(
    "id" SMALLSERIAL PRIMARY KEY,
    "proyecto" SMALLINT NOT NULL,
    "nombre" CHARACTER varying(255) NOT NULL,
    "descripcion" CHARACTER varying(255) NOT NULL,
    "duracion" INTEGER NOT NULL,
    "fecha" DATE NOT NULL,
    CONSTRAINT "proyecto" FOREIGN KEY ("proyecto")
        REFERENCES "proyecto" ("id") ON DELETE CASCADE
)