import pandas as pd


def get_name(split_list: list) -> str:
    if len(split_list[1]) > 6:
        return split_list[0]
    return split_list[0] + " " + split_list[1]


def get_university(split_list: list) -> str:
    devel = "Development"
    dep = "Department"
    lab = "Laboratory"
    if split_list[2].find(devel) == -1 and split_list[2].find(dep) == -1 and split_list[2].find(lab) == -1:
        if len(split_list[1]) > 6:
            return split_list[1]
        return split_list[2]
    return split_list[3]


def get_country(split_list: list) -> str:
    return split_list[-1]


def main():
    scopus_data_to_list_split = []
    name_list = []
    university_list = []
    country_list = []
    scopus_data = pd.read_csv("scopus2020.csv")['Authors with affiliations']
    scopus_data_to_list = scopus_data.to_list()

    for elem in scopus_data_to_list:
        for item in elem.split("; "):
            scopus_data_to_list_split.append(item)
        scopus_data_to_list_split.append("")
    for elem in scopus_data_to_list_split:
        elem_split = elem.split(', ')
        if len(elem_split) == 1:
            name_list.append("")
            university_list.append("")
            country_list.append("")
            continue
        name_list.append(get_name(elem_split))
        try:
            university_list.append(get_university(elem_split))
            country_list.append(get_country(elem_split))
        except IndexError:
            university_list.append("Not")
            country_list.append("Not")
    result_df = pd.DataFrame({'Author': name_list, 'University': university_list, 'Country': country_list})
    result_df.to_excel("result.xlsx", index=False)
