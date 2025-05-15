var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// 여기서부터 

var io=require("socket.io")();
io.listen(1234);
io.sockets.on("connection",function(socket){
//웹페이지에 누가 들어오면 로그 알림 
console.log('🔌 클라이언트 연결됨');
  socket.on("snackRegistered",function(){
    console.log("연결완료");
    io.emit('selectAgainAdd');
  });
  socket.on('newSnackAdded', () => {
    // 모든 사람에게 알림
    io.emit('selectAgain');
  });
  
  socket.on("snackUpdated",function(){
    console.log("데이터 수정됨");
    io.sockets.emit("selectAgainUpd","getP");
  });
  socket.on("snackDeleted",function(){
    console.log("데이터 삭제됨");
    io.sockets.emit("selectAgainDel","getP");
  });
});

//여기까지 내가 만든거. 

app.use('/', indexRouter);
app.use('/users', usersRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
