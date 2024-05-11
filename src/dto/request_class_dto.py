class RequestClassDTO:
    def __init__(self, request_class_title, links, scenario_activation_question, scenario_steps):
        self.request_class_title = request_class_title
        self.links = links
        self.scenario_activation_question = scenario_activation_question
        self.scenario_steps = scenario_steps

    def to_json(self):
        return {
            'request_class_title': self.request_class_title,
            'links': self.links,
            'scenario_activation_question': self.scenario_activation_question,
            'scenario_steps': self.scenario_steps
        }