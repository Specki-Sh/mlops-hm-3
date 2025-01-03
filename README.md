# ML Model API

Домашняя работа #3 `Юсупов Шахзод`, используется модель из второго дз, 
[Amazon.com - Employee Access Challenge](https://www.kaggle.com/competitions/amazon-employee-access-challenge/data)

## Установка и запуск

### Локальный запуск

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Запустите приложение:
```bash
python -m app
```

### Запуск через Docker

1. Соберите Docker образ:
```bash
docker build -t ml-api .
```

2. Запустите контейнер:
```bash
docker run -p 8000:8000 ml-api
```

## API Endpoints

### Health Check
- GET `/health`
- Проверяет состояние сервиса
- Возвращает: `{"status": "success"}`

### Predict
- POST `/predict`
- Принимает JSON с входными данными (поддерживает как одиночные, так и пакетные предсказания)
- Возвращает предсказания модели и версию

#### Примеры запросов:

1. Одиночное предсказание:
```json
{
    "data": {
        "id": 1,
        "RESOURCE": 78766,
        "MGR_ID": 72734,
        "ROLE_ROLLUP_1": 118079,
        "ROLE_ROLLUP_2": 118080,
        "ROLE_DEPTNAME": 117878,
        "ROLE_TITLE": 117879,
        "ROLE_FAMILY_DESC": 118177,
        "ROLE_FAMILY": 19721,
        "ROLE_CODE": 117880
    }
}
```

2. Пакетное предсказание:
```json
{
    "data": [
        {
            "id": 1,
            "RESOURCE": 78766,
            "MGR_ID": 72734,
            "ROLE_ROLLUP_1": 118079,
            "ROLE_ROLLUP_2": 118080,
            "ROLE_DEPTNAME": 117878,
            "ROLE_TITLE": 117879,
            "ROLE_FAMILY_DESC": 118177,
            "ROLE_FAMILY": 19721,
            "ROLE_CODE": 117880
        },
        {
            "id": 2,
            "RESOURCE": 40644,
            "MGR_ID": 4378,
            "ROLE_ROLLUP_1": 117961,
            "ROLE_ROLLUP_2": 118327,
            "ROLE_DEPTNAME": 118507,
            "ROLE_TITLE": 118863,
            "ROLE_FAMILY_DESC": 122008,
            "ROLE_FAMILY": 118398,
            "ROLE_CODE": 118865
        }
    ]
}
```

#### Пример ответа:
```json
{
	"predictions": [
		{
			"id": 1,
			"prediction": 0.759767275142261,
			"model_version": "1.0.0"
		},
		{
			"id": 2,
			"prediction": 0.9931125554035115,
			"model_version": "1.0.0"
		}
	]
}
```

## Swagger документация

После запуска приложения, документация API доступна по адресу:
- http://localhost:8000/docs

## Примечания

- Убедитесь, что модель находится в папке `model/` с именем `model.cbm`