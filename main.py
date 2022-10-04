from utils.utility import Utility, LINK


def main():
    """
    executes if the file is run as a root.
    """

    # Extraction of the first link with **dltins**

    interview = Utility.init_load(file_link=LINK, extension="xml")
    first_link = interview.find_in_xml_file(attrs={"name": "download_link"})

    # commenting everything below as this is related to zip file which causes problem while reading, and crashes my pc,
    # so I was unable to see the contents of the file and convert it to csv
    # but you can try convert_to_csv method which works exactly the way it is intended.
    # example
    # interview.convert_to_csv({"names": ['surej', 'bittu'], "age": [20, 22]}, filename="result.csv")

    # every thing related to work
    # work_file = Utility.init_load(file_link=first_link, extension="zip")

    # unzipped_file_path = work_file.unzip_file(key='dltins', root="./")

    # work_file.convert_to_csv(data={}, filename="result")


# todo Convert the contents of the xml into a CSV with the following header:
# todo FinInstrmGnlAttrbts.Id
# todo FinInstrmGnlAttrbts.FullNm
# todo FinInstrmGnlAttrbts.ClssfctnTp
# todo FinInstrmGnlAttrbts.CmmdtyDerivInd
# todo FinInstrmGnlAttrbts.NtnlCcy
# todo Issr

if __name__ == '__main__':
    main()
