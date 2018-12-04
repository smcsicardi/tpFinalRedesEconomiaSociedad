import sys
import json
import pandas as pd

archivoJSON = sys.argv[1]
subreddit = sys.argv[2]
cantidadComments = int(sys.argv[3])
contador = 0

if subreddit == ".":
	subreddit = "reddit.com"

usuarios = []
commentIds = []
parentIds = []


with open(archivoJSON) as f:
	for line in f:
		comentario = json.loads(line)
		if comentario["subreddit"].lower() == subreddit:
			contador += 1
			print(contador)
			usuarios.append(comentario["author"])
			commentIds.append(comentario["id"])
			parentIds.append(comentario["parent_id"])
			if cantidadComments == contador:
				break
	cantidadComments = contador

df = pd.DataFrame()
df["user"] = usuarios
df["id"] = commentIds
df["parent"] = parentIds
df.to_csv('{}.{}.{}.comments.csv'.format(archivoJSON, subreddit, cantidadComments))