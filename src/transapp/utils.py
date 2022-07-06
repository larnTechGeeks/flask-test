import os
from datetime import datetime


class Util:
    """This class acts as source for creating helper functions consumed by the application.
    """
    @classmethod
    def get_database_dsn(self):
        """This method loads environment variables and uses them to create a dsn string that is used
            to initiate a database connection.
        """

        DB_USER = os.environ.get('DB_USER')
        DB_PASSWORD = os.environ.get('DB_PASSWORD')
        DB_HOST = os.environ.get('DB_HOST')
        DB_PORT = os.environ.get('DB_PORT')
        DB_NAME = os.environ.get('DB_NAME')

        dsn = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

        return dsn

    @classmethod
    def parse_string_to_date(self, value):
        """This method is used to parse date submitted by forms which are in string form 
            into the correct datetime format.
        """
        try:
            date_time_obj = datetime.strptime(value, '%Y-%m-%d')
            return date_time_obj, True
        except ValueError:
            return '', False


        

