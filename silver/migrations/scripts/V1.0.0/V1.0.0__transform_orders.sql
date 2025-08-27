CREATE OR REPLACE TABLE {{ database_name }}.{{ schema_name }}.orders_transformed_table_silver AS
SELECT
    order_id,
    customer_id,
    order_date,
    product_id,
    quantity,
    price,
    quantity * price AS total_amount
FROM {{ database_name }}.BRONZE.{{ var('bronze_table') }};
