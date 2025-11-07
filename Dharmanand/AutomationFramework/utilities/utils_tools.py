import json

class Utils:
    def read_json_file(self, file_path):
        with open(file_path, "r") as file:
            data = file.read()
            json_data = json.loads(data)
        return json_data


if __name__ == "__main__":
    obj = Utils()
    data = obj.read_json_file("users_details.json")
    print(data)
    print(data['firstname'])