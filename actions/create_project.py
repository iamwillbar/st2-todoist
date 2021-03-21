from st2common.runners.base_action import Action

import requests, uuid, json

class CreateProjectAction(Action):
  def run(self, name, parent_id, color, favorite):
    response = requests.post(
      "https://api.todoist.com/rest/v1/projects",
      data=json.dumps({
          "name": name,
          "parent_id": parent,
          "color": color,
          "favorite": favorite
      }),
      headers={
          "Content-Type": "application/json",
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer %s" % self.config['api_token']
      })
    response.raise_for_status()
    return response.json()
