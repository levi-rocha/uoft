/*

Template for broadcasting message

wss.broadcast(JSON.stringify({
	'label': 'abort desktop connection'
}));

*/

var WebSocketServer = require('ws').Server
var wss = new WebSocketServer({port:10020}); // TODO: CHANGE TO YOUR OWN PORT
console.log("ws server running on port 10020");

var hasDesktop = 0;
var players = 0;
var gameStarted = 0;

wss.on('close', function() {
    console.log('disconnected');
});

wss.broadcast = function(message){
	var i;
	for(i=0;i<this.clients.length;i++){	
		this.clients[i].send(message);
	}
}

wss.kick = function(){
	var i;
	for(i=0;i<this.clients.length;i++){	
		this.clients[i].close();
	}
}

wss.on('connection', function(ws) {
	// New client connected
	ws.on('message', function(message) {
		// Received a message from a client
		var msg = JSON.parse(message);
					switch(msg.label) {
						case 'desktop connected':
							if (hasDesktop) {
								wss.broadcast(JSON.stringify({
									'label': 'abort desktop connection'
								}));
							} else {
								wss.broadcast(JSON.stringify({
									'label': 'accepted desktop connection'
								}));
							}
							break;
						case 'player connected':
							if (players > 5 || gameStarted) {
								wss.broadcast(JSON.stringify({
									'label': 'abort player connection'
								}));
							} else {
								players += 1;
								wss.broadcast(JSON.stringify({
									'label': 'accepted player connection',
									'pid': players
								}));
							}
							break;
						case 'start game':
							gameStarted = 1;
							wss.broadcast(JSON.stringify({
								'label': 'started game'
							}));
							break;
						case 'new round':
							wss.broadcast(JSON.stringify({
								'label': 'new round',
								'figure1': msg.figure1,
								'color1': msg.color1,
								'figure2': msg.figure2,
								'color2': msg.color2,
								'hardcore': msg.hardcore,
								'animated': msg.animated,
								'moving': msg.moving
							}));
							break;
						case 'player choice':
							wss.broadcast(JSON.stringify({
								'label': 'player choice',
								'pid': msg.pid,
								'choice': msg.choice
							}));
							break;
						case 'round over':
							wss.broadcast(JSON.stringify({
								'label': 'round over'
							}));
							break;
						case 'game over':
							wss.broadcast(JSON.stringify({
								'label': 'game over',
								'winner': msg.winner,
								'score': msg.score
							}));
							hasDesktop = 0;
							players = 0;
							wss.kick();
							break;
						case 'desktop disconnected':
							hasDesktop = 0;
							players = 0;
							wss.kick();
							break;
						default:
							// Nothing
					}
	});
});

// express serving front
var express = require('express');
var serveStatic = require('serve-static');
var app = express();
app.use(serveStatic(__dirname));
app.listen(10021);

// fetch files via 
// http://cslinux.utm.utoronto.ca:10021/blitz.html
// or
// http://cslinux.utm.utoronto.ca:10021/join.html
