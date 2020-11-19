# Django-Polls-API
Выполнение тестового задания по созданию API для проведения опросов.

<h1>Инструкция по API-интерфейсу</h1>

Работа с приложением осуществляется посредством направления HTTP-запросов серверу с запущенным приложением.<br>
Адреса для обращения указаны относительно сервера. Например, для адреса http://www.your-server.com/<b>api/token/</b> будет указан относительный путь <b>api/token/</b><br>

<h3>1. Администрирование</h3>

<h5>Авторизация</h5>

Для получения доступа к функциям администрирования необходимо авторизоваться и получить токен аутентификации.<br>
Адрес: <b>api/token/</b><br>
Запрос: <b>POST</b><br>
Параметры:<br>
<ul>
  <li><b>"username"</b>: "имя пользователя"</li>
  <li><b>"password"</b>: "пароль"</li>
</ul>
Ответ:<br>
<ul>
  <li><b>"refresh"</b>: "токен для обновления токена доступа"</li>
  <li><b>"access"</b>: "токен доступа для аутентификации<"/li>
</ul>

Токен доступа имеет срок жизни, по истечению которого становится неактивен.<br>
Чтобы обновить токен доступа не обязательно проходить авторизацию заново, достаточно получить новый токен с помощью токена обновления.<br>
Адрес: <b>api/refresh/</b><br>
Запрос: <b>POST</b><br>
Параметры:<br>
<ul>
  <li><b>"refresh"</b>: "токен для обновления токена доступа"</li>
</ul>
Ответ:<br>
<ul>
  <li><b>"access"</b>: "токен доступа для аутентификации<"/li>
</ul>

Для доступа к разделам администрирования необходимо передавать токен доступа в заголовке запроса:<br>
<b>"Authorization"</b>: "Bearer токен-доступа"<br>

<h5>Управление опросами</h5>

Сначала необходимо создать опрос. После этого можно будет создавать вопросы для этого опроса.<br><br>

Получить список всех опросов.<br>
Адрес: <b>api/polls/</b><br>
Запрос: <b>GET</b><br>
Параметры: без параметров.<br>
Ответ: список опросов<br>
<ul>
  <li><b>"id"</b>: "id опроса"</li>
  <li><b>"title"</b>: "Название опроса"</li>
  <li><b>"description"</b>: "Описание опроса"</li>
  <li><b>"start_date"</b>: "Дата начала опроса"</li>
  <li><b>"end_date"</b>: "Дата завершения опроса"</li>
</ul>

Создать новый опрос.<br>
Адрес: <b>api/polls/</b><br>
Запрос: <b>POST</b><br>
Параметры:<br>
<ul>
  <li><b>"title"</b>: "Название опроса (не больше 255 символов)"</li>
  <li><b>"description"</b>: "Подробное описание опроса"</li>
  <li><b>"start_date"</b>: "Дата начала опроса в формате YYYY-MM-DD"</li>
  <li><b>"end_date"</b>: "Дата завершения опроса в формате YYYY-MM-DD"</li>
</ul>
Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>

Изменить существующий опрос.<br>
Адрес: <b>api/polls/<int:pk>/</b> (где poll_pk - id опроса)<br>
Запрос: <b>PUT</b><br>
Параметры (можно указать лишь те параметры, которые необходимо изменить):<br>
<ul>
  <li><b>"title"</b>: "Название опроса (не больше 255 символов)"</li>
  <li><b>"description"</b>: "Подробное описание опроса"</li>
  <li><b>"start_date"</b>: "Дата начала опроса в формате YYYY-MM-DD"</li>
  <li><b>"end_date"</b>: "Дата завершения опроса в формате YYYY-MM-DD"</li>
</ul>
Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>

Удалить опрос.<br>
Адрес: <b>api/polls/<int:pk>/</b> (где poll_pk - id опроса)<br>
Запрос: <b>DELETE</b><br>
Параметры: без параметров.<br>
Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>

<h5>Управление вопросами</h5>

После того, как Вы создали опрос, можно подключить к нему вопросы.<br><br>

