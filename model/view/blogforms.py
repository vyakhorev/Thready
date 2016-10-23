
# Defines basic interface for a blog view (a.k.a. mediator)
class cBlogView():

    def getHTML(self):
        """
        :return: some HTML text representing the record
        """
        raise NotImplementedError

    def getCalls(self):
        """
        :return: a list of commands applicable to the record
        """
        raise NotImplementedError

# Create an instance of this, pass instructions + the cBlock, get a ready cBlogView inheritor class
class cBlogViewFactory():
    def __init__(self, block_class):
        self.block_class = block_class

    def getView(self):
        """
        :return: this should return  cBlogView with proper methods
        """
        return

    def setup(self):
        pass