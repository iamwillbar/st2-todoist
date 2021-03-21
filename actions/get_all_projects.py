from st2common.runners.base_action import Action

import requests, uuid, json

class GetAllProjectsAction(Action):
  def run(self):
    response = requests.get(
      "https://api.todoist.com/rest/v1/projects",
      headers={
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer %s" % self.config['api_token']
      })
    response.raise_for_status()
    return dict(projects=response.json())
