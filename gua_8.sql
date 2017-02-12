/*
 Navicat Premium Data Transfer

 Source Server         : iching
 Source Server Type    : SQLite
 Source Server Version : 3008008
 Source Database       : main

 Target Server Type    : SQLite
 Target Server Version : 3008008
 File Encoding         : utf-8

 Date: 02/12/2017 20:00:57 PM
*/

PRAGMA foreign_keys = false;

-- ----------------------------
--  Table structure for gua_8
-- ----------------------------
DROP TABLE IF EXISTS "gua_8";
CREATE TABLE "gua_8" (
	 "gua_bi_str" text(3,0) NOT NULL,
	 "gua_name" text(2,0) NOT NULL,
	 "gua_ sign" text(2,0) NOT NULL,
	 "gua_other_name" text(2,0) NOT NULL,
	 "gua_index" text(1,0) NOT NULL,
	PRIMARY KEY("gua_bi_str")
);

-- ----------------------------
--  Records of gua_8
-- ----------------------------
BEGIN;
INSERT INTO "gua_8" VALUES (111, '乾', '☰', '天', 1);
COMMIT;

PRAGMA foreign_keys = true;
