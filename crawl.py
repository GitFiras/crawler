'''
Project: Crawler

    • Crawl: parameter url
    • download webpage: get(url) to get HTML
    • fetch all found links
    • fetch all found links in the links
    • Output: print urls found
    • draw a graph of all pages linked to
        ◦ output links for graphs before parse in the format, saved in a .txt file:
        ◦ routers/ → link1
        ◦ routers/ → link2
        ◦ routers/ → link3
- Use beautiful soup to structure HTML

Instructions
./crawl.py	→ start https://wikipedia/routers		--max 1000

Precautions:
    • Stay on the same main domain (ie. wikipedia.com)
    • broken links → status code
    • image links (non-HTML ) → content type header
    • Anchor links (pointers that link to the same page as a quick link) → ignore hash with “#…” (ie. #heading2) delete everything beyond href #.
    • De-duplicate webpages


Stopping conditions
    • Define a maximum number of links found and downloaded, based on a counter (--max 1000)
    • Define a maximum depth of steps (2)
        ◦ Queue (Python Queue or Python list)
        ◦ Insert complete url + count of ‘1’ into queue
        ◦ Downloader Processes items from the queue. Download url, Get links, put Links in the queue with count of ‘2’ as a tuple.
        ◦ Hash set, to see every url only once.
'''



