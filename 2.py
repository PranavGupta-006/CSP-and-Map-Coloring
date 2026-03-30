districts = [
    "Adilabad","Komaram Bheem","Nirmal","Mancherial","Nizamabad","Jagitial",
    "Peddapalli","Jayashankar","Bhadradri","Mulugu","Warangal Urban",
    "Warangal Rural","Jangaon","Mahabubabad","Khammam","Karimnagar",
    "Rajanna Sircilla","Kamareddy","Medak","Siddipet","Sangareddy",
    "Vikarabad","Hyderabad","Medchal","Rangareddy","Yadadri","Suryapet",
    "Nalgonda","Mahabubnagar","Narayanpet","Wanaparthy","Nagarkurnool",
    "Jogulamba Gadwal"
]

neighbors = {
    "Adilabad": ["Komaram Bheem","Nirmal"],
    "Komaram Bheem": ["Adilabad","Mancherial","Nirmal"],
    "Nirmal": ["Adilabad","Komaram Bheem","Nizamabad","Jagitial"],
    "Mancherial": ["Komaram Bheem","Jagitial","Peddapalli"],
    "Nizamabad": ["Nirmal","Kamareddy","Jagitial"],
    "Jagitial": ["Nirmal","Mancherial","Karimnagar","Rajanna Sircilla"],
    "Peddapalli": ["Mancherial","Karimnagar","Jayashankar"],
    "Jayashankar": ["Peddapalli","Mulugu","Bhadradri"],
    "Bhadradri": ["Jayashankar","Mulugu","Khammam"],
    "Mulugu": ["Jayashankar","Bhadradri","Warangal Rural"],
    "Warangal Urban": ["Warangal Rural","Jangaon","Karimnagar"],
    "Warangal Rural": ["Mulugu","Warangal Urban","Jangaon"],
    "Jangaon": ["Warangal Urban","Warangal Rural","Yadadri","Siddipet"],
    "Mahabubabad": ["Warangal Rural","Khammam","Jangaon"],
    "Khammam": ["Bhadradri","Mahabubabad","Suryapet"],
    "Karimnagar": ["Jagitial","Peddapalli","Warangal Urban","Rajanna Sircilla"],
    "Rajanna Sircilla": ["Karimnagar","Jagitial","Siddipet"],
    "Kamareddy": ["Nizamabad","Medak","Siddipet"],
    "Medak": ["Kamareddy","Sangareddy","Siddipet"],
    "Siddipet": ["Medak","Rajanna Sircilla","Jangaon","Yadadri"],
    "Sangareddy": ["Medak","Vikarabad","Medchal"],
    "Vikarabad": ["Sangareddy","Rangareddy"],
    "Hyderabad": ["Medchal","Rangareddy"],
    "Medchal": ["Hyderabad","Sangareddy","Rangareddy"],
    "Rangareddy": ["Vikarabad","Hyderabad","Medchal","Mahabubnagar"],
    "Yadadri": ["Jangaon","Siddipet","Nalgonda"],
    "Suryapet": ["Khammam","Nalgonda"],
    "Nalgonda": ["Yadadri","Suryapet","Mahabubnagar"],
    "Mahabubnagar": ["Rangareddy","Narayanpet","Wanaparthy","Nagarkurnool"],
    "Narayanpet": ["Mahabubnagar"],
    "Wanaparthy": ["Mahabubnagar","Nagarkurnool"],
    "Nagarkurnool": ["Mahabubnagar","Wanaparthy","Jogulamba Gadwal"],
    "Jogulamba Gadwal": ["Nagarkurnool"]
}

colors = ["Red","Green","Blue","Yellow"]

def is_valid(d, c, a):
    for n in neighbors[d]:
        if n in a and a[n] == c:
            return False
    return True

def backtrack(a):
    if len(a) == len(districts):
        return a
    u = [d for d in districts if d not in a][0]
    for c in colors:
        if is_valid(u, c, a):
            a[u] = c
            r = backtrack(a)
            if r:
                return r
            del a[u]
    return None

solution = backtrack({})
print(solution)