const http = require('http');

// Create a server HTTP
const app = http.createServer((req, res) => {
  // define the heading of the answer
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  // Esend the answer
  res.end('Hello Holberton School!');
});

// Host the server on port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Export the server
module.exports = app;
