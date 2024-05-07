class RequestClassDTO:
    def __init__(self, links, scenario_activation_question, scenario_steps):
        self.links = links
        self.scenario_activation_question = scenario_activation_question
        self.scenario_steps = scenario_steps

    def to_json(self):
        return {
            'links': self.links,
            'scenario_activation_question': self.scenario_activation_question,
            'scenario_steps': self.scenario_steps
        }