class Page:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__url = kwargs.get('url')
        self.__filter_type = kwargs.get('filter_type') # xpath | selector
        self.__element = kwargs.get('element')
        self.__description = kwargs.get('description')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @url.deleter
    def url(self):
        del self.__url

    @property
    def filter_type(self):
        return self.__filter_type

    @filter_type.setter
    def filter_type(self, value):
        self.__filter_type = value

    @filter_type.deleter
    def filter_type(self):
        del self.__filter_type

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, value):
        self.__element = value

    @element.deleter
    def element(self):
        del self.__element

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @description.deleter
    def description(self):
        del self.__description
