#!/usr/bin/env python

import sys
import click
import fontconfig

@click.command()
@click.argument('text', type=click.File(), required=True)
@click.option('-f', '--font', required=True, help="Path to font file to be checked")
@click.option('-o', '--output', default=sys.stdout)
def cli(text, font, output):
    
    ttf = fontconfig.FcFont(font)

    line = []
    for w in text.read().strip().split(" "):
        if all(ttf.has_char(c) for c in w):
            line.append(w)
        
    output.write(" ".join(line))
    output.write('\n')


if __name__ == '__main__':
    cli()
