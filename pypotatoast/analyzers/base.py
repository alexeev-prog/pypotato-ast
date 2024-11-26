import ast
from rich import print


class BasicAnalyzer:
	def __init__(self, code: str):
		self.tree = ast.parse(code)
		self.variables = []
		self.functions = []
		self.classes = []

	def analyze(self):
		for node in ast.walk(self.tree):
			if isinstance(node, ast.FunctionDef):
				if node.name in self.functions:
					continue

				print(f'[green][+][/green] Found function: {node.name}')
				self.functions.append(node.name)
			elif isinstance(node, ast.ClassDef):
				if node.name in self.classes:
					continue
				
				print(f'[green][+][/green] Found class: {node.name}')
				self.classes.append(node.name)
			elif isinstance(node, ast.Name):
				if node.id in self.variables:
					continue

				print(f'[green][+][/green] Found variable: {node.id}')
				self.variables.append(node.id)

		print('=' * 30)
		print(f'[*] Total functions count: {len(self.functions)}')
		print(f'[*] Total classes count: {len(self.classes)}')
		print(f'[*] Total variables count: {len(self.variables)}')
