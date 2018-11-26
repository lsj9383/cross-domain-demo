function jsonp_callback(result) {
    console.log(result)
}

$(document).ready(function() {
    $('#jsonp-cors-btn').click(function() {
        $.ajax({
            url: 'http://localhost:5000/get-jsonp-cors',
            dataType: "jsonp",
            jsonp: "callback",
            success: function (result) {
                console.log(result)
            }
        })
    });
});
