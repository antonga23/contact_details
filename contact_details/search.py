from googlesearch import search


def Query(query):

    my_results_list = []
    for i in search(query,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'en',  # The language
                    num = 10,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = 10,  # Last result to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                    ):
        print(i)
        my_results_list.append(i)
    # extract domain from the list of urls
    domain_list = []
    for i in my_results_list:
        domain_list.append(i.split("//")[-1].split("/")[0])
    # extract the domain name from the list of domains
    domain_name = []
    for i in domain_list:
        domain_name.append(i.split(".")[0])
    # write domain list to a file
    with open("domain_list.txt", "w") as f:
        for i in domain_list:
            f.write(i + "\n")
    print(domain_list)
    return domain_list


if __name__ == "__main__":
    Query("silversands affiliate")