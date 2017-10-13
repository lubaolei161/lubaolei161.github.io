#!/usr/bin/env python
#-*-coding: UTF-8 -*-

#**********************程序说明*********************************#
#*模块: IDL层：CCTalk首次观看内容用户表（不包括预告）
#*作者：lubaolei
#*时间：2017-09-01
#*备注：
#***************************************************************#

#导入相关模块
import conn2_hive_db as conn_db
#***********************模块说明********************************#
#conn_db模块,封装了mysql、hive数据库接口
#hive_do(sql):函数、执行hive数仓库操作任务
#***************************************************************#

#获取时间参数、执行脚本目标表后缀名:'get start date default=sysdate()-1 '
(v_start_date,v_tag)=conn_db.get_date_tab()

#时间函数处理：增加'\''
v_start_date=repr(v_start_date)


#参数说明：v_tag   ，DW模型层级：默认def、adl、bdl、idl、adl，请通过-t  参数明确指定脚本运行模型层级，不指定：tag文件、log文件将自动存储在def目录。

t_idl_order_status_cctalk = 'idl_order_status_cctalk'
t_idl_order_track_eb = 'idl_order_track_eb'
t_idl_last_active_cctalk = 'idl_last_active_cctalk'

#commend /usr/bin/python -u /home/hadoop/dw_etl/sns/adl/adl_single_league_use_sns.py.bak -t 'xujing_test_idl' -d '2015-04-14' -v

#*********************用户修改区域BEGIN*************************#


#--------------------逻辑代码块<1>------------------------------#

#*****************<<PART-ONE:填写SQL说明文档信息>>**************#

#*****************<<PART-TWO:执行SQL语句>>**********************#
v_sql = v_add_jar + v_sql


#*****************<<PART-THREE:执行模块>>***********************#
#调用conn_db.hive_do(sql,test='exec')执行脚本，默认运行级别为执行：日志后台输出、正常产生tag文件；如果debug级别，日期前台数据输出；
conn_db.hive_do(v_sql)


v_add_jar = '''SET hive.exec.parallel=true;
set hive.exec.compress.intermediate=true;
set mapred.compress.map.output=true;
set mapred.map.output.compression.codec=org.apache.hadoop.io.compress.SnappyCodec;
set hive.exec.compress.output=true;
set mapred.output.compress=true;
set mapred.output.compression.codec=org.apache.hadoop.io.compress.SnappyCodec;
set mapred.output.compression.type=BLOCK;

'''



v_sql = '''



insert overwrite table ''' + t_idl_order_status_cctalk + '''  PARTITION(ds)

select
orderid
,uid             --(取最后)用户ID（沪江ID）
,platform             --(取最后)平台
,os_version             --(取最后)操作系统版本
,app_version             --(取最后)APP版本
,network             --(取最后)网络类型
,client_ip             --(取最后)客户端IP
,country             --(取最后)国家，根据客户端IP
,province             --(取最后)省份，根据客户端IP
,city             --(取最后)城市，根据客户端IP
,channel             --(取最后)渠道
,mfr             --(取最后)设备品牌
,model             --(取最后)设备型号
,resolution             --(取最后)分辨率
,device_name             --(取最后)设备名称
,device_type             --(取最后)设备类型（推断）
,carrier             --(取最后)服务提供商
,wifimac             --(取最后)WIFI的MAC地址
,imsi             --(取最后)用户识别码
,event_identifier             --(取最后)自定义事件标识
,event_id_razor             --(取最后)自定义事件ID(Razor)
,label             --(取最后)自定义事件标签
,event_cnt             --(取最后)对应事件被触发的次数
,activity             --(取最后)当前活跃的Activity
,event_type             --(取最后)自定义事件类别
,event_json             --(取最后)自定义事件扩展信息
,session_id       --(取最后)会话ID
,install_time          --新安装时间戳(取did的安装)
,install_channel          --新安装渠道(取did的安装)
,install_app_version          --新安装APP版本(取did的安装)
,install_event_json          --新安装扩展json(取did的安装)
,session_session_cnt
,session_duration
,ds

from

(
--取与订单间隔最小状态
select t.*,row_number2() over(partition by orderid order by abs(unix_timestamp(server_date)-unix_timestamp(orderdate)) desc ) rn from

(

select
eb.orderid
,eb.orderdate
,status.server_date
,status.uid             --(取最后)用户ID（沪江ID）
,status.platform             --(取最后)平台
,status.os_version             --(取最后)操作系统版本
,status.app_version             --(取最后)APP版本
,status.network             --(取最后)网络类型
,status.client_ip             --(取最后)客户端IP
,status.country             --(取最后)国家，根据客户端IP
,status.province             --(取最后)省份，根据客户端IP
,status.city             --(取最后)城市，根据客户端IP
,status.channel             --(取最后)渠道
,status.mfr             --(取最后)设备品牌
,status.model             --(取最后)设备型号
,status.resolution             --(取最后)分辨率
,status.device_name             --(取最后)设备名称
,status.device_type             --(取最后)设备类型（推断）
,status.carrier             --(取最后)服务提供商
,status.wifimac             --(取最后)WIFI的MAC地址
,status.imsi             --(取最后)用户识别码
,status.event_identifier             --(取最后)自定义事件标识
,status.event_id_razor             --(取最后)自定义事件ID(Razor)
,status.label             --(取最后)自定义事件标签
,status.event_cnt             --(取最后)对应事件被触发的次数
,status.activity             --(取最后)当前活跃的Activity
,status.event_type             --(取最后)自定义事件类别
,status.event_json             --(取最后)自定义事件扩展信息
,status.session_id       --(取最后)会话ID
,status.install_time          --新安装时间戳(取did的安装)
,status.install_channel          --新安装渠道(取did的安装)
,status.install_app_version          --新安装APP版本(取did的安装)
,status.install_event_json          --新安装扩展json(取did的安装)
,status.session_session_cnt
,status.session_duration
,status.ds
from
''' + t_idl_order_track_eb + '''  eb
inner join
(
select

uid             --(取最后)用户ID（沪江ID）
,platform             --(取最后)平台
,server_date             --(取最后)服务器时间
,os_version             --(取最后)操作系统版本
,app_version             --(取最后)APP版本
,network             --(取最后)网络类型
,client_ip             --(取最后)客户端IP
,country             --(取最后)国家，根据客户端IP
,province             --(取最后)省份，根据客户端IP
,city             --(取最后)城市，根据客户端IP
,channel             --(取最后)渠道
,mfr             --(取最后)设备品牌
,model             --(取最后)设备型号
,resolution             --(取最后)分辨率
,device_name             --(取最后)设备名称
,device_type             --(取最后)设备类型（推断）
,carrier             --(取最后)服务提供商
,wifimac             --(取最后)WIFI的MAC地址
,imsi             --(取最后)用户识别码
,event_identifier             --(取最后)自定义事件标识
,event_id_razor             --(取最后)自定义事件ID(Razor)
,label             --(取最后)自定义事件标签
,event_cnt             --(取最后)对应事件被触发的次数
,activity             --(取最后)当前活跃的Activity
,event_type             --(取最后)自定义事件类别
,event_json             --(取最后)自定义事件扩展信息
,session_id       --(取最后)会话ID
,install_time          --新安装时间戳(取did的安装)
,install_channel          --新安装渠道(取did的安装)
,install_app_version          --新安装APP版本(取did的安装)
,install_event_json          --新安装扩展json(取did的安装)
,session_session_cnt
,session_duration
,ds

from ''' + t_idl_last_active_cctalk + '''  where ut='uid' and ds='''+v_start_date+'''
) status

on eb.bbsuserid=status.uid
where to_date(eb.orderdate)='''+v_start_date+'''
)t

)source
where rn=1





'''

