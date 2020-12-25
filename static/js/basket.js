// Запрос в JS так называемый AJAX запросы  для независимой обработки запросов
// и обновления только частично, а не всего экрана
window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;
        console.log(t_href.name)
        console.log(t_href.value)
        // Здесь на стороне клиента обрабатывается только клики 
        // данные страниц и количества, далее все это поступает на сервер
        // И на сервере происходит обработка этого AJAX запроса
        $.ajax({
            url: "/baskets/edit/" + t_href.name + "/" + t_href.value + "/",
            // Здесь мы прописывам URL /baskets/edit/ номер id товара/ его количество/
            // B в метод объекта на обработку 3 элемента
            success: function (data) {
                $('.basket_list').html(data.result);
            },
            // Получили ответ от метода объекта /baskets/edit/ в виде JSONResponce
            // и отобразили на странице .basket_list, то есть обновили часть страницы
        });

        event.preventDefault();
    });
}