Получить список всех вопросов указанного опроса.<br>
Адрес: <b>api/polls/<int:poll_pk>/questions/</b> (где poll_pk - id опроса, для которого создаётся вопрос)<br>
Запрос: <b>GET</b><br>
Параметры: без параметров.<br>
Ответ: список вопросов<br>
<ul>
  <li><b>"id"</b>: "id вопроса"</li>
  <li><b>"poll"</b>: "id опроса"</li>
  <li><b>"type"</b>: "Тип предполагаемого ответа: TX - ответ текстом, OC - выбор одного варианта, MC - выбор нескольких вариантов"</li>
  <li><b>"text"</b>: "Текст вопроса"</li>
</ul>

Создать новый вопрос.<br>
Адрес: <b>api/polls/<int:poll_pk>/questions/</b> (где poll_pk - id опроса, для которого создаётся вопрос)<br>
Запрос: <b>POST</b><br>
Параметры:<br>
<ul>
  <li><b>"poll"</b>: "id опроса, для которого создаётся вопрос"</li>
  <li><b>"type"</b>: "Тип предполагаемого ответа: TX - ответ текстом, OC - выбор одного варианта, MC - выбор нескольких вариантов"</li>
  <li><b>"text"</b>: "Текст вопроса"</li>
</ul>
Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>

Изменить существующий вопрос.<br>
Адрес: <b>api/polls/<int:poll_pk>/questions/<int:pk></b> (где poll_pk - id опроса, pk - id вопроса)<br>
Запрос: <b>PUT</b><br>
Параметры (можно указать лишь те параметры, которые необходимо изменить):<br>
<ul>
  <li><b>"poll"</b>: "id опроса, для которого создаётся вопрос"</li>
  <li><b>"type"</b>: "Тип предполагаемого ответа: TX - ответ текстом, OC - выбор одного варианта, MC - выбор нескольких вариантов"</li>
  <li><b>"text"</b>: "Текст вопроса"</li>
</ul>
Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>

Удалить вопрос.<br>
Адрес: <b>api/polls/<int:poll_pk>/questions/<int:pk></b> (где poll_pk - id опроса, pk - id вопроса)<br>
Запрос: <b>DELETE</b><br>
Параметры: без параметров.<br>
Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>


<h5>Управление вариантами ответов</h5>

После того, как Вы создали вопросы, можно подключить к ним варианты ответов (для тех вопросов, которые предполагают выбор из вариантов).<br><br>

Получить список всех вариантов ответа указанного вопроса.<br>
Адрес: <b>polls/<int:poll_pk>/questions/<int:question_pk>/choices/</b> (где poll_pk - id опроса, question_pk - id вопроса, для которого создаётся вариант ответа)<br>
Запрос: <b>GET</b><br>
Параметры: без параметров.<br>
Ответ: список ответов<br>
<ul>
  <li><b>"id"</b>: "id ответа"</li>
  <li><b>"question"</b>: "id вопроса"</li>
  <li><b>"text"</b>: "Текст варианта ответа"</li>
</ul>

Создать новый ответ.<br>
Адрес: <b>polls/<int:poll_pk>/questions/<int:question_pk>/choices/</b> (где poll_pk - id опроса, question_pk - id вопроса, для которого создаётся вариант ответа)<br>
Запрос: <b>POST</b><br>
Параметры:<br>
<ul>
  <li><b>"question"</b>: "id вопроса, для которого создаётся вариант ответа"</li>
  <li><b>"text"</b>: "Текст варианта ответа"</li>
</ul>
Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>

Изменить существующий ответ.<br>
Адрес: <b>polls/<int:poll_pk>/questions/<int:question_pk>/choices/<int:pk></b> (где poll_pk - id опроса, pk - id вопроса, pk - id варианта ответа)<br>
Запрос: <b>PUT</b><br>
Параметры (можно указать лишь те параметры, которые необходимо изменить):<br>
<ul>
  <li><b>"question"</b>: "id вопроса, для которого создаётся вариант ответа"</li>
  <li><b>"text"</b>: "Текст варианта ответа"</li>
</ul>
Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>

Удалить ответ.<br>
Адрес: <b>polls/<int:poll_pk>/questions/<int:question_pk>/choices/<int:pk></b> (где poll_pk - id опроса, pk - id вопроса, pk - id варианта ответа)<br>
Запрос: <b>DELETE</b><br>
Параметры: без параметров.<br>
Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>



<h3>2. Функционал пользователя</h3>

<h5>Авторизация</h5>

Пользователю не нужно проходить авторизацию.<br>
Аутентификация происходит по произвольно выбранному ID для конкретного пользователя.<br>

<h5>Просмотр опросов</h5>

