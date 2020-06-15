/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 100406
 Source Host           : localhost:3306
 Source Schema         : food_blog

 Target Server Type    : MySQL
 Target Server Version : 100406
 File Encoding         : 65001

 Date: 09/06/2020 09:12:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES (1, 'pbkdf2_sha256$180000$BYO7fGvE5uXM$p5wlTLPTaTQSZpJrwxMR0fD8ugnibEGCfFdCMukEQzo=', '2020-05-15 06:09:39.922125', 1, 'Joshua', '', '', 'liyinankai1@163.com', 1, 1, '2020-05-15 06:08:01.118464');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for blog
-- ----------------------------
DROP TABLE IF EXISTS `blog`;
CREATE TABLE `blog`  (
  `blog_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `blog_category_id` smallint(6) NULL DEFAULT NULL,
  `blog_title` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `blog_excerpt` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `blog_content` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `blog_modified` datetime(0) NOT NULL,
  `browse_volume` int(11) NULL DEFAULT NULL,
  `praise_point` smallint(6) NULL DEFAULT NULL,
  PRIMARY KEY (`blog_id`) USING BTREE,
  INDEX `FK_setting`(`blog_category_id`) USING BTREE,
  CONSTRAINT `FK_setting` FOREIGN KEY (`blog_category_id`) REFERENCES `blog_category` (`blog_category_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 84 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of blog
-- ----------------------------
INSERT INTO `blog` VALUES (46, NULL, '1111', '111111111111113333333333', '222223333333', '2020-06-08 14:16:00', NULL, NULL);
INSERT INTO `blog` VALUES (58, NULL, '2222222333333333', '2222222222', '222222222222222222222', '2020-06-07 08:44:00', NULL, NULL);
INSERT INTO `blog` VALUES (61, NULL, '333333333333', '33333333333333', '33333333333333333333333', '2020-06-07 18:42:00', NULL, NULL);
INSERT INTO `blog` VALUES (65, NULL, '还在嫌弃作业不够秀？快来试试streamlit+heroku', '大家好，我是练习时长一天的偶像练习生“陈独秀”!\r\n你们是否还在为平时作业不够秀，不够高大上，无法引起老师注意而苦恼？\r\n你们是否还在为向甲方爸爸汇报成果的时候，没有一个华丽的展示方法，秀的他两眼发光，连连叫好而头秃？\r\n千万不要错过，本篇文章教你使用strealit+heroku 搭建自己的炫酷app！！！', '\r\n大家好，我是练习时长一天的偶像练习生“陈独秀”!\r\n\r\n童鞋们，你们是否还在为平时作业不够秀，不够高大上，无法引起老师注意而苦恼？\r\n\r\n同志们，你们是否还在为向甲方爸爸汇报成果的时候，没有一个华丽的展示方法，秀的他两眼发光，连连叫好而头秃？\r\n\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421150439474.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDk4NDY2NA==,size_16,color_FFFFFF,t_70)\r\n\r\n请大家搬好小板凳且看在下秀一波操作。\r\n带你们入职偶像练习生！！！\r\n\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421150600994.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDk4NDY2NA==,size_16,color_FFFFFF,t_70)\r\n\r\n<br>\r\n\r\n### 一、基本介绍\r\n#### （一）streamlit\r\n先简单介绍一下\r\n\r\n`streamlit`\r\n\r\n一个python的包，无需任何的HTML，CSS，JS，VUE……\r\n\r\n基础就可以做出一个好看又实用的web网页\r\n\r\n最最最重要的是他可以和机器学习，数据分析等嵌套\r\n\r\n这样就使得`streamlit`成为一个非常好的可视化成果展示的工具\r\n\r\n<br>\r\n\r\n先看看`streamlit`的效果\r\n\r\n一个官网上的模板\r\n\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/2020042114563823.gif)\r\n\r\n<br>\r\n\r\n这时候如果再和一些云服务器平台双剑合璧\r\n想一想，给老师或者甲方交过去作业或者方案的时候\r\n直接配上一个网址，他们点进去之后……\r\n简直不要太香\r\n\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421160637946.gif)\r\n\r\n<br>\r\n\r\n咱在这里先列出一些必看的网站\r\n\r\n+ 一篇介绍性的文章[https://baijiahao.baidu.com/s?id=1648882060644341406&wfr=spider&for=pc](https://baijiahao.baidu.com/s?id=1648882060644341406&wfr=spider&for=pc)\r\n\r\n+ `streamlit`的官网：[https://www.streamlit.io](https://www.streamlit.io/)\r\n\r\n+ 中文API开发手册[http://cw.hubwiz.com/card/c/streamlit-manual/](http://cw.hubwiz.com/card/c/streamlit-manual/)\r\n+ 社区[https://discuss.streamlit.io](https://discuss.streamlit.io/)\r\n\r\n<br>\r\n\r\n由于这是个比较新兴的项目，有许多的地方还不是特别的优秀，遇到问题的时候可以到社区里查查，说不定一些大佬会给出解决方法哦\r\n\r\n`streamlit`可以和很多的云平台配套\r\n\r\n比如说：EC2，Glitch，Heroku\r\n\r\n<br>\r\n\r\n我这里仅给出Heroku的搭建方法\r\n\r\n那么为啥选择这个平台嘞?\r\n\r\n当然是，Heroku对于像我这样的穷苦学生党和免费用户来说还是比较友好的，每个月有550h的免费挂载时长\r\n\r\n算下来大概是23天，应该够用了\r\n\r\n下面仅以我的一个作业作为演示\r\n\r\n<br>\r\n\r\n#### （二）app效果\r\n使用`Block-Stripe Update algorithm `实现`pagerank`算法\r\n代码会在最后部分给出\r\napp地址\r\n[https://streamlit-pagerank.herokuapp.com](https://streamlit-pagerank.herokuapp.com)\r\n\r\n>注：该app我只是为了交作业????\r\n>将于2020年5月20日左右到期\r\n\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/20200421160745709.gif)', '2020-06-08 11:40:00', NULL, NULL);
INSERT INTO `blog` VALUES (69, NULL, '888888888888', '888888888888888888', '88888888888888888888888888888888888888', '2020-06-08 14:00:00', NULL, NULL);
INSERT INTO `blog` VALUES (70, NULL, '999999999999999999', '999999999999999', '999999999999999999999999999999999999', '2020-06-08 14:00:00', NULL, NULL);
INSERT INTO `blog` VALUES (71, NULL, '1111', '111111111111112222222222222222', '222223333333', '2020-06-08 14:16:00', NULL, NULL);
INSERT INTO `blog` VALUES (73, NULL, 'aaaaaaaaaaa', 'aaaaaaaaaaaadddddddddddd', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaa', '2020-06-08 14:18:00', NULL, NULL);
INSERT INTO `blog` VALUES (74, NULL, 'fffffffffff', 'ffffffffffffffff', 'fffffffffffffffffffffffffff', '2020-06-08 17:33:00', NULL, NULL);
INSERT INTO `blog` VALUES (75, NULL, 'SQL相关操作笔记（附习题）', 'SQL相关操作笔记（附习题）', '<br>\r\n\r\nSQL相关操作\r\n\r\n+ 插入\r\n+ 删除\r\n+ 更新\r\n+ 触发器\r\n+ 视图\r\n+ 索引\r\n+ 权限\r\n+ 授权图\r\n\r\n<br>\r\n\r\n\r\n\r\n### 插入\r\n\r\n\r\n\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/2020040309381119.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDk4NDY2NA==,size_16,color_FFFFFF,t_70)\r\n\r\n`ABC`\r\n\r\n<br>\r\n\r\n### 删除\r\n\r\n\r\n\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/20200403093717215.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDk4NDY2NA==,size_16,color_FFFFFF,t_70)\r\n', '2020-06-08 17:38:00', NULL, NULL);
INSERT INTO `blog` VALUES (76, NULL, '适合小白的前端框架大总结', '适合小白的前端框架大总结111111', '<br>\r\n推荐一个超级厉害的前端网站\r\n\r\n[http://www.fly63.com/nav](http://www.fly63.com/nav)\r\n适合像我一样的小白入门\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/20200325160521861.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDk4NDY2NA==,size_16,color_FFFFFF,t_70)\r\n他已经按模块将很多的前端相关的网站都总结了\r\n内容非常丰富 d=====(￣▽￣*)b\r\n下面是小编搜集的一些相关的框架和项目\r\n<br>\r\n\r\n### 15种CSS框架\r\n\r\n\r\n\r\n**1. Bootstrap**\r\n\r\n[https://getbootstrap.com](https://getbootstrap.com/)\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/2020032516123942.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDk4NDY2NA==,size_16,color_FFFFFF,t_70)\r\n最初被称为Twitter Blueprint的Bootstrap，是作为内部团队使用的工具而创建的。它是最著名的前端框架之一。自公开发布以来，Bootstrap的使用率逐年攀升。\r\n\r\nBootstrap提供了报警、按钮、轮播、下拉式菜单、以及表单等设计模板。借助Bootstrap的移动优先(mobile-first)功能，您可以轻松地创建响应式布局，进而保证在横跨多个设备上的设计一致性。\r\n\r\n**2. Skeleton**\r\n\r\n[http://getskeleton.com/](http://getskeleton.com/)\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/20200325161514292.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDk4NDY2NA==,size_16,color_FFFFFF,t_70)\r\nSkeleton号称“简单的响应式样板”。由于此框架只有大约400行代码，因此它更适合于小型项目，以及开发人员需要创建轻量级内容的应用场景。\r\n\r\n由于布局简单，Skeleton对于那些刚开始使用前端框架的人来说，是一个不错的选择。当然，也正是缺少CSS设计模板、预处理器、以及整体功能，受限的Skeleton不太适合大型的项目。\r\n\r\n**3. ZURB Foundation**\r\n[https://get.foundation](https://get.foundation)\r\n![在这里插入图片描述](https://img-blog.csdnimg.cn/20200325161430903.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NDk4NDY2NA==,size_16,color_FFFFFF,t_70)', '2020-06-08 17:48:00', NULL, NULL);
INSERT INTO `blog` VALUES (77, NULL, 'hhhhhhhhh', 'hhhhhhhhhhhh', 'hhhhhhhhhhhhhhhhhhhhh', '2020-06-08 22:05:00', NULL, NULL);
INSERT INTO `blog` VALUES (78, NULL, 'kkkkkkkkkkkhhhhhhhhhhhhhh', 'kkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkkkkkkkk', '2020-06-08 22:07:00', NULL, NULL);

-- ----------------------------
-- Table structure for blog_category
-- ----------------------------
DROP TABLE IF EXISTS `blog_category`;
CREATE TABLE `blog_category`  (
  `blog_category_id` smallint(6) NOT NULL,
  `blog_category_name` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `blog_category_description` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`blog_category_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 18 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2020-05-15 06:06:41.993414');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2020-05-15 06:06:44.375979');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2020-05-15 06:06:55.849545');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2020-05-15 06:06:58.820467');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2020-05-15 06:06:58.874830');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2020-05-15 06:07:00.375678');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2020-05-15 06:07:01.479642');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2020-05-15 06:07:02.787905');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2020-05-15 06:07:02.839890');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2020-05-15 06:07:04.175847');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2020-05-15 06:07:04.230878');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2020-05-15 06:07:04.310842');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2020-05-15 06:07:04.617460');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2020-05-15 06:07:04.862191');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2020-05-15 06:07:06.030190');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2020-05-15 06:07:06.083921');
INSERT INTO `django_migrations` VALUES (17, 'sessions', '0001_initial', '2020-05-15 06:07:06.433288');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('1nzogopvqz3tkxosvv4l0d21rrsfymvz', 'OTQxMzc0ODNiZWJhMWVkYTRiNTU0MGVkMzQ5YTQwYTY2MjAzMDE4ZDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIyZDU1MGIxNmU5NmYzZDNiOTNmZWRjNDJjODcwOWE4NjNmOWMwMDFkIiwibW9kaWZ5IjowLCJpc19sb2dpbiI6IjEiLCJlbWFpbCI6ImxpeWluYW5rYWkxQDE2My5jb20ifQ==', '2020-06-23 01:09:09.796257');

-- ----------------------------
-- Table structure for garbage
-- ----------------------------
DROP TABLE IF EXISTS `garbage`;
CREATE TABLE `garbage`  (
  `garbage_id` int(11) NOT NULL AUTO_INCREMENT,
  `garbage_catgory_id` smallint(6) NOT NULL,
  `garbage_img` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `garbage_description` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `garbage_name` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`garbage_id`) USING BTREE,
  INDEX `FK_belong`(`garbage_catgory_id`) USING BTREE,
  CONSTRAINT `FK_belong` FOREIGN KEY (`garbage_catgory_id`) REFERENCES `garbage_catgory` (`garbage_catgory_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of garbage
-- ----------------------------
INSERT INTO `garbage` VALUES (1, 1, 'http://www.aiimg.com/uploads/userup/0906/1412400122b.jpg', NULL, '报纸');
INSERT INTO `garbage` VALUES (2, 1, 'https://ns-strategy.cdn.bcebos.com/ns-strategy/upload/fc_big_pic/part-00395-212.jpg', NULL, '包装纸');
INSERT INTO `garbage` VALUES (3, 2, 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1002511127,2563297224&fm=26&gp=0.jpg', NULL, '卫生纸');
INSERT INTO `garbage` VALUES (4, 2, 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3679926600,3553344919&fm=26&gp=0.jpg', NULL, '尘土');
INSERT INTO `garbage` VALUES (5, 3, 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2895731510,1699682303&fm=26&gp=0.jpg', NULL, '剩菜剩饭');
INSERT INTO `garbage` VALUES (6, 3, 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3757077887,4228294053&fm=26&gp=0.jpg', NULL, '果皮');
INSERT INTO `garbage` VALUES (7, 4, 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3829981557,259880582&fm=26&gp=0.jpg', NULL, '电池');
INSERT INTO `garbage` VALUES (8, 4, 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2452153345,1762479784&fm=26&gp=0.jpg', NULL, '灯泡');

-- ----------------------------
-- Table structure for garbage_catgory
-- ----------------------------
DROP TABLE IF EXISTS `garbage_catgory`;
CREATE TABLE `garbage_catgory`  (
  `garbage_catgory_id` smallint(6) NOT NULL AUTO_INCREMENT,
  `garbage_catgory_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `garbage_category_description` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`garbage_catgory_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of garbage_catgory
-- ----------------------------
INSERT INTO `garbage_catgory` VALUES (1, '可回收物', '这些垃圾通过综合处理回收利用，可以减少污染，节省资源');
INSERT INTO `garbage_catgory` VALUES (2, '其它垃圾', '其他垃圾（上海称干垃圾）包括除上述几类垃圾之外的砖瓦陶瓷、渣土、卫生间废纸、纸巾等难以回收的废弃物及尘土、食品袋（盒）。采取卫生填埋可有效减少对地下水、地表水、土壤及空气的污染。');
INSERT INTO `garbage_catgory` VALUES (3, '厨余垃圾', '厨余垃圾（上海称湿垃圾）包括剩菜剩饭、骨头、菜根菜叶、果皮等食品类废物。经生物技术就地处理堆肥，每吨可生产0.6~0.7吨有机肥料。');
INSERT INTO `garbage_catgory` VALUES (4, '有害垃圾', '有害垃圾含有对人体健康有害的重金属、有毒的物质或者对环境造成现实危害或者潜在危害的废弃物。包括电池、荧光灯管、灯泡、水银温度计、油漆桶、部分家电、过期药品及其容器、过期化妆品等。这些垃圾一般使用单独回收或填埋处理。');

-- ----------------------------
-- Table structure for login
-- ----------------------------
DROP TABLE IF EXISTS `login`;
CREATE TABLE `login`  (
  `ID` bigint(20) NULL DEFAULT NULL,
  `login_time` datetime(0) NOT NULL,
  `ip` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `errorcount` tinyint(1) NULL DEFAULT NULL,
  INDEX `fk_user_login`(`ID`) USING BTREE,
  CONSTRAINT `fk_user_login` FOREIGN KEY (`ID`) REFERENCES `user` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of login
-- ----------------------------
INSERT INTO `login` VALUES (9, '2020-06-08 17:27:00', '192.168.56.1', 2);
INSERT INTO `login` VALUES (9, '2020-06-08 17:27:00', '192.168.56.1', 2);
INSERT INTO `login` VALUES (9, '2020-06-08 17:47:00', '192.168.56.1', 0);
INSERT INTO `login` VALUES (9, '2020-06-08 17:47:00', '192.168.56.1', 0);
INSERT INTO `login` VALUES (9, '2020-06-08 17:54:00', '192.168.56.1', 0);
INSERT INTO `login` VALUES (9, '2020-06-08 18:55:00', '192.168.56.1', 0);
INSERT INTO `login` VALUES (9, '2020-06-08 20:10:00', '192.168.56.1', 0);
INSERT INTO `login` VALUES (9, '2020-06-08 21:41:00', '192.168.56.1', 0);
INSERT INTO `login` VALUES (9, '2020-06-08 22:25:00', '192.168.56.1', 0);
INSERT INTO `login` VALUES (9, '2020-06-08 22:34:00', '192.168.56.1', 0);
INSERT INTO `login` VALUES (8, '2020-06-09 08:52:00', '192.168.56.1', 2);
INSERT INTO `login` VALUES (9, '2020-06-09 09:09:00', '192.168.56.1', 0);

-- ----------------------------
-- Table structure for publish_blog
-- ----------------------------
DROP TABLE IF EXISTS `publish_blog`;
CREATE TABLE `publish_blog`  (
  `blog_id` bigint(20) NOT NULL,
  `ID` bigint(20) NOT NULL,
  `publish_time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`blog_id`, `ID`) USING BTREE,
  INDEX `FK_publish_blog2`(`ID`) USING BTREE,
  CONSTRAINT `FK_publish_blog` FOREIGN KEY (`blog_id`) REFERENCES `blog` (`blog_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_publish_blog2` FOREIGN KEY (`ID`) REFERENCES `user` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of publish_blog
-- ----------------------------
INSERT INTO `publish_blog` VALUES (46, 8, '2020-06-08 14:16:00');
INSERT INTO `publish_blog` VALUES (58, 9, NULL);
INSERT INTO `publish_blog` VALUES (61, 9, '2020-06-07 18:42:00');
INSERT INTO `publish_blog` VALUES (65, 9, '2020-06-08 11:40:00');
INSERT INTO `publish_blog` VALUES (69, 8, '2020-06-08 14:00:00');
INSERT INTO `publish_blog` VALUES (70, 8, '2020-06-08 14:00:00');
INSERT INTO `publish_blog` VALUES (71, 8, '2020-06-08 14:02:00');
INSERT INTO `publish_blog` VALUES (73, 8, '2020-06-08 14:18:00');
INSERT INTO `publish_blog` VALUES (74, 9, '2020-06-08 17:33:00');
INSERT INTO `publish_blog` VALUES (75, 9, '2020-06-08 17:38:00');
INSERT INTO `publish_blog` VALUES (76, 9, '2020-06-08 17:38:00');
INSERT INTO `publish_blog` VALUES (77, 9, '2020-06-08 22:05:00');
INSERT INTO `publish_blog` VALUES (78, 9, NULL);

-- ----------------------------
-- Table structure for search
-- ----------------------------
DROP TABLE IF EXISTS `search`;
CREATE TABLE `search`  (
  `garbage_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `ID` bigint(20) NOT NULL,
  `search_time` datetime(0) NOT NULL,
  INDEX `FK_search2`(`ID`) USING BTREE,
  CONSTRAINT `FK_search2` FOREIGN KEY (`ID`) REFERENCES `user` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_registered` datetime(0) NOT NULL,
  `user_email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_pass` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_birthday` date NULL DEFAULT NULL,
  `gender` tinyint(1) NOT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  UNIQUE INDEX `user_name`(`user_name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (8, 'ly2', '2020-05-26 00:00:00', '1819975371@qq.com', '111111', '1900-12-15', 1);
INSERT INTO `user` VALUES (9, 'Joshua_yi', '2020-05-27 00:00:00', 'liyinankai1@163.com', '123456', '1930-11-12', 1);

-- ----------------------------
-- Table structure for user_info_plus
-- ----------------------------
DROP TABLE IF EXISTS `user_info_plus`;
CREATE TABLE `user_info_plus`  (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `brief_info` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `blog_url` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_identity` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `other` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `city` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `qq` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `wechat` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`ID`) USING BTREE,
  CONSTRAINT `user_info_plus_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `user` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_info_plus
-- ----------------------------
INSERT INTO `user_info_plus` VALUES (8, '11111111111', '12345678911', 'https://www.baidu.com/', 'student', 'other information about you 255 words', 'beijing', '123456789', '123456789');
INSERT INTO `user_info_plus` VALUES (9, 'hhhhhhhhhhhhhhhh', '12345678910', 'http', 'student', 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj', 'tianjin', '1819975371', 'wechatyi');

-- ----------------------------
-- Procedure structure for modify_user_info
-- ----------------------------
DROP PROCEDURE IF EXISTS `modify_user_info`;
delimiter ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `modify_user_info`(
-- user info plus
IN input_info VARCHAR(200),
IN input_other VARCHAR(255),
IN input_phone VARCHAR(11),
IN input_qq VARCHAR(15),
IN input_wechat VARCHAR(20),
IN input_url VARCHAR(100),
IN input_city VARCHAR(20),
IN input_identity VARCHAR(20),
-- user info
IN input_gender TINYINT(1),
IN input_name VARCHAR(20),
IN input_pwd VARCHAR(20),
IN input_birthday VARCHAR(20),
-- other
IN input_email VARCHAR(50),
OUT message VARCHAR(100)
)
BEGIN
	DECLARE type TINYINT(1);
	DECLARE id_tmp BIGINT;
	SET id_tmp = (SELECT ID FROM `user` WHERE user_email = input_email);
	SET message := "default message";
	
	IF (SELECT COUNT(*) FROM user_info_plus WHERE ID=id_tmp) = 0
	THEN 
	SET type=1;
	ELSE
	SET type=2;
	END IF;
	
	IF type = 1
	THEN
	
	INSERT INTO user_info_plus(ID, brief_info, phone, blog_url, user_identity, other, city, qq, wechat)
VALUES(id_tmp, input_info, input_phone, input_url, input_identity, input_other, input_city, input_qq, input_wechat);
	UPDATE `user` SET gender=input_gender, user_name=input_name, user_pass=input_pwd, user_birthday=input_birthday WHERE ID = id_tmp;

	SET message := 'user information modify success';
-- 	SELECT message;
	
	ELSEIF type=2
	THEN

	UPDATE user_info_plus SET brief_info=input_info, phone=input_phone, blog_url=input_url, user_identity=input_identity, other=input_other, city=input_city, qq=input_qq, wechat=input_wechat
	WHERE ID = id_tmp;
	
	UPDATE `user` SET gender=input_gender, user_name=input_name, user_pass=input_pwd, user_birthday=input_birthday WHERE ID = id_tmp;
	SET message := 'user information modify success';
 END IF;
 
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for save_blog
-- ----------------------------
DROP PROCEDURE IF EXISTS `save_blog`;
delimiter ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `save_blog`(
IN title VARCHAR(30),
IN abstract VARCHAR(200),
IN content TEXT,
IN modified_time DATETIME,
IN email VARCHAR(50),
IN type INT,
IN blogID BIGINT,
OUT message VARCHAR(100)
)
BEGIN
	
	DECLARE id_tmp BIGINT;
	SET id_tmp = (SELECT ID FROM `user` WHERE user_email = email);
	SET message := "default message";
				IF LENGTH(title)=0
			THEN
			SET message := 'The title can not be null';
			ELSE
			
	IF type = 1
	THEN
	INSERT INTO blog(blog_title, blog_excerpt, blog_content, blog_modified) VALUES(title, abstract, content, modified_time);
	
	INSERT INTO publish_blog(ID, blog_id) VALUES(id_tmp, LAST_INSERT_ID());
	SET message := 'blog save success';
-- 	SELECT 'blog save success' INTO message;
-- 	SELECT message;
	ELSEIF type=2
	THEN
		IF (SELECT blog_id FROM publish_blog WHERE ID=id_tmp AND blog_id=blogID) IS NULL
		THEN
		SET message := 'This blog does not exist';
-- 		SELECT 'This blog does not exist' INTO message;
-- 		SELECT message;
		ELSE
		

			UPDATE blog SET blog_title = title, blog_excerpt = abstract, blog_content = content, blog_modified = modified_time WHERE blog_id = blogID;
-- 		SELECT 'blog modified success' INTO message;
			SET message := 'blog modified success';
		END IF;
 END IF;
 END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user
-- ----------------------------
DROP TRIGGER IF EXISTS `trg_user_update_check`;
delimiter ;;
CREATE TRIGGER `trg_user_update_check` BEFORE UPDATE ON `user` FOR EACH ROW BEGIN
	DECLARE msg varchar(100);
	
	IF NEW.gender<>1 AND NEW.gender <>0
	THEN
		SET msg = CONCAT('user gender：', NEW.gender,' must be 0 or 1');
		SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
	END IF;

END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user_info_plus
-- ----------------------------
DROP TRIGGER IF EXISTS `trg_user_info_insert_check`;
delimiter ;;
CREATE TRIGGER `trg_user_info_insert_check` BEFORE INSERT ON `user_info_plus` FOR EACH ROW BEGIN
	DECLARE msg varchar(100);
	
	IF LENGTH(NEW.brief_info) > 200
	THEN
		SET msg = CONCAT('brief_info：',NEW.brief_info,' length not meet the requirements(0< <=20)');
		SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
	END IF;
	
	IF LENGTH(NEW.phone) <> 11
	THEN
		SET msg = CONCAT('phonw：',NEW.phone,' length not meet the requirements 11');
		SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
	END IF;
	
	IF LENGTH(NEW.user_identity) >20
	THEN
		SET msg = CONCAT('user identity：', NEW.user_identity,' length not meet the requirements (0< <=20)');
		SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
	END IF;
	
	IF LENGTH(NEW.blog_url)>100
	THEN
		SET msg = CONCAT('blog url：', NEW.blog_url,' length not meet the requirements (0<= <=100)');
		SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
	END IF;
	
	IF LENGTH(NEW.other) > 255
	THEN
		SET msg = CONCAT('user other info ：',other,' length not meet the requirements(0<= <=255)');
		SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
	END IF;
	
	IF LENGTH(NEW.city) >20
	THEN
		SET msg = CONCAT('user city：', NEW.city,' length not meet the requirements (0< <=20)');
		SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
	END IF;
	
	IF LENGTH(NEW.qq) <>0
	THEN
		IF LENGTH(NEW.qq) >15 OR LENGTH(NEW.qq)<5
		THEN
			SET msg = CONCAT('user qq：', NEW.qq,' length not meet the requirements (5<= <=15)');
			SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
		END IF;
	END IF;
	
	IF LENGTH(NEW.wechat) <> 0
	THEN
		IF LENGTH(NEW.wechat) >20 OR LENGTH(NEW.wechat)<6
		THEN
			SET msg = CONCAT('user wechat：', NEW.wechat,' length not meet the requirements (6<= <=20)');
			SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
		END IF;
	END IF;

END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table user_info_plus
-- ----------------------------
DROP TRIGGER IF EXISTS `trg_user_info_update_check`;
delimiter ;;
CREATE TRIGGER `trg_user_info_update_check` BEFORE UPDATE ON `user_info_plus` FOR EACH ROW BEGIN
	DECLARE msg varchar(100);
	
	IF LENGTH(NEW.qq) <>0
	THEN
		IF LENGTH(NEW.qq) >15 OR LENGTH(NEW.qq)<5
		THEN
			SET msg = CONCAT('user qq：', NEW.qq,' length not meet the requirements (5<= <=15)');
			SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
		END IF;
	END IF;
	
	IF LENGTH(NEW.wechat) <> 0
	THEN
		IF LENGTH(NEW.wechat) >20 OR LENGTH(NEW.wechat)<6
		THEN
			SET msg = CONCAT('user wechat：', NEW.wechat,' length not meet the requirements (6<= <=20)');
			SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
		END IF;
	END IF;
	
	IF LENGTH(NEW.phone) <> 11
	THEN
		SET msg = CONCAT('phone：',NEW.phone,' length not meet the requirements 11');
		SIGNAL SQLSTATE 'HY000' SET MESSAGE_TEXT = msg;
	END IF;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
