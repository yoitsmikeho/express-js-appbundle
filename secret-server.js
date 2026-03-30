// This is a simple Node.js server that serves a secret message.
// The secret message is stored in a variable and is not exposed in the code.
// The server listens on port 8080 and responds with a message when accessed.
var pat = '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';

const http = require('http');

http.createServer((request, response) => {

	response.writeHead(200, {
		'Content-Type': 'text/plain'
	});
	response.write('Hello from Pieces!');
	response.end();

}).listen(8080);

console.log('server running on port 8080'); 