Получить список всех опросов.<br>
Адрес: <b>api/polls/</b><br>
Запрос: <b>GET</b><br>
Параметры: без параметров.<br>
Ответ: список опросов<br>
<ul>
  <li><b>"id"</b>: "id опроса"</li>
  <li><b>"title"</b>: "Название опроса"</li>
  <li><b>"description"</b>: "Описание опроса"</li>
  <li><b>"start_date"</b>: "Дата начала опроса"</li>
  <li><b>"end_date"</b>: "Дата завершения опроса"</li>
</ul>

Выбрать опрос и получить список вопросов к нему.<br>
Адрес: <b>api/polls/<int:poll_pk>/questions/</b> (где poll_pk - id опроса, для которого создаётся вопрос)<br>
Запрос: <b>GET</b><br>
Параметры: без параметров.<br>
Ответ: список вопросов<br>
<ul>
  <li><b>"id"</b>: "id вопроса"</li>
  <li><b>"poll"</b>: "id опроса"</li>
  <li><b>"type"</b>: "Тип предполагаемого ответа: TX - ответ текстом, OC - выбор одного варианта, MC - выбор нескольких вариантов"</li>
  <li><b>"text"</b>: "Текст вопроса"</li>
</ul>

Просмотреть вопрос и получить список вариантов ответов.<br>
Адрес: <b>polls/<int:poll_pk>/questions/<int:question_pk>/</b> (где poll_pk - id опроса, question_pk - id вопроса, для которого создаётся вариант ответа)<br>
Запрос: <b>GET</b><br>
Параметры: без параметров.<br>
Ответ: список ответов<br>
<ul>
  <li><b>"id"</b>: "id вопроса"</li>
  <li><b>"poll"</b>: "id опроса"</li>
  <li><b>"type"</b>: "Тип предполагаемого ответа: TX - ответ текстом, OC - выбор одного варианта, MC - выбор нескольких вариантов"</li>
  <li><b>"text"</b>: "Текст вопроса"</li>
  <li>
  <ul>
  <li><b>"id"</b>: "id ответа"</li>
  <li><b>"question"</b>: "id вопроса"</li>
  <li><b>"text"</b>: "Текст варианта ответа"</li>
  </ul
  </li>
</ul>

<h5>Отправка ответов</h5>

После того, как пользователь ответил на все вопросы, он может загрузить ответы на сервер.<br>
Адрес: <b>api/polls/<int:poll_pk>/answers/</b> (где poll_pk - id опроса)<br>
Запрос: <b>POST</b><br>
Параметры: список ответов<br>
<ul>
  <li><b>"user_id"</b>: "id пользователя"</li>
  <li><b>"question"</b>: "id вопроса"</li>
  <li><b>"text_answer"</b>: "Ответ текстом (если предполагается ответ текстом. Иначе поле не требуется)"</li>
  <li><b>"choice_answer"</b>: "Список из одного или нескольких ответов (если предполагается ответ выбором)"</li>
</ul>
Пример:<br>
<source>
[<br>
    {<br>
        "user_id": "3",<br>
        "question": "1",<br>
        "text_answer": "This is a text answer for question #1."<br>
    },<br>
    {<br>
        "user_id": "3",<br>
        "question": "2",<br>
        "text_answer": "This is a text answer for question #2."<br>
    },<br>
    {<br>
        "user_id": "3",<br>
        "question": "3",<br>
        "choice_answer": ["2", "5"]<br>
    }    <br>
]<br>
</source>

Ответ:<br>
<ul>
  <li><b>"Success"</b>: "Сообщение сервера"</li>
</ul>

<h5>Просмотр пройденных опросов</h5>

Пользователь можем просматривать свои ответы на опросы, в которых он участвовал.<br>
Адрес: <b>api/answers/<int:user_id></b> (где user_id - id пользователя)<br>
Запрос: <b>GET</b><br>
Параметры: без параметров<br>
Ответ: список вопросов с ответами пользователя
<ul>
  <li><b>"user_id"</b>: "id пользователя"</li>
  <li><b>"question"</b>: "id вопроса"</li>
  <li><b>"text_answer"</b>: "Ответ текстом (если предполагается ответ текстом. Иначе поле не требуется)"</li>
  <li><b>"choice_answer"</b>: "Список из одного или нескольких ответов (если предполагается ответ выбором)"</li>
</ul>