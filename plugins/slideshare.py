from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import directives, Directive


class SlideShare(Directive):
    """ Embed Slideshare slides in posts.

    Based on the YouTube directive by Brian Hsu:
    https://gist.github.com/1422773

    Usage:
    .. slideshare:: VIDEO_ID
    """

    def boolean(argument):
        """Conversion function for yes/no True/False."""
        value = directives.choice(argument, ('yes', 'True', 'no', 'False'))
        return value in ('yes', 'True')

    required_arguments = 1
    optional_arguments = 5
    option_spec = {
        'class': directives.unchanged,
        'width': directives.positive_int,
        'height': directives.positive_int,
        'marginwidth': directives.positive_int,
        'marginheight': directives.positive_int,
        'scrolling': boolean,
    }

    final_argument_whitespace = False
    has_content = False

    def run(self):
        slideshare_id = self.arguments[0].strip()
        url = 'https://www.slideshare.net/slideshow/embed_code/key/{}'.format(slideshare_id)

        width = self.options['width'] if 'width' in self.options else None
        height = self.options['height'] if 'height' in self.options else None
        marginwidth = self.options['marginwidth'] if 'marginwidth' in self.options else 0
        marginheight = self.options['marginheight'] if 'marginheight' in self.options else 0
        scrolling = self.options['scrolling'] if 'scrolling' in self.options else "no"

        # ('<iframe src="http://slideshare.net/slideshow'
                   # '/embed_code/%s" width="590" height="481" '
                   # 'marginwidth="0" marginheight="0" scrolling="no"></iframe>')
        iframe_arguments = [
            (width, 'width="{}"'),
            (height, 'height="{}"'),
            (marginwidth, 'marginwidth="{}"'),
            (marginheight, 'marginheight="{}"'),
            (scrolling, 'scrolling="{}"')
        ]

        embed_block = '<iframe src="{}" '.format(url)

        for value, format in iframe_arguments:
            embed_block += (format + ' ').format(value) if value else ''

        embed_block = embed_block[:-1] + '></iframe>'

        return [
            nodes.raw('', embed_block, format='html')
            # nodes.raw('', '</div>', format='html'),
        ]


def register():
    directives.register_directive('slideshare', SlideShare)
