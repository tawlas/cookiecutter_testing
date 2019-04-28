# -*- coding: utf-8 -*-

"""Console script for cookiecutter_testing."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for cookiecutter_testing."""
    click.echo("Replace this message by putting your code into "
               "cookiecutter_testing.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
