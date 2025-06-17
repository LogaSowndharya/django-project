from django.shortcuts import render

data_list = []

def index(request):
    if request.method == "GET":
        id_ = request.GET.get("id", "")
        name = request.GET.get("name", "")
        email = request.GET.get("email", "")
        action = request.GET.get("action", "")

        if action == "Add" and id_ and name and email:
            exists = any(d["id"] == id_ and d["name"] == name and d["email"] == email for d in data_list)
            if not exists:
                data_list.append({"id": id_, "name": name, "email": email})

        elif action == "Delete" and id_:
            data_list[:] = [d for d in data_list if d["id"] != id_]

        elif action == "Update" and id_ and name:
            for d in data_list:
                if d["id"] == id_:
                    d["name"] = name
                    break

        elif action == "Show":
            return render(request, "show.html", {"data": data_list})

    return render(request, "index.html")
