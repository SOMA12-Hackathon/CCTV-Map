const mysql = require("mysql");

const HOST 		= "127.0.01",
	  PORT 		= "3306",
	  USER 		= "soma",
	  PASS 		= "soma123",
	  DBNAME 	= "cctv_map";

module.exports = mysql.createConnection({
  host: HOST,
  port: PORT,
  user: USER,
  password: PASS,
  database: DBNAME
});