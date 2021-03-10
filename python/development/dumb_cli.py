import click


@click.group()
def main():
    pass

@main.command(help='Take a letter and print its corresponding ascii number')
@click.argument('letter')
def l2n(letter):
    print(ord(letter))

@main.command(help='Take an ascii number and print its corresponding letter')
@click.option('--upper', '-u', help='Print upper-case letter', default=False)
@click.argument('number')
def n2l(number, upper):
    number = int(number)
    if upper:
        print(chr(number).upper())
    else:
        print(chr(number).lower())


if __name__ == '__main__':
    main()