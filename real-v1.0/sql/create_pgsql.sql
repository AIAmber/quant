CREATE TABLE "public"."t_quant_model" (
	"time_stamp" varchar(32) COLLATE "default",
	"stock_name" varchar(32) COLLATE "default",
	"price" float4,
	"open_tod" float4,
	"close_lst" float4,
	"high" float4,
	"low" float4,
	"sel_5" float4,
	"sel_5_num" int4,
	"sel_4" float4,
	"sel_4_num" int4,
	"sel_3" float4,
	"sel_3_num" int4,
	"sel_2" float4,
	"sel_2_num" int4,
	"sel_1" float4,
	"sel_1_num" int4,
	"buy_1" float4,
	"buy_1_num" int4,
	"buy_2" float4,
	"buy_2_num" int4,
	"buy_3" float4,
	"buy_3_num" int4,
	"buy_4" float4,
	"buy_4_num" int4,
	"buy_5" float4,
	"buy_5_num" int4,
	"volume" int8,
	"turn_volume" float8
)
WITH (OIDS=FALSE)
;

ALTER TABLE "public"."t_quant_model" OWNER TO "postgres";