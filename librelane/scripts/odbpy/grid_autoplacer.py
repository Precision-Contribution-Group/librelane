#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2025 LibreLane Contributors
import sys
from decimal import Decimal

from reader import click_odb, click


@click.group
def cli():
    pass


@click.command()
@click.option("-c", "--config", required=True, help="Configuration JSON input")

@click_odb
def macro_grid_autoplacer(reader, config):
    """
    Places a group of macro instances in a grid pattern.
    """

    db_units_per_micron = reader.block.getDbUnitsPerMicron()

    print(config)

    # read config
    # macros = {}
    # with open(config, "r") as config_file:
    #     for line in config_file:
    #         # Discard comments and empty lines
    #         line = line.split("#")[0].strip()
    #         if not line:
    #             continue
    #         line = line.split()
    #         name, x, y, orientation = line
    #         macro_data = [
    #             name,
    #             int(Decimal(x) * db_units_per_micron),
    #             int(Decimal(y) * db_units_per_micron),
    #             orientation,
    #         ]
    #         name_escaped = reader.escape_verilog_name(name)
    #         macros[name_escaped] = macro_data
    #
    # print("Placing the following macros:")
    # print(macros)
    #
    # print("Design name:", reader.name)
    #
    # macros_cnt = len(macros)
    # for inst in reader.block.getInsts():
    #     inst_name = inst.getName()
    #     if inst.isFixed():
    #         assert inst_name not in macros, inst_name
    #         continue
    #     if inst_name in macros:
    #         print("Placing", inst_name)
    #         macro_data = macros[inst_name]
    #         _, x, y, orientation = macro_data
    #         x = gridify(x, 5)
    #         y = gridify(y, 5)
    #         inst.setOrient(lef_rot_to_oa_rot(orientation))
    #         inst.setLocation(x, y)
    #         if fixed:
    #             inst.setPlacementStatus("FIRM")
    #         else:
    #             inst.setPlacementStatus("PLACED")
    #         del macros[inst_name]
    #
    # if len(macros):
    #     print("Declared macros not instantiated in design:", file=sys.stderr)
    #     for macro in macros.values():
    #         print(f"* {macro[0]}", file=sys.stderr)
    #     exit(1)
    #
    # print(f"Successfully placed {macros_cnt} instances.")


cli.add_command(macro_grid_autoplacer)

if __name__ == "__main__":
    cli()
