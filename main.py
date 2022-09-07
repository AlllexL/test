from urls import urls
from wrap import mark_the_time
from sevices import get_response


@mark_the_time
def main():
    """Get the sequence of urls and save the data in *.jsons"""

    get_response(urls)


if __name__ == '__main__':
    main()
