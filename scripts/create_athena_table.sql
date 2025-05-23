CREATE EXTERNAL TABLE IF NOT EXISTS titanic_db.titanic (
  Survived int,
  Pclass int,
  Sex string,
  Age double,
  SibSp int,
  Parch int,
  Fare double,
  Embarked string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'field.delim' = ','
) LOCATION 's3://seu-bucket-titanic/processed/'
TBLPROPERTIES ('has_encrypted_data'='false');
