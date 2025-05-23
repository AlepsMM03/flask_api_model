# API REST para Modelo Random Forest

Esta API carga un modelo `.pkl` y devuelve predicciones para una app móvil (por ejemplo, Ionic).

### Endpoint
POST `/predict`

**Body JSON:**
```json
{
  "features": [0.45, 123.4, 60]
}
```

**Response:**
```json
{
  "prediction": 1
}
```