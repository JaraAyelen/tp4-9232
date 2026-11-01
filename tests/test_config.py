import unittest
import yaml
import os

class TestDockerComposeConfig(unittest.TestCase):
    def test_yaml_syntax(self):
                filepath = os.path.join(os.path.dirname(__file__), '..', 'docker-compose.yml')

        with open(filepath, 'r') as file:
            try:
                yaml.safe_load(file)
                valid = True
            except yaml.YAMLError:
                valid = False

        self.assertTrue(valid, "El archivo docker-compose.yml tiene errores de sintaxis")

if __name__ == '__main__':
    unittest.main()
