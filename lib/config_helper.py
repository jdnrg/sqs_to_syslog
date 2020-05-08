import os
import yaml


class ConfigHelper(object):
    def __init__(self):
        config = self.read_yml('configs')
        self.rl_aws_region = config["redlock"]["aws_region"]
        self.rl_aws_queue = config["redlock"]["aws_sqs_queue"]
        self.rl_syslog_host = config["redlock"]["syslog_host"]


    @classmethod
    def read_yml(self, f):
        yml_path = os.path.join(os.path.dirname(__file__), "../config/%s.yml" % f)
        return yaml.load(file(yml_path, 'r'))
