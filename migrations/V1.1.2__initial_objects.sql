-- Use idempotent syntax to avoid errors if schema exists
CREATE SCHEMA IF NOT EXISTS {{ schema_name }};

-- Create or replace table to ensure it’s in the right schema
CREATE OR REPLACE TABLE {{ database_name }}.{{ schema_name }}.HELLO_WORLD_test_22
(
   FIRST_NAME VARCHAR
  ,LAST_NAME VARCHAR
);
