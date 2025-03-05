import sys
import cv2
import numpy as np
from deepface import DeepFace
import pandas as pd
import random 

# コマンドライン引数から画像パスを取得
image_path = sys.argv[1]

# 画像を読み込む
img = cv2.imread(image_path)

# DeepFaceで感情分析
result = DeepFace.analyze(img, actions=['emotion'])
emotion = result[0]['dominant_emotion']

# 結果を標準出力

df = pd.read_csv("output.csv")

if emotion == "happy":
    results = df[(df['energy'] >= 0.5) & (df['valence'] >= 0.5)]['URL'].tolist()
elif emotion == "sad":
    results = df[(df['energy'] <= 0.5) & (df['valence'] <= 0.5)]['URL'].tolist()
elif emotion == "angry":
    results = df[(df['energy'] >= 0.5) & (df['valence'] <= 0.5)]['URL'].tolist()
elif emotion == "disgust":
    results = df[(df['energy'] >= 0.5) & (df['valence'] <= 0.5)]['URL'].tolist()
elif emotion == "surprise":
    results = df[(df['energy'] >= 0.5) & (df['valence'] >= 0.5)]['URL'].tolist()
elif emotion == "fear":
    results = df[(df['energy'] >= 0.5) & (df['valence'] <= 0.5)]['URL'].tolist()
elif emotion == "neutral":
    results = df[(df['energy'] >= 0.3) & (df['energy'] <= 0.7) & (df['valence'] >= 0.3) & (df['valence'] <= 0.7)]['URL'].tolist()

if results:
    random_result = random.choice(results)
    print(emotion+','+random_result)

else:
    print("can't find date")
