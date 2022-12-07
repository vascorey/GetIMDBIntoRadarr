from arrapi import RadarrAPI
from arrapi.exceptions import NotFound, ArrException
import get_imdbs
import json
import requests

baseurl = "https://qiweh.nephele.usbx.me/radarr/"
apikey = "c8d6b1e2f5ff4ef6b82164d055dc953a"
exclusions_api_url = f"{baseurl}/api/v3/exclusions?apikey={apikey}"
excluded = requests.get(exclusions_api_url).json()

movies_to_add = get_imdbs.get_cool_movies()
radarr = RadarrAPI(baseurl, apikey)

def check_excluded(title):
	for exc in excluded:
		if title == exc['movieTitle']:
			return True
	return False

for m in movies_to_add:
	try:
		movie = radarr.get_movie(imdb_id=m)
	except NotFound as n:
		print(n)
	except ArrException as a:
		print(a)
	if movie.id == None:
		if check_excluded(movie.title):
			print(f"{datetime.datetime.now()} || {movie} is excluded")
		else:
			try:
				print(f"{datetime.datetime.now()} || Add movie: {movie}")
				movie.add(root_folder=1, minimum_availability='released', quality_profile='Any', tags=['addedByRadarrScript'])
			except ArrException as a:
				print(a)
	else:
		print(f"{datetime.datetime.now()} || Movie already exists: {movie}")
print()
