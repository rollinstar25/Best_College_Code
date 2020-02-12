//App For The Product Pobularity Calculator

const express = require('express') //imports express
const app = express() //initializes express
const port = 8080 //sets port number or listening point
var path = require('path');


app.use(express.static('public'))

app.get('/', (req, res) => res.sendFile(path.join(__dirname, '/index.html')));
app.get('/elves', (req, res) => res.sendFile(path.join(__dirname, '/elves.html')));
app.get('/accessories', (req, res) => res.sendFile(path.join(__dirname, '/accessories.html')));
app.get('/elvisPresley', (req, res) => res.sendFile(path.join(__dirname, '/elvisPresley.html')));
app.get('/gothic', (req, res) => res.sendFile(path.join(__dirname, '/gothic.html')));
app.get('/flashlight', (req, res) => res.sendFile(path.join(__dirname, '/flashlight.html')));
app.get('/present', (req, res) => res.sendFile(path.join(__dirname, '/present.html')));


app.listen(port, () => console.log(`Listening on port ${port}!`)) //creates the server
