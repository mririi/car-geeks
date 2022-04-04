const express = require('express')
const path = require('path')
const app = express()
app.use('/',serveStatic(path.join(__dirname,'/dist')))
