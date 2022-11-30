const https = require('https');
const fs = require('fs');
const express = require('express');
const path = require('path');

const app = express();

const key = fs.readFileSync('OpenSSL/bin/key.pem');
const cert = fs.readFileSync('OpenSSL/bin/cert.pem');


app.get('/', (req, res) => {
    res.status(200).sendFile(path.join(__dirname, '/index.html'))
});

https.createServer({key, cert},app).listen(3000);

console.log('Servidor aberto em https://localhost:3000');