from ultralytics import YOLO

model = YOLO("best.pt")
model.predict(source="drone_footage_oil_spill_original.mp4", show=True, save=True, hide_labels=True , hide_conf=False, conf=0.5, save_txt=False, save_crop=False, line_thickness=2)