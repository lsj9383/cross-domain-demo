$(document).ready(function() {
    $('#get-cors-btn').click(function() {
        alert("ready?");
        $.get("http://localhost:5000/get-cors", function(data){
            console.log(data);
        });
    });

    $('#post-cors-btn').click(function() {
        alert("ready?");
        $.ajax({
            type: "POST",
            timeout: 10000, // 超时时间 10 秒
            headers: {
                'Content-Type':'application/json'
            },
            xhrFields: {
                withCredentials: true
            },
            url: "http://localhost:5000/post-cors",
            data : '{"name":abc}',
            success: function(data) {
                console.log(data);
            },
            error: function(err) {alert("error");},
            complete: function(XMLHttpRequest, status) {}
        });
    });   
});