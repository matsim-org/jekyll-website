#!/usr/bin/env python
# Fetch latest MATSim blog posts via Confluence API

import urllib, json, yaml

num_posts_to_retrieve = 5

latest_posts_url = ( "https://matsim.atlassian.net/wiki/rest/api/content/search?" + 
                     "cql=type=blogpost%20order%20by%20created%20desc" + 
                     "&limit=" + str(num_posts_to_retrieve) +
                     "&expand=history,body.view")

posts = []

url = urllib.urlopen(latest_posts_url)
data = json.loads(url.read())    
results = data['results']
base_url = data['_links']['base']
        
for post in results:
      item = {}
      item['date'] = post['history']['createdDate'][:10]
      item['title'] = post['title']
      item['author'] = post['history']['createdBy']['displayName']
      item['author_link'] = base_url + '/display/~' + post['history']['createdBy']['username']
      item['link'] = base_url + post['_links']['webui']
      item['body'] = post['body']['view']['value']

      # todo: don't use default user image
      image = post['history']['createdBy']['profilePicture']['path'];
      item['image'] = 'https://matsim.atlassian.net' + image

      posts.append(item)        
      print item['date'], item['title']

outfile = open('_data/news.yml','w')
yaml.dump(posts, outfile, default_flow_style=False)      

url.close()
outfile.close()
