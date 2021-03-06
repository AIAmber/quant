CREATE TABLE `t_stock_sz000672_171231` (
  `time_stamp` varchar(32) NOT NULL,
  `stock_name` varchar(16) DEFAULT NULL,
  `price` float(10,2) DEFAULT NULL,
  `open_tod` float(10,2) DEFAULT NULL,
  `close_lst` float(10,2) DEFAULT NULL,
  `high` float(10,2) DEFAULT NULL,
  `low` float(10,2) DEFAULT NULL,
  `sel_5` float(10,2) DEFAULT NULL,
  `sel_5_num` int(11) DEFAULT NULL,
  `sel_4` float(10,2) DEFAULT NULL,
  `sel_4_num` int(11) DEFAULT NULL,
  `sel_3` float(10,2) DEFAULT NULL,
  `sel_3_num` int(11) DEFAULT NULL,
  `sel_2` float(10,2) DEFAULT NULL,
  `sel_2_num` int(11) DEFAULT NULL,
  `sel_1` float(10,2) DEFAULT NULL,
  `sel_1_num` int(11) DEFAULT NULL,
  `buy_1` float(10,2) DEFAULT NULL,
  `buy_1_num` int(11) DEFAULT NULL,
  `buy_2` float(10,2) DEFAULT NULL,
  `buy_2_num` int(11) DEFAULT NULL,
  `buy_3` float(10,2) DEFAULT NULL,
  `buy_3_num` int(11) DEFAULT NULL,
  `buy_4` float(10,2) DEFAULT NULL,
  `buy_4_num` int(11) DEFAULT NULL,
  `buy_5` float(10,2) DEFAULT NULL,
  `buy_5_num` int(11) DEFAULT NULL,
  `volume` bigint(16) DEFAULT NULL,
  `turn_volume` double(20,2) DEFAULT NULL
);