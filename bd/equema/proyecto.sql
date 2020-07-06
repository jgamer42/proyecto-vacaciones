CREATE TABLE "proyecto"
(
    "id" SMALLSERIAL PRIMARY KEY,
    "nombre" CHARACTER varying(255) NOT NULL,
    "descripcion" CHARACTER varying(255) NOT NULL,
    "fecha_inicio" DATE NOT NULL,
    "fecha_final" DATE
)
