CREATE TABLE "trades" (
  "timestamp" timestamp NOT NULL,
  "symbol" character(6) NOT NULL,
  "side" character(4) NOT NULL,
  "size" double precision NOT NULL,
  "price" real NOT NULL
);