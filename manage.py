from app import wsgi
import bottle
import click
from settings import WSGI_OPTS, DEBUG


@click.group()
def manager():
    """Base Manager instance.

     All available commands will be mounted on this object.
    """
    pass


@manager.command()
@click.option('--host', default=WSGI_OPTS['host'], type=str, help='Set Application server host.')
@click.option('--port', default=WSGI_OPTS['port'], type=int, help='Set Application server port.')
@click.option('--server', default=WSGI_OPTS['server'], type=str, help='Set Application server wsgi container.')
@click.option('--reloader', default=WSGI_OPTS['reloader'], type=bool, help='Set Application server reloader option.')
@click.option('--debug', default=DEBUG, type=bool, help='Set Application server debug mode.')
def runserver(host, port, server, reloader, debug):
    """API geotag-CAAS

    Args:
        host (str): Application IP or domain name.
        port (int): Application port.
        server (str): Application wsgi server alias.
        reloader (bool): Enable Application auto-reload on change.
        debug (bool): Enable Application DEBUG mode.
    """

    @wsgi.route('/static/<filename:path>')
    def static_server(filename):
        return bottle.static_file(filename, root='static')

    bottle.debug(debug)

    bottle.run(
        app=wsgi,
        server=server,
        host=host,
        port=port,
        reloader=reloader
    )


if __name__ == '__main__':

    manager()
