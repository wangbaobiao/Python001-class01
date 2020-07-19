# 1. SELECT * FROM data;
## 方式一：
import pymysql
import numpy as np
import pandas as pd
sql = 'SELECT *  FROM BOOK'
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'P@ssw0rd',
    'database': 'mybook',
    'charset': 'utf8mb4'
}
conn = pymysql.connect(**config)
# conn = pymysql.connect('ip', 'name', 'pass', 'dbname', 'charset=utf8')
df1 = pd.read_sql(sql, conn)
print(df1)

## 方式二：
group =['x','y']
df=pd.DataFrame({'group':np.random.randint(0,50,15),
                   'id':np.random.randint(0,15,15),
                   'age': np.random.randint(0,60,15),
                   'high': np.random.randint(0,2,15),
                   })
print(df)



# 2. SELECT * FROM data LIMIT 10;
df.head(10)
# print(df.head(10))

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
# df["id"]
# print(df["id"])

# 4. SELECT COUNT(id) FROM data;
df.count()
## 这个是统计行列数量
df.shape
# print(df.shape)

# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df[ ( df['id']<1000 ) & ( df['age']>30 ) ]
# print(df[ ( df['id']<1000 ) & ( df['age']>30 ) ])

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
table1 = pd.DataFrame({
    "id":np.random.randint(0,2000,10),
    "order_id":np.random.randint(0,60,10),
    "age":np.random.randint(15,70,10)
    })
## 方式一
print(table1.groupby('id').agg({'order_id':pd.Series.nunique}))#分组计数

## 方式二
table=table1.drop_duplicates(subset='order_id',keep='first')
table= table.groupby('id').aggregate({'order_id':'count',})
print(table)

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
table1 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10)
    })

table2 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "salary":np.random.randint(5,50,10),
    })

pd.merge(table1, table2, on= 'id', how='inner')
# print(pd.merge(table1, table2, on= 'id', how='inner'))

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
table1 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(15,50,10)
    })

table2 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "age":np.random.randint(5,50,10),
    })
pd.merge(table1, table2)

# 9. DELETE FROM table1 WHERE id=10;
table1[table1['id']!=10]

# 10. ALTER TABLE table1 DROP COLUMN column_name;
table1 = pd.DataFrame({
    "id":[group[x] for x in np.random.randint(0,len(group),10)] ,
    "column_name":np.random.randint(15,50,10)
    })
table1.drop('column_name',axis=1)
