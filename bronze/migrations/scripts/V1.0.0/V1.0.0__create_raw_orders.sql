CREATE TABLE IF NOT EXISTS {{ database_name }}.{{ schema_name }}.orders_raw_table (
    order_id STRING,
    customer_id STRING,
    order_date DATE,
    product_id STRING,
    quantity NUMBER,
    price NUMBER
);
