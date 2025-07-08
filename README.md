# Lambda Architecture – Real-Time & Batch Stock Analytics with FinDrum

This project showcases a Lambda Architecture using **FinDrum** for ingesting, processing, storing, and visualizing financial data. It combines real-time analytics via Kafka and PostgreSQL with batch processing through scheduled FinDrum pipelines, offering a complete and modular environment for technical stock analysis.

## Architecture Overview

![Architecture](./imgs/architecture.png)

---

## Real-Time Processing (Speed Layer)

- **Kafka** ingests stock prices via the `stock_prices` topic.
- A Kafka-based trigger in FinDrum listens for new messages.
- Upon message arrival the results are saved in a PostgreSQL table (`realtime_stock`).
- **Grafana** queries PostgreSQL for real-time metrics like volume, open/close prices, etc.

---

## 📦 Batch Processing (Batch Layer)

- **Kafka Connect** pushes all incoming events to **MinIO**, preserving them for later analysis.
- A scheduled FinDrum pipeline runs hourly starting:
  - Reads historical data from MinIO.
  - Aggregates prices (average, volume, etc.).
  - Saves the summary into a PostgreSQL table (`hourly_stock_summary`).

This batch layer is ideal for daily reports or technical indicators like moving averages.

---

## Visualization (Serving Layer)

- **Grafana** connects to PostgreSQL to visualize both real-time and aggregated metrics.
- Dashboards include:
  - Minute-by-minute close prices.
  - Volume trends by stock symbol.
  - Historical summaries per hour.

---

## Services

| Service       | Port(s)    | Purpose                     |
| ------------- | ---------- | --------------------------- |
| Zookeeper     | 2181       | Kafka coordination          |
| Kafka         | 9092       | Event streaming             |
| MinIO         | 9000, 9001 | S3-compatible storage       |
| Kafka Connect | 8083       | Sink connector to MinIO     |
| PostgreSQL    | 5432       | Structured data persistence |
| Grafana       | 3000       | Real-time dashboard         |

---

## How It Works

1. **Stock events** are sent to Kafka (`stock_prices` topic).
2. Kafka Connect stores events in MinIO.
3. A real-time processing pipeline:
   - Consumes messages.
   - Saves results in PostgreSQL.
4. Grafana connects to PostgreSQL and visualizes the live data.

---

## How to Run

### 1. Clone the repo and start services

```bash
git https://github.com/FinDrum/Lambda-Architecture.git
cd Lambda-Architecture/infrastructure
docker-compose up --build
```

### 2. Run FinDrum Pipelines

Activate your Python environment.

Install requirements.txt

```bash
pip install -r requirements.txt
```

And run the pipelines

```python
from findrum import Platform

platform = Platform("./config.yaml")
platform.register_pipeline("./pipelines/realtime_pipeline.yaml")
platform.register_pipeline("./pipelines/batch_pipeline.yaml")
platform.start()
```

### 3. Access interfaces

- MinIO Console: http://localhost:9001 (user: `minioadmin`, pass: `minioadmin`)
- Grafana: http://localhost:3000 (user: `admin`, pass: `admin`)

### 4. Dashboard Overview

![Architecture](./imgs/dashboard.png)

## Requirements

- Docker & Docker Compose
- Python 3.12+ (if running the pipeline manually)

## Future Improvements

- Automate batch jobs using Spark over MinIO data.

- Integrate Prometheus for extended monitoring.

- Add anomaly detection pipelines using ML.

---

© 2025 – FinDrum
