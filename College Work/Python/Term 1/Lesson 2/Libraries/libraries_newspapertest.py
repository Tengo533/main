import newspaper
src_url = 'https://cnn.com'
cnn_paper = newspaper.build(src_url, memoize_articles=False)

print(f"\n\nCNN website number of articles: {cnn_paper.size()}\n\n")

count = 0
for article in cnn_paper.articles:
    print(article.url)
    if count == 30:
        print(f"\n\nREACHED MAX {count} ARTICLES")
        break 
    count += 1

print(f"\n\nFIRST ARTICLE\n\n")
article_1 = cnn_paper.articles[0]
article_1.download()
article_1.parse()
print( f"TITLE: {article_1.title}")
print( f"AUTHORS: {article_1.authors}")
print( article_1.text)