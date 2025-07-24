CREATE EXTERNAL TABLE chicago_crime (
  id STRING,
  case_number STRING,
  date STRING,
  block STRING,
  iucr STRING,
  primary_type STRING,
  description STRING,
  location_description STRING,
  arrest BOOLEAN,
  domestic BOOLEAN,
  beat STRING,
  district STRING,
  ward STRING,
  community_area STRING,
  fbi_code STRING,
  x_coordinate STRING,
  y_coordinate STRING,
  year INT,
  updated_on STRING,
  latitude DOUBLE,
  longitude DOUBLE,
  location STRING
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
)
LOCATION 's3://chicago-crime-stream-data/2025/';
