CREATE OR REPLACE TABLE {{ database_name }}.{{ schema_name }}.orders_gold_table AS
SELECT
    customer_id,
    SUM(total_amount) AS total_spent,
    COUNT(DISTINCT order_id) AS orders_count
FROM {{ database_name }}.SILVER.{{ var('silver_table') }}
GROUP BY customer_id;
