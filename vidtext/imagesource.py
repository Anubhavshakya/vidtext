from rake_nltk import Rake
from google_images_download import google_images_download
def getImage(listData):
	r = Rake(min_length=1, max_length=10)
	li = listData
	r.extract_keywords_from_text(li)
	key_collection = r.get_ranked_phrases_with_scores()
	keyword = key_collection[0][1]
	response = google_images_download.googleimagesdownload()
	arguments = {"keywords":keyword,"limit":2,"print_urls":True}
	reponsePaths = response.download(arguments)
	path = reponsePaths[keyword][0]
	return path
