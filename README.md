rs.config:
{
 "_id" : "replicaSet",
 "version" : 8,
 "protocolVersion" : NumberLong(1),
 "members" : [
  {
   "_id" : 0,
   "host" : "node0:27017",
   "arbiterOnly" : false,
   "buildIndexes" : true,
   "hidden" : false,
   "priority" : 1,
   "tags" : {

   },
   "slaveDelay" : NumberLong(0),
   "votes" : 1
  },
  {
   "_id" : 1,
   "host" : "node1:27017",
   "arbiterOnly" : false,
   "buildIndexes" : true,
   "hidden" : false,
   "priority" : 1,
   "tags" : {

   },
   "slaveDelay" : NumberLong(0),
   "votes" : 1
  },
  {
   "_id" : 2,
   "host" : "node_master:27017",
   "arbiterOnly" : false,
   "buildIndexes" : true,
   "hidden" : false,
   "priority" : 1,
   "tags" : {

   },
   "slaveDelay" : NumberLong(0),
   "votes" : 1
  }
 ],
 "settings" : {
  "chainingAllowed" : true,
  "heartbeatIntervalMillis" : 2000,
  "heartbeatTimeoutSecs" : 10,
  "electionTimeoutMillis" : 10000,
  "getLastErrorModes" : {

  },
  "getLastErrorDefaults" : {
   "w" : 1,
   "wtimeout" : 0
  },
  "replicaSetId" : ObjectId("JPtUKpetQiyfzGpBS5SM")
 }
}

rs.status:
{
 "set" : "replicaSet",
 "date" : ISODate("2019-11-01T08:41:07.801Z"),
 "myState" : 2,
 "term" : NumberLong(6),
 "syncingTo" : "18.218.33.242:27017",
 "heartbeatIntervalMillis" : NumberLong(2000),
 "members" : [
  {
   "_id" : 0,
   "name" : "node0:27017",
   "health" : 1,
   "state" : 2,
   "stateStr" : "SECONDARY",
   "uptime" : 290,
   "optime" : {
    "ts" : Timestamp(1572597171, 1),
    "t" : NumberLong(6)
   },
   "optimeDate" : ISODate("2019-11-01T08:32:51Z"),
   "syncingTo" : "node0:27017",
   "configVersion" : 8,
   "self" : true
  },
  {
   "_id" : 1,
   "name" : "node1:27017",
   "health" : 1,
   "state" : 2,
   "stateStr" : "SECONDARY",
   "uptime" : 289,
   "optime" : {
    "ts" : Timestamp(1572597171, 1),
    "t" : NumberLong(6)
   },
   "optimeDate" : ISODate("2019-11-01T08:32:51Z"),
   "lastHeartbeat" : ISODate("2019-11-01T08:41:07.335Z"),
   "lastHeartbeatRecv" : ISODate("2019-11-01T08:41:07.060Z"),
   "pingMs" : NumberLong(0),
   "syncingTo" : "18.218.33.242:27017",
   "configVersion" : 8
  },
  {
   "_id" : 2,
   "name" : "node_master:27017",
   "health" : 1,
   "state" : 1,
   "stateStr" : "PRIMARY",
   "uptime" : 289,
   "optime" : {
    "ts" : Timestamp(1572597171, 1),
    "t" : NumberLong(6)
   },
   "optimeDate" : ISODate("2019-11-01T08:32:51Z"),
   "lastHeartbeat" : ISODate("2019-11-01T08:41:07.335Z"),
   "lastHeartbeatRecv" : ISODate("2019-11-01T08:41:06.828Z"),
   "pingMs" : NumberLong(0),
   "electionTime" : Timestamp(1572592611, 1),
   "electionDate" : ISODate("2019-11-01T07:16:51Z"),
   "configVersion" : 8
  }
 ],
 "ok" : 1
}
///
see sc1.png
///

Shutting down primary node...
rs.config:
{
 "_id" : "replicaSet",
 "version" : 8,
 "protocolVersion" : NumberLong(1),
 "members" : [
  {
   "_id" : 0,
   "host" : "node0:27017",
   "arbiterOnly" : false,
   "buildIndexes" : true,
   "hidden" : false,
   "priority" : 1,
   "tags" : {

   },
   "slaveDelay" : NumberLong(0),
   "votes" : 1
  },
  {
   "_id" : 1,
   "host" : "node1:27017",
   "arbiterOnly" : false,
   "buildIndexes" : true,
   "hidden" : false,
   "priority" : 1,
   "tags" : {

   },
   "slaveDelay" : NumberLong(0),
   "votes" : 1
  },
  {
   "_id" : 2,
   "host" : "node_master:27017",
   "arbiterOnly" : false,
   "buildIndexes" : true,
   "hidden" : false,
   "priority" : 1,
   "tags" : {

   },
   "slaveDelay" : NumberLong(0),
   "votes" : 1
  }
 ],
 "settings" : {
  "chainingAllowed" : true,
  "heartbeatIntervalMillis" : 2000,
  "heartbeatTimeoutSecs" : 10,
  "electionTimeoutMillis" : 10000,
  "getLastErrorModes" : {

  },
  "getLastErrorDefaults" : {
   "w" : 1,
   "wtimeout" : 0
  },
  "replicaSetId" : ObjectId("JPtUKpetQiyfzGpBS5SM")
 }
}

rs.status:
{
 "set" : "replicaSet",
 "date" : ISODate("2019-11-01T08:44:27.340Z"),
 "myState" : 1,
 "term" : NumberLong(7),
 "heartbeatIntervalMillis" : NumberLong(2000),
 "members" : [
  {
   "_id" : 0,
   "name" : "node0:27017",
   "health" : 1,
   "state" : 1,
   "stateStr" : "PRIMARY",
   "uptime" : 490,
   "optime" : {
    "ts" : Timestamp(1572597795, 1),
    "t" : NumberLong(7)
   },
   "optimeDate" : ISODate("2019-11-01T08:43:15Z"),
   "infoMessage" : "could not find member to sync from",
   "electionTime" : Timestamp(1572597794, 1),
   "electionDate" : ISODate("2019-11-01T08:43:14Z"),
   "configVersion" : 8,
   "self" : true
  },
  {
   "_id" : 1,
   "name" : "node1:27017",
   "health" : 1,
   "state" : 2,
   "stateStr" : "SECONDARY",
   "uptime" : 489,
   "optime" : {
    "ts" : Timestamp(1572597795, 1),
    "t" : NumberLong(7)
   },
   "optimeDate" : ISODate("2019-11-01T08:43:15Z"),
   "lastHeartbeat" : ISODate("2019-11-01T08:44:26.756Z"),
   "lastHeartbeatRecv" : ISODate("2019-11-01T08:44:27.258Z"),
   "pingMs" : NumberLong(0),
   "syncingTo" : "node1:27017",
   "configVersion" : 8
  },
  {
   "_id" : 2,
   "name" : "node_master:27017",
   "health" : 0,
   "state" : 8,
   "stateStr" : "(not reachable/healthy)",
   "uptime" : 0,
   "optime" : {
    "ts" : Timestamp(0, 0),
    "t" : NumberLong(-1)
   },
   "optimeDate" : ISODate("1970-01-01T00:00:00Z"),
   "lastHeartbeat" : ISODate("2019-11-01T08:44:26.791Z"),
   "lastHeartbeatRecv" : ISODate("2019-11-01T08:43:02.899Z"),
   "pingMs" : NumberLong(0),
   "lastHeartbeatMessage" : "Connection refused",
   "configVersion" : -1
  }
 ],
 "ok" : 1
}
///
see sc2.png
///