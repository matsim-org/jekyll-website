#!/usr/bin/env python
# Fetch latest MATSim blog posts via Confluence API

import urllib, json, yaml
import xml.etree.ElementTree as ET

num_posts_to_retrieve = 5

latest_posts_url = ( "https://matsim.atlassian.net/wiki/rest/api/content/search?" +
                     "cql=type=blogpost%20order%20by%20created%20desc" +
                     "&limit=" + str(num_posts_to_retrieve) +
                     "&expand=history,body.view")

def remove_tag(content, tagStart, tagEnd):
    start = content.find(tagStart)
    if (start<0):
       print('### not found!')
       return content

    end = content.find(tagEnd, start) + 2
    stripped = content[:start] + content[end:]

    print '### found'

    return remove_tag(stripped, tagStart, tagEnd)

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

      # fix relative links to /wiki
      body = post['body']['view']['value']
      body = body.replace('="/wiki', '="https://matsim.atlassian.net/wiki')

      # strip out confluence images. Screw you Confluence! You suck.
      # cleaned = remove_tag(body, '<img ', '/>')
      item['body'] = body #cleaned

      # todo: don't use default user image
      image = post['history']['createdBy']['profilePicture']['path'];
      item['image'] = None # 'https://matsim.atlassian.net' + image

      posts.append(item)
      print item['date'], item['title']

outfile = open('_data/news.yml','w')
yaml.dump(posts, outfile, default_flow_style=False)

url.close()
outfile.close()
