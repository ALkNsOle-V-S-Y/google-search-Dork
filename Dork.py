# script py ALkNsOle

from googlesearch import search

def search_and_save_dork_results():
    dork = input("Enter your Google dork query: ")

    try:
        search_results = search(dork, num=10, stop=1000, pause=2)  
        filename = 'result.txt'

        with open(filename, 'w', encoding='utf-8') as f:
            for result in search_results:
                f.write(result + '\n')

        print(f'Google dork results saved to {filename}')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    search_and_save_dork_results()
