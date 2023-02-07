from db.economy import mercado

async def on_recursos():
    
    recursos: list[dict[str,str | int]] = [

        {
            "name": "Diamante", 
            "compra": mercado.find_one({"_id": "mercado"})["diamante"]["compra"],
            "venda": mercado.find_one({"_id": "mercado"})["diamante"]["venda"]
        },

        {
            "name": "Ouro", 
            "compra": mercado.find_one({"_id": "mercado"})["ouro"]["compra"],
            "venda": mercado.find_one({"_id": "mercado"})["ouro"]["venda"]
        },

        {
            "name": "Ferro", 
            "compra": mercado.find_one({"_id": "mercado"})["ferro"]["compra"],
            "venda": mercado.find_one({"_id": "mercado"})["ferro"]["venda"]
        },

        {
            "name": "Esmeralda", 
            "compra": mercado.find_one({"_id": "mercado"})["esmeralda"]["compra"],
            "venda": mercado.find_one({"_id": "mercado"})["esmeralda"]["venda"]
        },

        {
            "name": "Prata", 
            "compra": mercado.find_one({"_id": "mercado"})["prata"]["compra"],
            "venda": mercado.find_one({"_id": "mercado"})["prata"]["venda"]
        },

        {
            "name": "Chumbo", 
            "compra": mercado.find_one({"_id": "mercado"})["chumbo"]["compra"],
            "venda": mercado.find_one({"_id": "mercado"})["chumbo"]["venda"]
        },

        {
            "name": "Madeira", 
            "compra": mercado.find_one({"_id": "mercado"})["madeira"]["compra"],
            "venda": mercado.find_one({"_id": "mercado"})["madeira"]["venda"]
        },

        {
            "name": "Perola", 
            "compra": mercado.find_one({"_id": "mercado"})["perola"]["compra"],
            "venda": mercado.find_one({"_id": "mercado"})["perola"]["venda"]
        }
        
    ]

    return recursos