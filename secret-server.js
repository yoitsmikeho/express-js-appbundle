var aws_access_key_id = "AKIA1234567890FAKE"
var aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
var github_token="ghp_ddM8q3nuSCvZjVhMcs3zcOF2E1fJXF4B5iBE"
var gitlab_token="glpat-jhbdfkjbdfb"
const http = require('http');

http.createServer((request, response) => {

	response.writeHead(200, {
		'Content-Type': 'text/plain'
	});
	response.write('Hello from Pieces!');
	response.end();

}).listen(8080);

console.log('server running on port 8080'); 