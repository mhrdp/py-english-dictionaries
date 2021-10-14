import requests

class Datamuse:
    def __init__(self, max_result=100):
        self.api_root = 'https://api.datamuse.com'
        self.max_result = max_result
        self.__validate_max__(max_result)

    # define static method to validate max result
    @staticmethod
    def __validate_max__(max_result):
        if not 0 < max_result <= 1000:
            raise ValueError

    # make request to the api and return as a json    
    def api_call(self, endpoint, **kwargs):
        # this will return: 'api_root/endpoint'
        url = '/'.join([self.api_root, endpoint])

        # request to API based on kwargs/URL parameters send by the function
        # kwargs is the 'key=val' inside function arguments
        response = requests.get(url, params=kwargs)

        # return in json format: [{'word': ..., 'score: ..., 'tags': [...]}, {...}]
        return response.json()
    
    def set_max_result(self, max_result):
        self.__validate_max__(max_result)
        self.max_result = max_result

    def words(self, **kwargs):
        """
        This endpoint returns a list of words (and multiword expressions) from
        a given vocabulary that match a given set of constraints.
        See <https://www.datamuse.com/api/> for the official Datamuse API
        documentation for the `/words` endpoint.

        :param `**kwargs`: Query parameters of constraints and hints.
        :return: A list of words matching that match the given constraints.
        """
        # if 'max' is not present in URL's parameters
        if 'max' not in kwargs:
            kwargs.update({'max': self.max_result})
        return self.api_call('words', **kwargs)
    
    def suggest(self, s, max_result=None, vocabulary=None):
        """
        This resource is useful as a backend for “autocomplete” widgets
        on websites and apps when the vocabulary of possible search terms
        is very large.
        It provides word suggestions given a partially-entered query
        using a combination of the operations.
        The suggestions perform live spelling correction and intelligently
        fall back to choices that are phonetically or semantically similar
        when an exact prefix match can't be found.

        :param s: Prefix hint string; typically, the characters that the user has entered so far into a search box.
        :param max_results: Maximum number of results to return, not to exceed 1000.
        :param vocabulary: The language vocabulary to use. Currently, `en` and `es` are supported.
        :return: A list of suggested words to the given string s.
        """
        parameter = {'s': s}
        if max_result is not None:
            parameter['max'] = max_result
        if vocabulary is not None:
            parameter['v'] = vocabulary
        return self.api_call('sug', **parameter)
