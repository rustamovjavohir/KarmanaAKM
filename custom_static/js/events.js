window.onload = function () {
    let url = new URL(window.location.href);
    let category = url.searchParams.get('category');
    let page = url.searchParams.get('page');
    getEventsList(category, page);
    getEventCategoriesList();
    $('#event-search-button').on('click', function () {
        let search = $('#event-search-input').val();
        searchEvents(search);
        console.log(search);
    });
}


function searchEvents(value) {
    $.ajax({
        url: '/api/event/list/',
        type: 'GET',
        dataType: 'json',
        params: {
            'search': value
        },
        success: function (data) {
            console.log(data);
            fillEvent(data);
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function getEventsList(category = null, page = null) {
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


function fillEvent(data) {
    let result = data.results;
    clearEvent();
    for (const item of result) {
        articleTemplate(item);
    }
}


function clearEvent() {
    $('#article').html('');
}

function articleTemplate(article) {
    $('#article').append(
        '<article class="entry">' +
        articleImage(article) +
        articleTitle(article) +
        articleMeta(article) +
        articleContent(article) +
        '</article>'
    );


}

function timeFormatter(time) {
    const monthNames = [
        'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
    ];
    let date = new Date(time);
    let year = date.getFullYear();
    let month = monthNames[date.getMonth()];
    let day = date.getDate();
    let hours = date.getHours();
    let minutes = date.getMinutes();

    // return year + '-' + month + '-' + day;
    return `${day} ${month} ${year} г. ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;

}

function articleImage(article) {
    let image =
        '<div class="entry-img">' +
        '<img src="' + article.main_image + '" alt="" class="img-fluid">' +
        '</div>'
    return image;
}

function articleTitle(article) {
    let articleUrl = article.id;
    let title =
        '<h2 class="entry-title">' +
        '<a href="' + articleUrl + '">' + article.name + '</a>' +
        '</h2>'
    return title;
}

function articleMeta(article) {
    let meta =
        '<div class="entry-meta">' +
        '<ul>' +
        '<li class="d-flex align-items-center"><i class="icofont-user"></i>' +
        '<i class="bi bi-person"></i>' + article.user + '</li>' +
        '<li class="d-flex align-items-center"><i class="icofont-wall-clock"></i>' +
        '<i class="bi bi-clock"></i>' +
        '<time datetime="2020-01-01">' + timeFormatter(article.created_at) + '</time></li>' +
        '</ul>' +
        '</div>'
    return meta;
}

function articleContent(article) {
    let content =
        '<div class="entry-content">' +
        '<p>' + article.description + '</p>' +
        '<div class="read-more">' +
        '<a href="' + article.id + '">Batafsil</a>' +
        '</div>' +
        '</div>'
    return content;
}


function getEventCategoriesList() {
    $.ajax({
        url: '/api/books/categories/',
        type: 'GET',
        dataType: 'json',
        data: {
            is_event: true,
        },

        success: function (data) {
            fillEventCategory(data);
        },
        error: function (error) {
            console.log(error);
        }
    });
}


function clearCategory() {
    $('#categories').html('');
}

function categoryTemplate(category) {
    let categoryUrl = category.slug;
    let categoryTemplate =
        '<li><a href="?category=' + categoryUrl + '">' + category.name + '</a></li>';
    return categoryTemplate;
}

function fillEventCategory(data) {
    let categoryId = $('#categories');
    let result = data.results;
    clearCategory();
    for (const item of result) {
        categoryId.append(categoryTemplate(item));
    }
}


function fillPagination(data) {
    let pagination = $('#pagination');
    let result = data.results;
    clearPagination();
    for (const item of result) {
        pagination.append(paginationTemplate(item));
    }
}