import json
from download import download

with open('test.json', 'r') as file_handle:
	articles = json.load(file_handle)
	for article in articles:
		file_name_to_save = '/home/trdat/Projects/tiny_spiders/data/mdpi/Applied_Mechanics/' + article['article_title'].replace(" ", "_") + '.pdf'
		link_download_pdf = article['link_download_pdf']
		print(file_name_to_save, '\n', link_download_pdf)
		path = download(link_download_pdf, file_name_to_save)