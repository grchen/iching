/*
 Navicat Premium Data Transfer

 Source Server         : iching
 Source Server Type    : SQLite
 Source Server Version : 3008008
 Source Database       : main

 Target Server Type    : SQLite
 Target Server Version : 3008008
 File Encoding         : utf-8

 Date: 02/12/2017 20:48:37 PM
*/

PRAGMA foreign_keys = false;

-- ----------------------------
--  Table structure for gua_yilin
-- ----------------------------
DROP TABLE IF EXISTS "gua_yilin";
CREATE TABLE "gua_yilin" (
	 "gua_name" text(2,0) NOT NULL,
	 "gua_info_index" text(8,0) NOT NULL,
	 "gua_info" text(200,0) NOT NULL,

	PRIMARY KEY("gua_name","gua_info_index","gua_info")
);

-- ----------------------------
--  Records of gua_yilin
-- ----------------------------
BEGIN;
INSERT INTO "gua_yilin" VALUES ('乾', '乾', '道陟石阪，胡言連蹇，譯瘖且聾，茵使道通請謁不行求事無功。');
COMMIT;

PRAGMA foreign_keys = true;
