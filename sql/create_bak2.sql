-- Table: public.t_stock_sz000672_bak2new

DROP TABLE public.t_stock_sz000672_bak2new;

CREATE TABLE public.t_stock_sz000672_bak2new
(
    stock_name character varying COLLATE pg_catalog."default" NOT NULL,
    price double precision COLLATE pg_catalog."default",
    open_tod double precision COLLATE pg_catalog."default",
    close_lst double precision COLLATE pg_catalog."default",
    high double precision COLLATE pg_catalog."default",
    low double precision COLLATE pg_catalog."default",
    sel_5 double precision COLLATE pg_catalog."default",
    sel_5_num bigint COLLATE pg_catalog."default",
    sel_4 double precision COLLATE pg_catalog."default",
    sel_4_num bigint COLLATE pg_catalog."default",
    sel_3 double precision COLLATE pg_catalog."default",
    sel_3_num bigint COLLATE pg_catalog."default",
    sel_2 double precision COLLATE pg_catalog."default",
    sel_2_num bigint COLLATE pg_catalog."default",
    sel_1 double precision COLLATE pg_catalog."default",
    sel_1_num bigint COLLATE pg_catalog."default",
    buy_1 double precision COLLATE pg_catalog."default",
    buy_1_num bigint COLLATE pg_catalog."default",
    buy_2 double precision COLLATE pg_catalog."default",
    buy_2_num bigint COLLATE pg_catalog."default",
    buy_3 double precision COLLATE pg_catalog."default",
    buy_3_num bigint COLLATE pg_catalog."default",
    buy_4 double precision COLLATE pg_catalog."default",
    buy_4_num bigint COLLATE pg_catalog."default",
    buy_5 double precision COLLATE pg_catalog."default",
    buy_5_num bigint COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.t_stock_sz000672_bak2new
    OWNER to postgres;
COMMENT ON TABLE public.t_stock_sz000672_bak2new
    IS 'for test';