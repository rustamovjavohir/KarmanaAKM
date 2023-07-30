window.onload = function () {

}

function fillEvent(data) {
    let result = data.results;
    for (const item of result) {
        console.log(item.main_image);
        articleTemplate(item);
    }
}
