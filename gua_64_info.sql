/*
 Navicat Premium Data Transfer

 Source Server         : iching
 Source Server Type    : SQLite
 Source Server Version : 3008008
 Source Database       : main

 Target Server Type    : SQLite
 Target Server Version : 3008008
 File Encoding         : utf-8

 Date: 02/12/2017 21:07:56 PM
*/

PRAGMA foreign_keys = false;

-- ----------------------------
--  Table structure for gua_64_info
-- ----------------------------
DROP TABLE IF EXISTS "gua_64_info";
CREATE TABLE "gua_64_info" (
	 "gua_name" text(2,0) NOT NULL,
	 "gua_info_index" text(8,0) NOT NULL,
	 "gua_info" text(200,0) NOT NULL,

	PRIMARY KEY("gua_name","gua_info_index","gua_info")
);

-- ----------------------------
--  Records of gua_64_info
-- ----------------------------
BEGIN;
INSERT INTO "gua_64_info" VALUES ('乾', '初九', '初九：潜龙，勿用。');
COMMIT;

PRAGMA foreign_keys = true;
