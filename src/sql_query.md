## SQL Query 

```sql
SELECT
    p.title AS title,
    i.url AS url,
    COALESCE(pd.translatedtext, pd.originaltext) AS product_description
FROM product p
LEFT JOIN product_images pi 
  ON p.id = pi.productid 
  AND pi.imageindex = 0
LEFT JOIN image i 
  ON pi.imageid = i.id
LEFT JOIN product_description pd
  ON p.id = pd.productid 
  AND pd.countrycode = 'us';
```

In the above query, if you want to get only the data that has the matching records in the joined tables, you can use inner join instead of left join.
