// ------------------------------------------------------------------------------------------------------------------

var today = new Date();
var d = today.getDate();
var m = today.getMonth() + 1;
var y = today.getFullYear();

var dateList = '';


function addDates(dates){

    dateList = dates;
}


function getDateList(){
    return dateList ? dateList.match(/.{1,10}/g) : '';
}


$('#dates').multiDatesPicker({
    dateFormat: "yy-mm-dd",
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


// ------------------------------------------------------------------------------------------------------------------


function calculateTotal(){

    var dates = document.getElementById('dates').value;

    if (dates.length)
        dates = dates.split(", ");

    var price = document.getElementById('price').innerHTML;
    var comision = document.getElementById('comision').innerHTML;

    var priceTotal = dates.length * price;
    var comision = priceTotal * 0.08;

    document.getElementById('priceTotal').innerHTML = '$' + priceTotal;
    document.getElementById('comision').innerHTML = '$' + comision;
    document.getElementById('total').value = '$' + (priceTotal + comision);

}
