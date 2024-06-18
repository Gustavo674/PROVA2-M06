import cv2
import os

# Caminho do vídeo
video_path = 'la_cabra.mp4'  

# Diretório onde os frames serão salvos
output_dir = 'frames'

# Verifica se o diretório existe, se não, cria
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Captura o vídeo
video_capture = cv2.VideoCapture(video_path)

frame_count = 0
while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    frame_path = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_path, frame)
    frame_count += 1

video_capture.release()
print(f"Extração completa. {frame_count} frames salvos em '{output_dir}'")
