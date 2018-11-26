$(document).ready(function() {
    $('#get-cors-btn').click(function() {
        $.get("http://localhost:5000/get-cors", function(data){
            console.log(data);
        });
    });

    $('#post-cors-btn').click(function() {
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

    $('#ngx-get-cors-btn').click(function() {
        $.get("http://test.topbook.cc/ngx-get-cors", function(data){
            console.log(data);
        });
    });

    $('#ngx-post-cors-btn').click(function() {
        $.ajax({
            type: "POST",
            timeout: 10000, // 超时时间 10 秒
            headers: {
                'Content-Type':'application/json'
            },
            xhrFields: {
                withCredentials: true
            },
            url: "http://test.topbook.cc/ngx-post-cors",
            data : '{"name":abc}',
            success: function(data) {
                console.log(data);
            },
            error: function(err) {alert("error");},
            complete: function(XMLHttpRequest, status) {}
        });
    });
});