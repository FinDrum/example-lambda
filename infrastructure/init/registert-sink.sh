#!/bin/bash

echo "Registrando conector S3 Sink en Kafka Connect..."

curl -X POST http://localhost:8083/connectors \
    -H "Content-Type: application/json" \
    -d '{
    "name": "minio-sink-connector",
    "config": {
      "connector.class": "io.confluent.connect.s3.S3SinkConnector",
      "tasks.max": "1",
      "topics": "stock_prices",
      "s3.bucket.name": "stock-data",
      "s3.region": "us-east-1",
      "s3.part.size": 5242880,
      "flush.size": 100,
      "storage.class": "io.confluent.connect.s3.storage.S3Storage",
      "format.class": "io.confluent.connect.s3.format.json.JsonFormat",
      "partitioner.class": "io.confluent.connect.storage.partitioner.TimeBasedPartitioner",
      "path.format": "yyyy/MM/dd",
      "locale": "en",
      "timezone": "UTC",
      "topics.dir": "stock_prices",
      "s3.endpoint": "http://minio:9000",
      "s3.credentials.provider.class": "io.confluent.connect.s3.auth.AwsAccessKeyIdSecretAccessKeyCredentialsProvider",
      "aws.access.key.id": "minioadmin",
      "aws.secret.access.key": "minioadmin"
    }
  }'

echo "Conector S3 registrado."
