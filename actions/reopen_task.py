from st2common.runners.base_action import Action

import requests, uuid, json

class ReopenTaskAction(Action):
  def run(self, task_id):
    self.logger.info(f"Re-opening task {task_id}")
    response = requests.post(
      f"https://api.todoist.com/rest/v1/tasks/{task_id}/reopen",
      headers={
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer %s" % self.config['api_token']
      })
    response.raise_for_status()
    return True
