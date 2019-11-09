var today = new Date();
var d = today.getDate();
var m = today.getMonth() + 1;
var y = today.getFullYear();

var dateList = '';


function addDates(dates){
    //var datelist = dates.split("/");
    dateList = dates;
    //dateList = dates.match(/.{1,10}/g);
    //console.log(datelist);
}


function getDateList(){
    return dateList ? dateList.match(/.{1,10}/g) : '';
}


$('#mdp-demo').multiDatesPicker({
    dateFormat: "m-d-yy",
    // defaultDate:m + '-' + d +'-' + y,
    beforeShowDay: function(date) {
            // var enableddates = ["11-3-2019","11-24-2019", "11-25-2019", "11-26-2019", "11-30-2019", "12-3-2019", "12-4-2019"];
            var enableddates = getDateList();
            var m = date.getMonth() + 1;
            var d = date.getDate();
            var y = date.getFullYear();
            var currentdate = y + '-' + addZero(m) + '-' + addZero(d);

            for (var i = 0; i < enableddates.length; i++) {
                if ($.inArray(currentdate, enableddates) == -1 ) {
                    return [false];
                }
            }
            return enableddates;
    }
});


function addZero(number){
    return (number < 10) ? '0' + number : number;
}
