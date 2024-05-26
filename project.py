import os
from ultralytics import YOLO
import cv2

# ByteTrack konfigürasyon dosyasını okumak için kullanılan fonksiyon artık gerekli değil

# Dosya yolunu belirleme
config_path = os.path.join(os.path.dirname(__file__), 'bytetracker.yaml')
print(f"Config path: {config_path}")  # Dosya yolunu yazdırarak kontrol etme

# YOLO modelini yükleme
model = YOLO('yolov8m.pt')

# Video kaynağını açma
video_path = 'Test Video.mp4'
cap = cv2.VideoCapture(video_path)

# Video çıktısı için hazırlık yapma
output_path = 'output.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Model ile tespit yapma ve ByteTrack ile takip etme
    results = model.track(source=frame, tracker=config_path)
    
    vehicle_count = 0  # Arac sayısını sıfırlama
    
    for result in results:
        for box in result.boxes:
            # Koordinatları alıp dikdörtgen çizme
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            vehicle_count += 1
    
    # Arac sayısını görüntüye yazma
    cv2.putText(frame, f'Vehicle Count: {vehicle_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Çıktı videosuna yazma
    out.write(frame)
    
    # İşlemi izleme
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Döngü bittiğinde kaynakları serbest bırakma
cap.release()
out.release()
cv2.destroyAllWindows()
