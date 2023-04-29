const http = require('http');
const net = require('net');
const fs = require('fs')

// Listen on port 8080
let requestListener = function (req, res) {
  res.end("Hello World!");
}

const server = http.createServer(requestListener);

// Configure for Windows or Linux depending on environment
if (process.platform === 'win32') {
  const hostname = 'localhost';
  const port = 8080;

  // Bind to localhost only
  server.listen(port, () => {
    console.log(`listening at http://${hostname}:${port}/`);
  });
} else {
  const hostname = `127.0.0.1`;
  const port = 8080;

  // Bind to loopback interface
  server.bind((hostname || 'localhost').split(':')[0]);
  server.listen(port, () => {
    console.log(`listening at http://${hostname}:${port}