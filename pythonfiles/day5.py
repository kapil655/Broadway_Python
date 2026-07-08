<<<<<<< HEAD
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
=======
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
>>>>>>> df3427d2848eba3c94051b997d16cd23f97696d6
        print(item["type"], item["number"])