/*
 Navicat Premium Data Transfer

 Source Server         : iching
 Source Server Type    : SQLite
 Source Server Version : 3008008
 Source Database       : main

 Target Server Type    : SQLite
 Target Server Version : 3008008
 File Encoding         : utf-8

 Date: 02/12/2017 20:36:36 PM
*/

PRAGMA foreign_keys = false;

-- ----------------------------
--  Table structure for gua_64
-- ----------------------------
DROP TABLE IF EXISTS "gua_64";
CREATE TABLE "gua_64" (
	 "gua_bi_str" text(6,0) NOT NULL,
	 "gua_name" text(2,0) NOT NULL,
	 "gua_sign" text(2,0) NOT NULL,
	 "gua_other_name" text(6,0) NOT NULL,
	 "gua_index" text(2,0) NOT NULL,
	PRIMARY KEY("gua_bi_str")
);

-- ----------------------------
--  Records of gua_64
-- ----------------------------
BEGIN;
INSERT INTO "gua_64" VALUES (111111, '乾', '䷀', '乾为天', 1);
COMMIT;

PRAGMA foreign_keys = true;
