from st2common.runners.base_action import Action

import requests, uuid, json

class CreateTaskAction(Action):
  def run(self, content, project_id, section_id, parent_id, order, label_ids, priority, due_string, due_date, due_datetime, due_lang, assignee):
    response = requests.post(
      "https://api.todoist.com/rest/v1/tasks",
      data=json.dumps({
          "content": content,
          "project_id": project_id,
          "section_id": section_id,
          "parent_id": parent_id,
          "order": order,
          "label_ids": label_ids,
          "priority": priority,
          "due_string": due_string,
          "due_date": due_date,
          "due_datetime": due_datetime,
          "due_lang": due_lang,
          "assignee": assignee
      }),
      headers={
          "Content-Type": "application/json",
          "X-Request-Id": str(uuid.uuid4()),
          "Authorization": "Bearer %s" % self.config['api_token']
      })
    response.raise_for_status()
    return dict(task=response.json())
