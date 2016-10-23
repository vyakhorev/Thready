# Defines interface for a block representation, links to the model
class cViewBlock():

    """
    This thing should ease access to the blog view factory and edit form factory.
    So that, to implement an actual block it would be enough to inherit this class
    and apply factory methods to get an actual class for views.

    I should also support direct form loading. To do so I have to think about edit
    form interface..
    """

    def __init__(self):
        self.blog_factory = None



    # responsible for "blog" view - main commands + fields + text
    def getViewBlog(self):
        """
        :return: something that inherits cInterfaceBlogView
        """
        raise NotImplementedError

    # responsible for representing the variable
    def getViewEditForm(self):
        """
        :return: something that inherits cInterfaceEditDialog
        """
        raise NotImplementedError