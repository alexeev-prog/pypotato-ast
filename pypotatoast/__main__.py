import click
from pypotatoast.analyzers.base import BasicAnalyzer


@click.group()
def cli():
	"""
	A simple library based on AST Python for optimizing and debugging source code
	"""
	pass


@cli.command()
@click.argument('input_file')
def analyze(input_file: str):
	with open(input_file, 'r') as file:
		content = file.read()

	analyzer = BasicAnalyzer(content)
	analyzer.analyze()


if __name__ == '__main__':
	cli()
