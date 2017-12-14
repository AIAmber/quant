-- Table: leolee.t_stock_sz000672

-- DROP TABLE leolee.t_stock_sz000672;

CREATE TABLE leolee.t_stock_sz000672
(
    stock_name character varying COLLATE pg_catalog."default" NOT NULL,
    price double precision,
    "Open" double precision,
    "CloseLST" double precision,
    "High" double precision,
    "Low" double precision,
    "Sel_5" double precision,
    "Sel_5_num" bigint,
    "Sel_4" double precision,
    "Sel_4_num" bigint,
    "Sel_3" double precision,
    "Sel_3_num" bigint,
    "Sel_2" double precision,
    "Sel_2_num" bigint,
    "Sel_1" double precision,
    "Sel_1_num" bigint,
    "Buy_1" double precision,
    "Buy_1_num" bigint,
    "Buy_2" double precision,
    "Buy_2_num" bigint,
    "Buy_3" double precision,
    "Buy_3_num" bigint,
    "Buy_4" double precision,
    "Buy_4_num" bigint,
    "Buy_5" double precision,
    "Buy_5_num" bigint
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE leolee.t_stock_sz000672
    OWNER to leolee;
COMMENT ON TABLE leolee.t_stock_sz000672
    IS 't_stock_sz000672';

COMMENT ON COLUMN leolee.t_stock_sz000672.stock_name
    IS 'stock_name';