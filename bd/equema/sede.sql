CREATE TABLE "sede"
(
    "id" SMALLSERIAL PRIMARY KEY,    
    "nombre" CHARACTER varying(255) NOT NULL,
    "director" CHARACTER varying(255) NOT NULL,
    "direccion" CHARACTER varying(255) NOT NULL,
    "telefono" CHARACTER varying(255) NOT NULL
)