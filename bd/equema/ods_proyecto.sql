CREATE TABLE "ods_proyecto"
(
    "id" SMALLSERIAL PRIMARY KEY,
    "proyecto" SMALLINT NOT NULL,
    "ods" SMALLINT NOT NULL,
    CONSTRAINT "fkOds" FOREIGN KEY ("ods")
        REFERENCES "ods" ("id") ON DELETE CASCADE,
    CONSTRAINT "fkProyecto" FOREIGN KEY ("proyecto")
        REFERENCES "proyecto" ("id") ON DELETE CASCADE
)