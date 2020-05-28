# Mysql

## Mysql 5.6

### Query to identify tables with over 1GB of free space (ready to use PTOSC to clean)

    select TABLE_NAME, DATA_LENGTH / 1024 / 1024 / 1024 as data_gb, INDEX_LENGTH / 1024 / 1024 / 1024 as index_gb, DATA_FREE / 1024 / 1024 / 1024 as free_gb from information_schema.TABLES where DATA_FREE > 1073741824 order by DATA_FREE DESC;

### Query to identify tables where the index is longer than the data

    select TABLE_NAME, DATA_LENGTH / 1024 / 1024 / 1024 as data_gb, INDEX_LENGTH / 1024 / 1024 / 1024 as index_gb from information_schema.TABLES where TABLE_SCHEMA = 'DB-to-query' and INDEX_LENGTH > DATA_LENGTH order by INDEX_LENGTH DESC;
