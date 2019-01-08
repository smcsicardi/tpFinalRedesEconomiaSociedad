import sys
import json

archivoJSON = sys.argv[1]

usuarios = []
postIds = []
subreddit = []

contador = 0

with open(archivoJSON) as f:
	for line in f:
		contador += 1
		post = json.loads(line)
		usuarios.append(post["author"])
		postIds.append(post["id"])
		subreddit.append(post.get("subreddit"))
		print(contador)

import pandas as pd
df = pd.DataFrame()
df["user"] = usuarios
df["postId"] = postIds
df["subreddit"] = subreddit
df.to_csv('userPorPostId.csv')