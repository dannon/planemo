"""Module describing the planemo ``conda_recipe_init`` command."""
import click
import os

from planemo.cli import command_function
from planemo import options

from planemo.conda import clone_bioconda_repo, write_bioconda_recipe


@click.option(
    '-p',
    '--package_name',
    type=click.STRING,
    prompt=True,
    help=("Give the name of a Bioconductor package "
          "to create a new conda recipe")
)
@click.option(
    '-c',
    '--clone/--no-clone',
    default=False,
    prompt=True,
    help=("Clone bioconda repository from github or not?")
)
@click.option(
    '-b',
    '--bioconda_dir_path',
    type=click.STRING,
    prompt=True,
    help=("Give the path to folder containing bioconda repository")
)
@click.option(
    '-u',
    '--update/--no-update',
    default=False,
    help=("Update an existing bioconda recipe")
)
@click.command('conda_recipe_init')
@command_function
def cli(ctx, **kwds):
    """Make a conda recipe, given a package name.

    package_name = motifbreakR

    bioconda_dir = '/Users/nturaga/Documents/workspace'.
    """
    package_name = kwds.get("package_name")
    clone = kwds.get("clone")
    update = kwds.get("update")
    bioconda_dir_path = kwds.get("bioconda_dir_path")
    write_bioconda_recipe(package_name, clone, update, bioconda_dir_path)
    return