CSC309 Assignment 3
Spring 2016 - UTM

Student: Ives Levi Diniz Rocha
Student #: 1002813459

Instructions on how to play the game:
	[The following links assume you are hosting the server on cslinux.]
	- Run 'node server.js' to start the server.
	- Visit http://cslinux.utm.utoronto.ca:10021/index.html to read the game's instructions.
	- Press 'Play game' to go to the hosting page on the main screen.
	- Have all players visit http://cslinux.utm.utoronto.ca:10021/join.html on their phones to join the game. Up to 6 players can join a game.
	- If any players are playing remotely and can't see the main screen, have them visit the observer link on their computer: http://cslinux.utm.utoronto.ca:10021/observe.html
	- Make sure the desired options are selected in the hosting screen:
		-- The first option dictates how many rounds the game is going to have.
		-- Hardcore mode % is the amount of rounds that will be played in hardcore mode. In hardcore mode, the background animates faster, the figures move faster and alternate between visible and invisible, in order to make the game harder. Points are also doubled when in hardcore mode. This mode is not recommended for people with a history of seizures-- The other options dictate whether the figures and the background are animated and if the music is playing.
	- After all players have joined, press 'Start game'. The game will start and the controls will be enabled for all players. Good luck!

Required features achieved:
	- I believe all required features have been achieved by my code.

Additional features achieved:
	- Game play of more than 2 players:
		-- Game can be played by 1-6 players. Code can easily be changed to allow as many players as the server can handle.
	- Extensive use of HTML Canvas: 
		-- All the figures are drawn and animated via canvas work.
	- Impressive visual appearance: 
		-- Colorful and animated background and text.
		-- All the animations for background and text are done in CSS.
		-- Hardcore mode presents even more visuals.
	- Responsive and smooth game play:
		-- Game is optmized so the reaction time of players is considered when scoring.
		-- Controls are disabled after player has already made a choice.
		-- Score is shown in real time on the main screen.
		-- All players (and observers) receive game over feedback at end of game.
	- Other features:
		-- Index page includes detailed instructions on how to play.
		-- Observer page allows players to play the game remotely online.
		-- Customizable options to fit all players' needs and tastes.
		-- Original soundtrack composed by myself.
		-- I did everything by myself. Please go easy on me. Thanks for playing!