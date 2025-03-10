import re


def delete_html_tags(html: str) -> str:
    result = re.sub(r'<[^>]+>', '', html)
    return result


site = """<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport"
          content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous">

    <title>Жарт про функції</title>
</head>
<body>
<div class="container">
    <nav class="navbar navbar-expand-lg navbar-light"
         style="background-color: #e3f2fd;">
        <a class="navbar-brand" href="/">Блог</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse"
                data-target="#navbarNavDropdown"
                aria-controls="navbarNavDropdown"
                aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse " id="navbarNavDropdown">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item ">
                    <a class="nav-link" href="/accounts/login/ ">Вхід</a>
                </li>
                <li class="nav-item ">
                    <a class="nav-link"
                       href="/accounts/register/ ">Реєстрація</a>
                </li>

            </ul>
        </div>
    </nav>
</div>
<div class="container">
    <div class="row my-5">
        <div class="col-lg">
            <h1>Жарт про функції</h1>
            <p>
            <p>Ідуть дві функції — Декоратор і Генератор — через ліс. В одній з них раптом стався ексепшен.</p>

            <p>— Ох, я впала! — сказала Функція-Декоратор. — Піди, поклич мій ексепшен!</p>

            <p>— А що це таке, ексепшен? — запитав Функція-Генератор.</p>

            <p>— Ну, він зазвичай знає, що робити, коли я падаю!</p>

            <hr>


        </div>

    </div>
</div>
<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
        integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
        crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
        integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
        integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
        crossorigin="anonymous"></script>
</body>
</html>"""
print(delete_html_tags(site))
