import re

# Source: https://blog.flozz.fr/2020/09/07/introduction-a-sphinx-un-outil-de-documentation-puissant/
# Source: https://blog.flozz.fr/2020/10/04/documenter-un-projet-python-avec-sphinx/
def translate(text):
    """Translate the given text to Parseltongue.

    :param str text: The text to translate.

    :returns: the translated text.
    :rtype: str
    """
    return re.sub(r"[\w\d]", "s", text)


class Snake:
    """This is a snake.

    :param str name: The snake's name.
    """

    def __init__(self, name):
        """The constructor."""
        self.name = name

    def move(self, x, y):
        """Moves the snake to given position.

        .. WARNING::

            Be careful to not tie knots when moving the snake!

        :param int x: The x position where move to.
        :param int y: The y position where move to.
        """
        pass

    def speak(self):
        """Makes the snake speak."""
        return translate("Hello, I'm a ssssssnake!")
