from st2common.runners.base_action import Action

import requests, uuid, json

class DeleteProjectAction(Action):
  def run(self, project_id):
    self.logger.info(f"Deleting project {project_id}")
    response = requests.delete(
      f"https://api.todoist.com/rest/v1/projects/{project_id}",
      headers={
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer %s" % self.config['api_token']
      })
    response.raise_for_status()
    return True
