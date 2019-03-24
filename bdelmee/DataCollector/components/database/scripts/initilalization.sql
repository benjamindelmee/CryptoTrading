CREATE TABLE "trades" (
  "timestamp" timestamp NOT NULL,
  "symbol" character(6) NOT NULL,
  "side" character(4) NOT NULL,
  "size" double precision NOT NULL,
  "price" real NOT NULL
);

/**
 * View to obtain candlesticks at the minute level.
**/
CREATE VIEW candlesticks_minute AS
SELECT
	  B.symbol                            AS symbol
	, DATE_TRUNC('minute', B.timestamp)   AS timestamp
	, B.side                              AS side
	, B.open                              AS open
	, B.close                             AS close
	, MAX(B.price)                        AS high
	, MIN(B.price)                        AS low
	, SUM(B.size)                         AS volume
	, COUNT(B.*)                          AS nbTrades
FROM (
	SELECT
		  A.*
		, FIRST_VALUE(A.price) OVER (PARTITION BY A.symbol, DATE_TRUNC('minute', A.timestamp), A.side ORDER BY A.id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS open
		, LAST_VALUE(A.price)  OVER (PARTITION BY A.symbol, DATE_TRUNC('minute', A.timestamp), A.side ORDER BY A.id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS close
	FROM (SELECT trades.*, ROW_NUMBER() OVER (ORDER BY timestamp) AS id FROM trades) AS A
) AS B
GROUP BY
	  B.symbol
	, DATE_TRUNC('minute', B.timestamp)
	, B.side
	, B.open
	, B.close
ORDER BY
    B.symbol
  , DATE_TRUNC('minute', B.timestamp) 
  , B.side
;

/**
 * View to obtain candlesticks at the hour level.
**/
CREATE VIEW candlesticks_hour AS
SELECT
	  B.symbol                            AS symbol
	, DATE_TRUNC('hour', B.timestamp)     AS timestamp
	, B.side                              AS side
	, B.open                              AS open
	, B.close                             AS close
	, MAX(B.price)                        AS high
	, MIN(B.price)                        AS low
	, SUM(B.size)                         AS volume
	, COUNT(B.*)                          AS nbTrades
FROM (
	SELECT
		  A.*
		, FIRST_VALUE(A.price) OVER (PARTITION BY A.symbol, DATE_TRUNC('hour', A.timestamp), A.side ORDER BY A.id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS open
		, LAST_VALUE(A.price)  OVER (PARTITION BY A.symbol, DATE_TRUNC('hour', A.timestamp), A.side ORDER BY A.id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS close
	FROM (SELECT trades.*, ROW_NUMBER() OVER (ORDER BY timestamp) AS id FROM trades) AS A
) AS B
GROUP BY
	  B.symbol
	, DATE_TRUNC('hour', B.timestamp)
	, B.side
	, B.open
	, B.close
ORDER BY
    B.symbol
  , DATE_TRUNC('hour', B.timestamp) 
  , B.side
;

/**
 * View to obtain candlesticks at the day level.
**/
CREATE VIEW candlesticks_day AS
SELECT
	  B.symbol                            AS symbol
	, DATE_TRUNC('day', B.timestamp)      AS timestamp
	, B.side                              AS side
	, B.open                              AS open
	, B.close                             AS close
	, MAX(B.price)                        AS high
	, MIN(B.price)                        AS low
	, SUM(B.size)                         AS volume
	, COUNT(B.*)                          AS nbTrades
FROM (
	SELECT
		  A.*
		, FIRST_VALUE(A.price) OVER (PARTITION BY A.symbol, DATE_TRUNC('day', A.timestamp), A.side ORDER BY A.id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS open
		, LAST_VALUE(A.price)  OVER (PARTITION BY A.symbol, DATE_TRUNC('day', A.timestamp), A.side ORDER BY A.id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS close
	FROM (SELECT trades.*, ROW_NUMBER() OVER (ORDER BY timestamp) AS id FROM trades) AS A
) AS B
GROUP BY
	  B.symbol
	, DATE_TRUNC('day', B.timestamp)
	, B.side
	, B.open
	, B.close
ORDER BY
    B.symbol
  , DATE_TRUNC('day', B.timestamp) 
  , B.side
;