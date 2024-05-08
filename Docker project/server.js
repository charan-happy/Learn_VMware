var express = require('express')
var path = require('path')
var fs = require('fs')
var app = express();

app.get('/', function (req, res) {
    res.sendFile(path.join(_dirname, "index.html"));
});

app.get('/profile-picture', function (req, res){
    var img = fs.readFileSync('prfile-1.jpg');
    res.writehead(200, {'content-type': 'image/jpg'} );
    res.end(img, 'binary');
});

app.listen(5500, function() {
    console.log("app listening on port 5500");
});