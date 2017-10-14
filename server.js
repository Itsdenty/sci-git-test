var express = require('express');
var path = require('path');
var serveStatic = require('serve-static');

app = express();
app.use(serveStatic('/dist'));

var port = process.env.PORT || 8090;
app.listen(port);