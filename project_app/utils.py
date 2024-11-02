import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config   

class ItemOutletSales():
    def __init__(self,Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Identifier,Outlet_Type):

        self.Item_Weight = Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_MRP = Item_MRP
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type

        self.Item_Type_col = 'Item_Type_' + Item_Type
        self.Outlet_Identifier_col = 'Outlet_Identifier_' + Outlet_Identifier
        self.Outlet_Type_col = 'Outlet_Type_' + Outlet_Type
        
    def load_models(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.data_save_json = json.load(f)

            # self.column_names = np.array(self.data_save_json["column_names"]) 

    def get_predicted_sales_item(self):
            
        self.load_models()

        Item_Type_index = list(self.data_save_json['column_names']).index(self.Item_Type_col)
        Outlet_Identifier_index = list(self.data_save_json['column_names']).index(self.Outlet_Identifier_col)
        Outlet_Type_index = list(self.data_save_json['column_names']).index(self.Outlet_Type_col)

        # Item_Type_index = np.where(self.column_names == self.Item_Type_col)[0][0]
        # Outlet_Identifier_index = np.where(self.column_names == self.Outlet_Identifier_col)[0][0]
        # Outlet_Type_index = np.where(self.column_names == self.Outlet_Type_col)[0][0]

        array = np.zeros(len(self.data_save_json['column_names']))

        array[0] = self.Item_Weight
        array[1] = self.data_save_json["item_Fat_Content_select"][self.Item_Fat_Content]
        array[2] = self.Item_Visibility
        array[3] = self.Item_MRP 
        array[4] = self.data_save_json["outlet_Establishment_Year_select"][self.Outlet_Establishment_Year]
        array[5] = self.data_save_json["outlet_Size_select "][self.Outlet_Size]  
        array[6] = self.data_save_json["outlet_Location_Type_select"][self.Outlet_Location_Type]

        array[Item_Type_index] = 1
        array[Outlet_Identifier_index] = 1
        array[Outlet_Type_index] = 1
        array

        print("TESTING  an Array -->\n", array)

        sales = self.model.predict([array])[0]

        return int(sales)
    
if __name__ == "__main__":

    Item_Weight = 9.3 
    Item_Fat_Content = 'Regular'
    Item_Visibility = 0.016047
    Item_MRP = 249.80
    Outlet_Establishment_Year = '1985'
    Outlet_Size = "Medium"
    Outlet_Location_Type = "Tier 2"

    Item_Type = 'Snack Foods'
    Outlet_Identifier = 'OUT049'
    Outlet_Type = 'Supermarket Type2' 

    item_sales = ItemOutletSales(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Identifier,Outlet_Type)

    sales = item_sales.get_predicted_sales_item()

    print("The TOTAL SALES of an ITEM in a givenby outlates or store would be :", int(sales),"item sales")