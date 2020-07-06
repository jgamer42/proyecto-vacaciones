CREATE TABLE "programa"
(
    "id" SMALLSERIAL PRIMARY KEY,
    "nombre" CHARACTER varying(255) NOT NULL,
    "facultad" SMALLINT,
    CONSTRAINT "fkFacultad" FOREIGN KEY ("facultad")
        REFERENCES "facultad" ("id")
)