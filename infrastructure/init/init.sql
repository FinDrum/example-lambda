CREATE TABLE IF NOT EXISTS realtime_stock (
  symbol TEXT,
  timestamp TEXT,
  open DOUBLE PRECISION,
  close DOUBLE PRECISION,
  volume BIGINT
);

CREATE TABLE IF NOT EXISTS hourly_stock_summary (
    symbol TEXT,
    hour TIMESTAMP,
    avg_close DOUBLE PRECISION
);
