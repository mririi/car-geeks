const express = require('express')
var history = require('connect-history-api-fallback')
const path = require('path')
const serveStatic = require('serve-static')
app.use(history({
    // OPTIONAL: Includes more verbose logging
    verbose: true
}))
const app = express()
app.use('/',serveStatic(path.join(__dirname,'/dist')))
const port = process.env.PORT || 8080

app.listen(port)