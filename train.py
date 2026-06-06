from ultralytics import YOLO

# Cargar modelo base
model = YOLO("yolo11n.pt")

# Entrenar
model.train(
    data="dataSet/data.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)