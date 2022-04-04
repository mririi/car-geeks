const express = require('express')

const path = require('path')

const serveStatic = require('serve-static')

const app = express()

app.use("/", express.static(path.join(__dirname, "/dist")))

const port = process.env.PORT || 8080

app.listen(port)