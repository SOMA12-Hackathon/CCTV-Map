const express = require("express");
const db = require("../config/db_con");

const router = express.Router();

const query = "SELECT *, (6371*acos(cos(radians(?))*cos(radians(latitude))*cos(radians(longitude) " + 
			  "-radians(?))+sin(radians(?))*sin(radians(latitude)))) " + 
			  "AS distance " + 
			  "FROM CCTV HAVING distance <= ?";

router.post("/get_cctv_list", (req, res, err) => {
	const { latitude, longitude, radius } = req.body;
	
	if(!latitude || !longitude || !radius) return res.status(400).json({
		status:"error",
		msg:"requirements error"
	});
	
	db.query(query, [latitude + 0.0, longitude + 0.0, latitude + 0.0, radius + 0.0], (err, result) => {
		if (err) throw err;
		console.log(result);
		res.status(200).json({
			status:"success",
			length:result.length,
			result:result
		});
	});
});

module.exports = router;