"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from cafe.drivers.unittest.json_report import JSONReport
from cafe.drivers.unittest.xml_report import XMLReport


class Reporter:

    def __init__(self, result_parser):
        self.result_parser = result_parser

    def generate_report(self, type, directory=None):
        if type == 'json':
            report = JSONReport()
        elif type == 'xml':
            report = XMLReport()

        report.generate_report(self.result_parser, directory=directory)
