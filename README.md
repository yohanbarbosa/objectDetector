# Análisis de Métricas del Modelo YOLO11

## Precision

La métrica Precision indica el porcentaje de detecciones realizadas por el modelo que fueron correctas. Un valor alto significa que el modelo genera pocos falsos positivos.

Resultado obtenido:

* Precision = 0.932 (93.2%)

Esto indica que aproximadamente el 93.2% de las detecciones realizadas por el modelo corresponden correctamente a los objetos entrenados.

## Recall

La métrica Recall mide la capacidad del modelo para encontrar todos los objetos presentes en una imagen.

Resultado obtenido:

* Recall = 0.949 (94.9%)

Esto significa que el modelo detectó aproximadamente el 94.9% de los objetos reales presentes en el conjunto de validación.

## mAP@50

La métrica mAP@50 (mean Average Precision) evalúa el desempeño general del modelo utilizando un umbral IoU de 0.50.

Resultado obtenido:

* mAP@50 = 0.957 (95.7%)

Este resultado indica un excelente desempeño del modelo para identificar correctamente las clases Bag y Shoe.

## mAP@50-95

La métrica mAP@50-95 utiliza diferentes niveles de IoU entre 0.50 y 0.95, proporcionando una evaluación más exigente del modelo.

Resultado obtenido:

* mAP@50-95 = 0.637 (63.7%)

Este valor muestra que el modelo mantiene un buen rendimiento incluso bajo criterios de evaluación más estrictos.

## Conclusión

El modelo YOLO11 entrenado logró detectar correctamente las clases Bag y Shoe con una precisión superior al 93% y un recall cercano al 95%, obteniendo un desempeño satisfactorio para la tarea de detección de objetos propuesta.
