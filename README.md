# car_price_prediction(wip)


## Authorization
| Key | Value | add to |
| :--- | :--- | :--- |
| `Authorization` | value | Header |

## Request

```http
GET /
```

## Response

HTTP/1.1 200 OK

```{"brand":[all brands from the csv],"models":[all models from the csv],"gear_box":[all gear_box from the csv],"trim":[all versions from the csv], "energy":[all energy type from the csv]}```


## Request
```http
POST /predict
```
| Key | Type | Description |
| :--- | :--- | :--- |
| `brand` | `string` | brand name |
| `model` | `string` | model name |
| `gear_box` | `string` | gear_box name |
| `trim` | `string` | trim name |
| `energy` | `string` | energy type |
| `purchase_year` | `int` | purchase_year |

## Response
HTTP/1.1 200 OK
-> predicted price

## build docker image
``` 
docker image build -t python-docker .
```

## run docker container and expose port 
```
docker run -p 5000:5000 python-docker
```