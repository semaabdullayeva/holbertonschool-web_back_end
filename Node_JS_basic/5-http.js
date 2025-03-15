const http = require('http');

const app = http.createServer(function(req, res) {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  
  const url = req.url;

  if (url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  }
  else if (url === '/students') {
    res.write('This is the list of our students');
    
    res.end();
  }
});

app.listen(1242, () => {
  console.log('...');
});

module.exports = app;