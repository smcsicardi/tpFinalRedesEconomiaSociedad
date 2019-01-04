import sys
import json

archivoJSON = sys.argv[1]

usuarios = []
postIds = []

contador = 0

with open(archivoJSON) as f:
	for line in f:
		contador += 1
		post = json.loads(line)
		print(contador)
		usuarios.append(post["author"])
		postIds.append(post["id"])

import pandas as pd
df = pd.DataFrame()
df["user"] = usuarios
df["postId"] = postIds
df.to_csv('userPorPostId.csv')