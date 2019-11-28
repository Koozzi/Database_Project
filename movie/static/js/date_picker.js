//----------variables----------//
var d = new Date();
var day = "";
var month = "";
var year = "";
var currentDate = "";
var monthStartDay = "";
var inputDate = "";

var monthTextArray = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

var dayTextArray = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

//----------functions----------//

function getMonthInfo(year, month) {

  //use current month to find number of days in month
  //i dont know why i have to add 1 to month
  var startDate = new Date(year, month + 1, 0);
  var monthLength = startDate.getDate();

  var startDate = new Date(year, month, 1);
  var monthStartDay = startDate.getDay();

  return [monthLength, monthStartDay];

}

function drawCal(monthInfo) {

  var daysInMonth = monthInfo[0];
  var monthStartDays = monthInfo[1];
  var todate = d.getDate();
  var tomonth = d.getMonth();
  var toyear = d.getFullYear()

  //clear cal tbody
  $("#cal").empty();
  $("#cal").append("<tr><td>SUN</td><td>MON</td><td>TUE</td><td>WED</td><td>THUR</td><td>FRI</td><td>SAT</td>");

  //create empty row, append to to tbody
  var $rowOut = $("<tr></tr>");
  $("#cal").append($rowOut);

  //shift first row by month start date
  for (var i = 1; i <= monthStartDays; i++) {
    var $day = "<td></td>";
    $("#cal tr:last").append($day);
  }

  //for each day, append a td to the row
  for (var i = 1; i <= daysInMonth; i++) {
    if (year == toyear && month == tomonth && i >= todate) {
      var $day = "<td class='want_date'><a>" + (i) + "</a></td>";
      $("#cal tr:last").append($day);
      if ((i + monthStartDays) % 7 == 0 & i != 0) {
        $("#cal").append($rowOut);
        $rowOut = "<tr></tr>";
        $("#cal").append($rowOut);
      }
    }
    if (year == toyear && month == tomonth && i < todate) {
      var $day = "<td class='not_date'>" + (i) + "</td>";
      $("#cal tr:last").append($day);
      if ((i + monthStartDays) % 7 == 0 & i != 0) {
        $("#cal").append($rowOut);
        $rowOut = "<tr></tr>";
        $("#cal").append($rowOut);
      }
    }
    if (year == toyear && month < tomonth) {
      var $day = "<td class='not_date'>" + (i) + "</td>";
      $("#cal tr:last").append($day);
      if ((i + monthStartDays) % 7 == 0 & i != 0) {
        $("#cal").append($rowOut);
        $rowOut = "<tr></tr>";
        $("#cal").append($rowOut);
      }
    }
    if (year == toyear && month > tomonth) {
      var $day = "<td class='want_date'><a>" + (i) + "</a></td>";
      $("#cal tr:last").append($day);
      if ((i + monthStartDays) % 7 == 0 & i != 0) {
        $("#cal").append($rowOut);
        $rowOut = "<tr></tr>";
        $("#cal").append($rowOut);
      }
    }

    if (year > toyear) {
      var $day = "<td class='want_date'><a>" + (i) + "</a></td>";
      $("#cal tr:last").append($day);
      if ((i + monthStartDays) % 7 == 0 & i != 0) {
        $("#cal").append($rowOut);
        $rowOut = "<tr></tr>";
        $("#cal").append($rowOut);
      }
    }
    if (year < toyear) {
      var $day = "<td class='not_date'>" + (i) + "</td>";
      $("#cal tr:last").append($day);
      if ((i + monthStartDays) % 7 == 0 & i != 0) {
        $("#cal").append($rowOut);
        $rowOut = "<tr></tr>";
        $("#cal").append($rowOut);
      }
    }
  }

  //if day 7 (w/shift), append row contaning 7 days to tbody and clear row

}


//----------wiring----------//

$(".button_left").click(function () {

  
  
  month--;


  if (month < 0) {
    year--;
    month = 11;
  }

 

  //left button click
  $(".cal_head span").text(monthTextArray[month] + " " + year);
  drawCal(getMonthInfo(year, month));

});

//right button click
$(".button_right").click(function () {
 

  month++;

  if (month > 11) {
    year++;
    month = 0;
  }

  $(".cal_head span").text(monthTextArray[month] + " " + year);
  drawCal(getMonthInfo(year, month));

});

// $("#cal").on("click", ".want_date", function (e) {
//
//   e.preventDefault();
//   $(".want_date").css("background-color",'papayawhip');
//   $(this).css("background-color","orange");
//   // $(this).parent().addClass("circle");
//   var s = $(this).text()
//   // s = s.split('<');
//   var outputDate = monthTextArray[month] + " " + s + ", " + year;
//   inputDate = year + "-" + month + "-" + s;
//   console.log(outputDate);
//   $("#outputText").text(outputDate);
//   $("#dateinput").val(inputDate);
// });






//----------run----------//

//get current month and year
currentDate = new Date();
year = currentDate.getFullYear();
month = currentDate.getMonth();

//get text month name from month number and write to span
$(".cal_head span").text(monthTextArray[month] + " " + year);

//inital calander draw based on current month
drawCal(getMonthInfo(year, month));

$("#cal").on("click", ".want_date", function (e) {
    e.preventDefault();
    $(this).css("background-color","orange");
    $(this).parent().addClass("circle");
    var s = $(this).text()
    var outputDate = monthTextArray[month] + " " + s + ", " + year;
    real_month = month+1
    inputDate = year + "-" + real_month + "-" + s;
    console.log(outputDate);
    $("#outputText").text(outputDate);
    $("#dateinput").val(inputDate);
});