
CREATE TABLE "voluntario"
(
    "cedula" CHARACTER varying(255)  PRIMARY KEY,
    "nombre" CHARACTER varying(255)  NOT NULL,
    "apellido" CHARACTER varying(255) NOT NULL,
    "genero" CHARACTER varying(50) NOT NULL,
    "programa" SMALLINT NOT NULL,
    "correo" CHARACTER varying(255) NOT NULL,
    "telefono" CHARACTER varying(255) ,
    CONSTRAINT "programa" FOREIGN KEY ("programa")
        REFERENCES "programa" ("id") 
)