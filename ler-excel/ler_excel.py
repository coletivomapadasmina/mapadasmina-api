import pandas
import json

#constantes
excel_file = 'mapadasmina.xlsx'
sheet_name='respostas'

class ReadExcel():

    def __init__(self):
        candidates_dataframe = self.__read_excel_to_dataframe()     

        parties_list = self.__filter_parties_from_dataframe(candidates_dataframe)     
        roles_list = self.__filter_roles_from_dataframe(candidates_dataframe)

        candidates_dataframe=self.__find_role_party_ids_for_candidates(candidates_dataframe,parties_list,roles_list)

        parties_json=self.__convert_to_json(parties_list)
        roles_json=self.__convert_to_json(roles_list)
        candidates_json=self.__convert_to_json(candidates_dataframe)
        print (parties_json)
        print (roles_json)
        print (candidates_json)   
    

    def __read_excel_to_dataframe(self):
        candidates = pandas.ExcelFile(excel_file)
        data_frame = candidates.parse(sheet_name)
        return self.__trim_columns_from_dataframe(data_frame)
    
    def __trim_columns_from_dataframe(self,dataframe):
        trim_strings = lambda x: x.strip() if type(x) is str else x
        return dataframe.applymap(trim_strings)
    
    def __filter_parties_from_dataframe(self,candidates):
        return candidates['party'].unique().tolist()

    def __filter_roles_from_dataframe(self,candidates):
        return candidates['role'].unique().tolist()

    def __find_role_party_ids_for_candidates(self,candidates_dataframe,parties_list,roles_list):
        number_of_candidates = len(candidates_dataframe)
        party_id_list=[None]*number_of_candidates
        role_id_list=[None]*number_of_candidates
        for i in range(0,number_of_candidates):
            party_name = candidates_dataframe.at[i,'party']
            role_name = candidates_dataframe.at[i,'role']
            party_id_list[i] = parties_list.index(party_name)
            role_id_list[i] = roles_list.index(role_name)
        candidates_dataframe['party_id'] = party_id_list  
        candidates_dataframe['role_id'] = role_id_list
        return candidates_dataframe

    def __convert_to_json(self,object_to_convert):
        if isinstance(object_to_convert, list):           
            return json.dumps(object_to_convert)
        elif isinstance(object_to_convert, pandas.DataFrame):
            return object_to_convert.to_json

ReadExcel()


