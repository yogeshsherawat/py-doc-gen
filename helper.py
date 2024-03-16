

class Helper:

    @staticmethod
    def dump_json_data_to_json_file(data, filepath):
        import json
        with open(filepath, "w") as outfile:
            json.dump(data, outfile)
