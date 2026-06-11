#dictionary

user_Detail={
    "name":"kapil Joshi",
    "sim_card":[
        {
        "type":"ntc",
        "number":9768499902
    },
    {
        "type":"ncell",
        "number":9702029355
    
}
]
}
for item in user_Detail["sim_card"]:
        print(item["type"], item["number"])