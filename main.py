import requests
from urllib.parse import urljoin
from pprint import pprint

TOKEN = ''
API_BASE_URL = 'https://api.vk.com/method/'
V = '5.21'

class VkUser:
  def __init__(self, user_id, token=TOKEN, version=V):
    self.token = token
    self.version = version
    self.user_id = user_id


  def get_friends(self):
    get_friends = urljoin(API_BASE_URL, 'friends.get')
    response = requests.get(get_friends, params={
      'access_token': self.token,
      'v': self.version,
      'user_id': self.user_id,
  })
    return response.json()['response']['items']


  def __and__(self, other):
    return set(user1.get_friends()) & set(user2.get_friends())

  def get_link(self):
    get_link = urljoin('https://vk.com/', 'id' + self.user_id)
    return get_link



if __name__ == '__main__':
  user1 = VkUser('7052838')
  user2 = VkUser('848547')
  user_profile = VkUser('7052838')
  user = user_profile.get_link()
  pprint(user1 & user2)
  pprint(user)