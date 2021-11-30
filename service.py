from collections import namedtuple
from xml.etree import ElementTree

import requests

Episode = namedtuple('Episode', 'title link pubdate show_id')


def download_data(url):
    resp = requests.get(url)
    resp.raise_for_status()
    dom = ElementTree.fromstring(resp.text)
    episode_count = len(dom.findall('channel/item'))
    episode_data = {}
    for idx, item in enumerate(dom.findall('channel/item')):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx - 1
        )
        episode_data[episode.show_id] = episode
    return episode_data


def get_latest_id(episode_data):
    latest_show_id = max(episode_data.keys())
    oldest_show_id = min(episode_data.keys())
    return latest_show_id, oldest_show_id
