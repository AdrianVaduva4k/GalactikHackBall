var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'hackdb.cowzyzuil4nn.us-east-2.rds.amazonaws.com',
  user     : 'root',
  password : 'rootroot',
  database : 'Galactik'
});

String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search, 'g'), replacement);
};

var spawn = require('child_process').spawn

connection.connect();

var restify = require('restify');

var server = restify.createServer();

server.use(restify.plugins.bodyParser({
    mapParams: true
}));

server.use(
  function crossOrigin(req,res,next){
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    return next();
  }
);

server.post('/signUp', function(req, res, next) {
  connection.query('INSERT INTO users set ?', {user_name: req.params.name, user_email: req.params.email, user_password: req.params.psw, user_teamname: req.params.teamname}, function (error, results, fields) {
  if (error) throw error;
  var dataString = ""
  console.log(results.insertId);
  var py  = spawn('python3', ['PythonScript/Team.py'])
  py.stdout.on('data', function(data){
    dataString += data.toString();
    });
    py.stdout.on('end', function(){
       var teams = JSON.parse(dataString.replaceAll('\'', '"'))
       console.log(teams)
    
      var teamsInsert = []
      for (var index in teams.players) {
        var item = teams.players[index]
        teamsInsert.push( {
          player_name: item.nameOfPlayer,
          player_race: item.raceOfPlayer,
          player_stamina: item.playerStamina + "", 
          player_deffence: item.playerDeffence +"",
          player_attack: item.playerAtack+"",
          player_overall: item.overallOfPlayer+""
        })
      }
      
      for (var index in teamsInsert) {
         var sql = "INSERT INTO players SET ?";        

      connection.query(sql, teamsInsert[index], function(err) {
        console.log(err)
       
    })
      }
      
     
   });
   res.send(results)
        next();
 });
});

server.post('/genEnemy', function(req, res, next) {
  var dataString = ""
  var py  = spawn('python3', ['PythonScript/EnemyTeam.py'])
  py.stdout.on('data', function(data){
    dataString += data.toString();
    });
    py.stdout.on('end', function(){
       var teams = JSON.parse(dataString.replaceAll('\'', '"'))
       
      var teamsInsert = []
      for (var index in teams.players) {
        console.log(teams)
        var item = teams.players[index]
        teamsInsert.push( {
          player_name: item.nameOfPlayer,
          player_race: item.raceOfPlayer,
          player_stamina: item.playerStamina + "", 
          player_deffence: item.playerDeffence +"",
          player_attack: item.playerAtack+"",
          player_overall: item.overallOfPlayer+""
        })
      }
      
      for (var index in teamsInsert) {
         var sql = "INSERT INTO playersen SET ?";        

      connection.query(sql, teamsInsert[index], function(err) {
        console.log(err)
        
    })
      }
      next();
     //res.send(res)
    
   });
   
});

server.post('/signIn', function(req, res, next) {
   connection.query('SELECT * from users WHERE user_email = ? AND user_password = ?', [req.params.email, req.params.psw],  function (error, results, fields) {
    if (error) throw error;
  
    if(results.length > 0)
      res.send(results);
      next();
  });
  
});

server.get('/users', function(req, res, next) {
   connection.query('SELECT * from users', function (error, results, fields) {
    if (error) throw error;
     res.send(results);
    next();
  });
  
});

server.listen(8080, function() {
  console.log('%s listening at %s', server.name, server.url);
});