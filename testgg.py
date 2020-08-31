from googlesearch.googlesearch import GoogleSearch
response = GoogleSearch().search("faq covid 19")
for result in response.results:
    print("Title: " + result.title)
    print("Content: " + result.getText())
