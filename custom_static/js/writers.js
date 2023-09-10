$(document).ready(function () {
    console.log("writers.js loaded");
    // activeHeader();
});


// function activeHeader() {
//     let header = document.getElementById("xizmatlar-header");
//     header.classList.add("active");
//
// }

function getWritessList(category = null, page = null) {
    let data = {};
    if (category) {
        data['category'] = category;
    }
    if (page) {
        data['page'] = page;
    }
    $.ajax({
        url: '/api/event/list/',
        type: 'GET',
        dataType: 'json',
        data: data,
        params: {
            'page': 1,
            'page_size': 1
        },
        success: function (data) {
            // console.log(data);
            fillEvent(data);
        },
        error: function (error) {
            console.log(error);
        }
    });
}