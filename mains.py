from flask import Flask, jsonify, render_template, request

from project_app.utils import ItemOutletSales

app = Flask(__name__) 

@app.route("/")   
def hello_flask():
    print("Item Sales Prediction")
    return render_template("path.html")   

@app.route("/predict_sales",methods = ["POST", "GET"])
def get_sales_item():
    if request.method == "GET":
        print("GET Method")

        Item_Weight = eval(request.args.get("Item_Weight"))
        Item_Fat_Content = request.args.get("Item_Fat_Content")
        Item_Visibility = eval(request.args.get("Item_Visibility"))
        Item_MRP = eval(request.args.get("Item_MRP"))
        Outlet_Establishment_Year = request.args.get("Outlet_Establishment_Year")
        Outlet_Size= request.args.get("Outlet_Size")
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")

        Item_Type = request.args.get("Item_Type")
        Outlet_Identifier = request.args.get("Outlet_Identifier")
        Outlet_Type = request.args.get("Outlet_Type")

        item_sales = ItemOutletSales(Item_Weight,Item_Fat_Content,Item_Visibility,Item_MRP,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Item_Type,Outlet_Identifier,Outlet_Type)
         
        sales = item_sales.get_predicted_sales_item()

        return render_template("path.html", prediction = sales)
    

print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run()

