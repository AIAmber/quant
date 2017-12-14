-- Table: leolee.t_stock_sz000672_bak

-- DROP TABLE leolee.t_stock_sz000672_bak;

CREATE TABLE leolee.t_stock_sz000672_bak
(
    stock_name character varying COLLATE pg_catalog."default" NOT NULL,
    price character varying COLLATE pg_catalog."default",
    open character varying COLLATE pg_catalog."default",
    close_lst character varying COLLATE pg_catalog."default",
    high character varying COLLATE pg_catalog."default",
    low character varying COLLATE pg_catalog."default",
    sel_5 character varying COLLATE pg_catalog."default",
    sel_5_num character varying COLLATE pg_catalog."default",
    sel_4 character varying COLLATE pg_catalog."default",
    sel_4_num character varying COLLATE pg_catalog."default",
    sel_3 character varying COLLATE pg_catalog."default",
    sel_3_num character varying COLLATE pg_catalog."default",
    sel_2 character varying COLLATE pg_catalog."default",
    sel_2_num character varying COLLATE pg_catalog."default",
    sel_1 character varying COLLATE pg_catalog."default",
    sel_1_num character varying COLLATE pg_catalog."default",
    buy_1 character varying COLLATE pg_catalog."default",
    buy_1_num character varying COLLATE pg_catalog."default",
    buy_2 character varying COLLATE pg_catalog."default",
    buy_2_num character varying COLLATE pg_catalog."default",
    buy_3 character varying COLLATE pg_catalog."default",
    buy_3_num character varying COLLATE pg_catalog."default",
    buy_4 character varying COLLATE pg_catalog."default",
    buy_4_num character varying COLLATE pg_catalog."default",
    buy_5 character varying COLLATE pg_catalog."default",
    buy_5_num character varying COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE leolee.t_stock_sz000672_bak
    OWNER to leolee;
COMMENT ON TABLE leolee.t_stock_sz000672_bak
    IS 't_stock_sz000672';

COMMENT ON COLUMN leolee.t_stock_sz000672_bak.stock_name
    IS 'stock_name';