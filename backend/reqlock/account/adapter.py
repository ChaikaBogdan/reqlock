from allauth.account.adapter import DefaultAccountAdapter as DAA


class DefaultAccountAdapter(DAA):

    def add_message(*args, **kwargs):
        """
        Prevent adding messages to django admin
        For example on user confirming email
        """
        pass
