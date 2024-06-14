# Prova-2-M06

## 1. Como instalar

Use o seguinte comando para clonar esse repositório em sua máquina:

```bash
git clone https://github.com/Gustavo674/PROVA2-M06.git
cd PROVA2-M06.git
```

## 1.1 Como fazer funcionar

Primeiro temos que separar o vídeo em frames, com a pasta da prova aberta, utilize o seguinte comando:

```bash
python3 extract_frames.py
```

Agora que temos os frames separados, podemos analisar cada um deles, para isso utilize o seguinte comando:

```bash
python3 face_tracking_haar.py
```

Agora para fazermos uma segunda verificada e gerar o vídeo com a análise, em seu terminal, utilize o seguinte comando:

```bash
python3 double_face_eye_tracking_haar.py
```

## 1.2 Caso queira testar com outro vídeo

Para testar com outro vídeo será necessário modificar os arquivos:

- extract_frames.py
```python
video_path = 'la_cabra.mp4'
```
Para:
```python
video_path = 'seu_vídeo.mp4'
```

- double_face_eye_tracking_haar.py

```python
cap = cv2.VideoCapture('la_cabra.mp4')
```
Para:
```python
cap = cv2.VideoCapture('seu_vídeo.mp4')
```

# Perguntas e Respostas

## 2.1 Descreva de maneira concisa (um parágrafo no máximo) o funcionamento do método de detecção escolhido.

## Resposta

Haar Cascade é um método eficaz de detecção de objetos, pois é uma abordagem baseada em Machine Learning, em que uma função cascade é treinada com muitas imagens positivas e negativas.

## 2.2 Considere as seguintes alternativas para resolver o problema de detecção de faces:

## HAAR Cascade
## CNN
## NN Linear
## Filtros de correlação cruzada
## Classifique-os (coloque em ordem) em termos de viabilidade técnica (se é possível resolver o problema), facilidade de implementação e versatilidade da solução. Justifique sua classificação.

## Resposta

1. HAAR Cascade é geralmente a opção mais fácil, devido sua implementação robusta no OpenCV e facilidade de uso com modelos pré-treinados. 

2. CNN a complexidade aumenta, mas também as capacidades e a precisão dos resultados também são maiores. 

3. Redes neurais lineares são simples, mas mais limitadas em aplicações mais complexas. 

4. Filtros de correlação cruzada são meio termo em complexidade e precisão.


## 2.3 Considerando as mesmas alternativas acima, faça uma nova classificação considerando a viabilidade técnica para detecção de emoções através da imagem de uma face.

## Resposta

1. CNN já que a capacidade e precisão dos resultados são maiores.

2. HAAR Cascade devido sua implementação e uso com modelos pré-treinados.

3. Filtros de correlação sendo menor capacidade e menor facilidade e uso.

4. Redes neurais lineares por conta da limitação em aplicações mais complexas.

## 2.4 A solução apresentada ou qualquer outra das que foram listadas na questão 2.2. tem a capacidade de considerar variações de um frame para outro (e.g. perceber que em um frame a pessoa está feliz e isso influenciar na detecção do próximo frame)? Se não, quais alterações poderiam ser feitas para que isso seja possível?

## Resposta

O HAAR Cascade possui capacidade para detectar a informação se a pessoa está feliz em um frame e no outro frame não, ja que seria treinado com mais um arquivo xml, por exemplo "haarcascade_smileface.xml".

## 2.5 Quem ganha a bola de ouro 2024?

## Resposta

Vini Jr.