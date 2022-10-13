import os
from zipfile import ZipFile


import bs4
import requests
import pandas as pd
from bs4 import BeautifulSoup


def load_from_link(
        url: str,
        file_name: str,
        unzip_func,
        unzip_args: dict,
        extension: str = "xml",
) -> str:
    """
    download xml or zip file and extract it if the file value for extension is zip

    :parameter
    ----------

    :param url: Url of the file.
    :param file_name: Name you want to save the file with
    :param unzip_func: function to unzip the file downloaded
    :param unzip_args: arguments to pass in the unzip function
    :param extension: extension of file it will get from the url
    :return: file_name
    """
    response = requests.get(url)
    with open(f"{file_name}.{extension}", "wb") as file:
        file.write(response.content)

    if extension == "zip":
        unzipped_file_path = unzip_func(**unzip_args)
        return unzipped_file_path
    return file_name


class Utility:
    """
    All the utility function for the completion of the question.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.unzipped_file_path = None

    @classmethod
    def init_load(
        cls,
        file_link,
        extension: str,
    ):
        file_path = load_from_link(
            url=file_link,
            file_name="interview",
            extension=extension,
            unzip_func=cls.unzip_file,
            unzip_args={"filename": "interview", "extension": extension}

        )
        return cls(filepath=file_path)

    @staticmethod
    def unzip_file(
        filename: str,
        key: str,
        root: str = "../",
    ):
        """
        Takes in filename and unzips it, if the file name is not a zipfile it will raise BadzipFile error.

        :param filename:
        :param key: str to search in the file name
        :param root: path where to search the file.
        :return: str or None
        """
        with ZipFile(filename, "r") as zipped_file:
            zipped_file.extractall()
        for dir_path, dir_names, file_names in os.walk(root):
            for file in file_names:
                if key in file.lower():
                    return f"{dir_path}/{file}"
        return None



    def find_in_xml_file(
        self,
        attrs: dict,
    ) -> list[bs4.PageElement]:
        """
        Finds the first element with the attribute as :attrs

        :param attrs: attributes associated with element you want to find.
        :param file_path: file path you want find the element in.
        :return: treasure: first link from the xml file with attrs
        """
        with open(f"{self.filepath}.xml", "r") as xml_file:
            soup = BeautifulSoup(xml_file, features="xml")
            treasure = soup.find(attrs=attrs)
        return treasure.contents

    def convert_to_csv(
        self,
        data: dict[str, list],
        filename: str = "result",
    ):
        """
        Takes in a dictionary where key(str) is treated as column name and value is treated as rows(should be list) and
        converts it to csv file.

        :parameter
        ----------

        :param data: Dict in form of {"column_name": [row_value_1, row_value_2], ..., }
        :param filename: Name of the file will be saved with.
        :return: None
        """
        data = pd.DataFrame(data=data)
        data.to_csv(filename)


LINK =  "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"