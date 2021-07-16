def makeTeams(nTeams, nPlayers):
    try:
        if not (isinstance(nTeams, int) and isinstance(nPlayers, int)):
            raise TypeError('Arguments not integers!')
        elif nTeams == 0:
            raise ZeroDivisionError('No team specified!')

        elif nTeams < 0 or nPlayers < 0:
            raise ValueError("Input negative!")
        elif nPlayers % nTeams != 0:
            raise ValueError(('Remove ' + str(nPlayers % nTeams) + ' player(s)!'))

    except ZeroDivisionError as err:
        print(err)
        return
    except ValueError as err:
        print(err)
        return
    except TypeError as err:
        print(err)
        return
    else:
        return nPlayers // nTeams


def main():
    a = makeTeams(0, 10)
    b = makeTeams(5, 56)
    c = makeTeams(5, 55)
    print(a, b, c)


if __name__ == '__main__':
    main()