v_sql = v_add_jar + v_sql


#*****************<<PART-THREE:执行模块>>***********************#
#调用conn_db.hive_do(sql,test='exec')执行脚本，默认运行级别为执行：日志后台输出、正常产生tag文件；如果debug级别，日期前台数据输出；
conn_db.hive_do(v_sql)








#建表语句


#CREATE TABLE idl_order_status_cctalk(
#     orderid int  comment '订单id',
#     uid   int comment '(取最后)用户ID（沪江ID）',
#     platform   string comment '(取最后)平台',
#     os_version   string comment '(取最后)操作系统版本',
#     app_version   string comment '(取最后)APP版本',
#     network   string comment '(取最后)网络类型',
#     client_ip   string comment '(取最后)客户端IP',
#     country   string comment '(取最后)国家，根据客户端IP',
#     province   string comment '(取最后)省份，根据客户端IP',
#     city   string comment '(取最后)城市，根据客户端IP',
#     channel   string comment '(取最后)渠道',
#     mfr   string comment '(取最后)设备品牌',
#     model   string comment '(取最后)设备型号',
#     resolution   string comment '(取最后)分辨率',
#     device_name   string comment '(取最后)设备名称',
#     device_type   string comment '(取最后)设备类型（推断）',
#     carrier   string comment '(取最后)服务提供商',
#     wifimac   string comment '(取最后)WIFI的MAC地址',
#     imsi   string comment '(取最后)用户识别码',
#     event_identifier   string comment '(取最后)自定义事件标识',
#     event_id_razor   string comment '(取最后)自定义事件ID(Razor)',
#     label   string comment '(取最后)自定义事件标签',
#     event_cnt   bigint comment '(取最后)对应事件被触发的次数',
#     activity   string comment '(取最后)当前活跃的Activity',
#     event_type   string comment '(取最后)自定义事件类别',
#     event_json   string comment '(取最后)自定义事件扩展信息',
#     session_id   string comment '(取最后)会话ID',
#     install_time   bigint comment '新安装时间戳(取did的安装)',
#     install_channel   string comment '新安装渠道(取did的安装)',
#     install_app_version   string comment '新安装APP版本(取did的安装)',
#     install_event_json   string comment '新安装扩展json(取did的安装)',
#     session_session_cnt bigint comment '回话数（时长在1-24*3600）',
#     session_duration    bigint comment 'session 时长'
#)
#comment '下单状态表'
#partitioned by
#(
#     ds string comment '日期,yyyy-MM-dd'
#)
#row format delimited fields terminated by '\001'
#NULL DEFINED AS ''
#stored as SEQUENCEFILE;
