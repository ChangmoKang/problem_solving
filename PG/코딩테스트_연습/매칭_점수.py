import re

def solution(word, pages):
    url_finder = re.compile('<meta property="og:url" content="https://(.+)"/>')
    link_finder = re.compile('<a href="https://(.*)">')
    
    result = {}
    for i, page in enumerate(pages):
        page_url = url_finder.findall(page)[0]
        basic_result = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())
        # link_result = link_finder.findall(page)
        
        link_result = []
        links = page.split('a href="https://')
        for link in links[1:]:
            link_result.append(link.split('"')[0])
            
        result[page_url] = {
            "index": i,
            "link_list": link_result,
            "basic_score": basic_result,
            "link_score": 0
        }
    
    for info in result.values():
        for link in info['link_list']:
            if link in result:
                result[link]['link_score'] += info['basic_score'] / len(info['link_list'])
    
    for url, info in result.items():
        result[url]['match_score'] = info['basic_score'] + info['link_score']

    for info in sorted(result.values(), key=lambda x: (-x['match_score'], x['index'])):
        return info['index']
