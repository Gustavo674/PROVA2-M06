import cv2
import os

# Diretório onde os frames rastreados estão salvos
frames_dir = 'frames'
output_dir = 'tracked_frames_haar'

# Verifica se o diretório de saída existe, se não, cria
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Carrega o classificador Haar Cascade
haar_cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_cascade_path)

# Ajuste dos parâmetros do Haar Cascade
scaleFactor = 1.1
minNeighbors = 5
minSize = (30, 30)

# Processa cada frame
for frame_name in sorted(os.listdir(frames_dir)):
    frame_path = os.path.join(frames_dir, frame_name)
    image = cv2.imread(frame_path)

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detecta rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors, minSize=minSize)
    
    # Filtra detecções por tamanho mínimo
    filtered_faces = [face for face in faces if face[2] > 50 and face[3] > 50]

    # Desenha retângulos ao redor dos rostos detectados
    for (x, y, w, h) in filtered_faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Salva a imagem com os rostos rastreados
    output_path = os.path.join(output_dir, frame_name)
    cv2.imwrite(output_path, image)

print(f"Rastreamento completo. Frames com rostos rastreados salvos em '{output_dir}'")
