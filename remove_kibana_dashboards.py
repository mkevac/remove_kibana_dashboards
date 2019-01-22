import requests

hostname = "google.com"
list_request = "https://{}/api/saved_objects/_find?type=dashboard&per_page=50&page=1&search_fields=title%5E3&search_fields=description"
delete_request = "https://{}/api/saved_objects/dashboard/{}"

# put your auth cookie if any here
auth_cookie = ""


def main():

    headers = {"Cookie": auth_cookie, "kbn-version": "6.4.0"}

    while True:

        res = requests.get(list_request.format(hostname), headers=headers)
        res = res.json()
        total = res["total"]

        print("Dashboards: {}".format(total))

        dashboards = [x["id"] for x in res["saved_objects"] if x["attributes"]['description'].startswith("automatically generated")]

        print("To delete: {}".format(len(dashboards)))

        for x in dashboards:
            print("Deleting dashboard {}".format(x))
            res = requests.delete(delete_request.format(hostname, x), headers=headers)
            if not res.ok:
                print(res)

if __name__ == "__main__":
    main()
