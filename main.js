const express = require("express");
const bodyParser = require("body-parser");
const logger = require("morgan");
const cors = require("cors");
// const index = require("./routes/index");
const api = require("./routes/api");

const app = express();

app.use(logger("combined"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cors("*"));
// app.use("/", index);
app.use("/api", api);

app.get("/", (req, res, err) => {
	res.status(200).sendFile(__dirname+"/views/test.html");
});

app.listen(3000, () => {
	console.log("Test app listening on port 3000!")
});