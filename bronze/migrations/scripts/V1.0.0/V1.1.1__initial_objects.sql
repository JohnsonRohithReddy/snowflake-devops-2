USE DATABASE {{ var.database }};
USE SCHEMA {{ var.schema }};

CREATE TABLE IF NOT EXISTS {{ var.schema }}.HELLO_WORLD_4_45 (
    FIRST_NAME VARCHAR,
    LAST_NAME VARCHAR
);
