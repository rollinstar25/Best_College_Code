//Turtle Flipper
//This is the simple one

//What it will need
/*
1. unlimited levels with increasing time limits
2. counts how many times someone clicks during the time limit method:countClicks
3. at the end of every level the turtle is flipped 
4. Displays the high scores after each level is complete
5. options to replay level or move on
6. the number of seconds is calculated by Fibonacci, method: calculateTime
7. resets when you exit.

*/

//App
const express = require('express') //imports express
const app = express() //initializes express
const port = 8080 //sets port number or listening point
var path = require('path');

app.use(express.static('turtle_media'))

app.get('/', (req, res) => res.sendfile(path.join(__dirname, '/turtleIndex.html')));

app.listen(port, () => console.log(`Listening on port ${port}!`)) //creates the server
